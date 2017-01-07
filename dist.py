#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests


def minDist(pos, game):
	burger_loc = (-1, -1)
	burger_dist = -1
	fries_loc = (-1, -1)
	fries_dist = -1
	heroes_loc = (-1, -1)
	heroes_dist = -1
	for k, v in game.burger_locs:
		if (burger_dist == -1):
			burger_loc = (k, v)
			burger_dist = dist(pos, (k, v))
		elif burger_dist > dist(pos, (k, v)):
			burger_loc = (k, v)
			burger_dist = dist(pos, (k, v))
	for k, v in game.fries_locs:
		if (fries_dist == -1):
			fries_loc = (k, v)
			fries_dist = dist(pos, (k, v))
		elif fries_dist > dist(pos, (k, v)):
			fries_loc = (k, v)
			fries_dist = dist(pos, (k, v))
	for k, v in game.heroes_locs:
		if (k != pos[0] & v != pos[1]):
			if (heroes_dist == -1):
				heroes_loc = (k, v)
				heroes_dist = dist(pos, (k, v))
			elif heroes_dist > dist(pos, (k, v)):
				heroes_loc = (k, v)
				heroes_dist = dist(pos, (k, v))
	return([burger_loc, fries_loc, heroes_loc])

def dist(a, b):
	return ((((b[0] - a[0])) * (b[0] - a[0])) + ((b[1] - a[1]) * (b[1] - a[1])))
