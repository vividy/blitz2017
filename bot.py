from random import choice
from game import Game
from pathfinding import pathfinding

class Bot:
    pass

class RandomBot(Bot):
    def move(self, state):
        game = Game(state)
        us = None
        for x in game.heroes:
            if (x.name == "Rimouski City Gang"):
                us = x
                break;
        dirs = ['Stay', 'North', 'South', 'East', 'West']
        res = pathfinding(game.board, (us.pos["x"], us.pos["y"]), (1, 0))
        return choice(dirs)
