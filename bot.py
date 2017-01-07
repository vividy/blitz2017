from random import choice
from game import Game
import pathfinding


class Bot:
    pass

class RandomBot(Bot):
    def move(self, state):
        game = Game(state)
        dirs = ['Stay', 'North', 'South', 'East', 'West']
        pathfinding(game.board, 0, 1)
        return choice(dirs)
