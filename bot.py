from random import choice
from game import Game
from pathfinding import pathfinding
from timeout import timeout, TimeoutError


class Bot:
    pass


class RandomBot(Bot):
    def __init__(self):
        self.going = None

    @timeout(0.8)
    def move_less_one(self, state):
        game = Game(state)
        us = None
        ourPos = (0, 0)
        for it in game.heroes:
            if it.name == "Rimouski City Gang":
                us = it
                ourPos = (it.pos["x"], it.pos["y"])
                break;

        if not self.going:
            dist = -1
        min = None
        i = 0
        for x, y in game.customers_locs:
            customer = game.customers[i]
            pos = (x, y)
            tmp = (pos[0] - ourPos[0]) * (pos[1] - ourPos[1])
            if dist > tmp:
                min = customer
                dist = tmp
        friesOk = us.frenchFries >= customer.french_fries
        burgerOk = us.burger >= customer.burger
        if friesOk and burgerOk:
            self.going = pos
        elif not friesOk:
            min = None
            dist = -1
            id = game.board.tiles[ourPos[0]][ourPos[1]]
            for x, y in game.fries_locs:
                fries = game.board.tiles[x][y]
                tmp = (x - ourPos[0]) * (y - ourPos[1])
                if fries.hero_id != id and tmp < dist:
                    dist = tmp
                    min = (x, y)
            self.going = min
        else:
            min = None
            dist = -1
            id = game.board.tiles[ourPos[0]][ourPos[1]]
            for x, y in game.burger_locs:
                burger = game.board.tiles[x][y]
                tmp = (x - ourPos[0]) * (y - ourPos[1])
                if burger.hero_id != id and tmp < dist:
                    dist = tmp
                    min = (x, y)
            self.going = min
            pass

        ret = pathfinding(game.board, ourPos, self.going)
        print(ret)
        return ret
        # if (res[0] + ourPos[0], res[1] + ourPos[1]) == self.going:
        #     self.going = None

    def move(self, state):
        try:
            return self.move_less_one(state)
        except Exception as e:
            print(e)
            dirs = ['Stay', 'North', 'South', 'East', 'West']
            return choice(dirs)
