from random import choice
from game import Game, AIM
from pathfinding import pathfinding
from dist import *
from timeout import timeout, TimeoutError


class Bot:
    pass


def random_choice():
    print("RANDOM")
    dirs = ['Stay', 'North', 'South', 'East', 'West']
    return choice(dirs)


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

        if self.going is None:
            dist = -1
            min = None
            i = 0
            id = game.board.tiles[ourPos[0]][ourPos[1]].id
            for x, y in game.customers_locs:
                customer = game.customers[i]
                pos = (x, y)
                dist = -1
                tmp = ((pos[0] - ourPos[0]) ** 2) + ((pos[1] - ourPos[1]) ** 2)
                if dist > tmp:
                    min = customer
                    dist = tmp
            friesOk = us.fries >= customer.french_fries
            burgerOk = us.burger >= customer.burger
            if friesOk and burgerOk:
                self.going = pos
            else:
                minF = None
                minB = None
                distF = float('infinity')
                distB = float('infinity')
                if not friesOk:
                    for x, y in game.fries_locs:
                        fries = game.board.tiles[x][y]
                        tmp = ((x - ourPos[0]) ** 2) + ((y - ourPos[1]) ** 2)
                        print(fries.hero_id, id, tmp, distF)
                        if fries.hero_id != id and tmp < distF:
                            distF = tmp
                            minF = (x, y)
                if not burgerOk:
                    for x, y in game.burger_locs:
                        burger = game.board.tiles[x][y]
                        tmp = ((x - ourPos[0]) ** 2) + ((y - ourPos[1]) ** 2)
                        if burger.hero_id != id and tmp < distB:
                            distB = tmp
                            minB = (x, y)
                self.going = (minF if distF < distB else minB)

        if self.going is None:
            return random_choice()

        ret = pathfinding(state['game']['board']['tiles'], game.board, ourPos, self.going)
        if ret is None:
            return random_choice()
        res = AIM[ret]
        if res[0] + ourPos[0] == self.going[0]  and res[1] + ourPos[1] == self.going[1]:
            self.going = None
        print(ret)
        return ret

    def move(self, state):
        try:
            return self.move_less_one(state)
        except :
            return random_choice()
