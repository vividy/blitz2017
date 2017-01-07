from random import choice
from game import Game
from pathfinding import pathfinding

class Bot:
    pass

class RandomBot(Bot):
	def minDist(self, pos, game):
		self.burger_loc = (-1, -1)
		self.fries_locs = (-1, -1)
		self.heroes_locs = (-1, -1)
		for k, v in game.burger_locs:
			burger_loc = (k, v)
		for k, v in game.fries_locs:
			fries_locs = (k, v)
		for k, v in game.heroes_locs:
			if (k != pos[0] & v != pos[1]):
				heroes_locs = (k, v)
		return([burger_loc, fries_locs, heroes_locs])

	# def move(self, state):
	# 	game = Game(state)
	# 	dirs = ['Stay', 'North', 'South', 'East', 'West']
	# 	pathfinding(game.board, (0,0), (1,0))
	# 	print(self.minDist([5,5], game))
	# 	print(game.board.size)
	# 	print(game.heroes[0].name)
	# 	print(game.board.tiles[game.heroes[0].pos['x']][game.heroes[0].pos['y']])
	# 	# for x in xrange(0,game.board.size):
	# 	# 	for y in game.board.tiles[x]
	# 	# 		print("x: " + x + "\ty: " + y + "\tcase: "+ game.board.tiles[x][])
	# 	return choice(dirs)
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