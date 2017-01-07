from random import choice
from game import Game
from pathfinding import pathfinding
from dist import *

class Bot:
    pass

class RandomBot(Bot):

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
		print(minDistBurger([5,5], game))
		print(minDistFries([5,5], game))
		print(minDistHero([5,5], game))
		dirs = ['Stay', 'North', 'South', 'East', 'West']
		res = pathfinding(game.board, (us.pos["x"], us.pos["y"]), (1, 0))
		return choice(dirs)