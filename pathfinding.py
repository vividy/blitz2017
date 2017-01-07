import re
import requests

BASE_URL = "http://game.blitz.codes:8081/pathfinding/direction"


def pathfinding( map, start, target):
    params = {'map': map.tiles, 'size' : map.size, 'start' : "({0},{1})".format(start[0], start[1]), 'target' : "({0},{1})".format(target[0], target[1])}
    r = requests.get(BASE_URL, params=params, timeout=10*60)
    if r.status_code == 200:
        print(r.json())
    else:
        print("Error path")
        print(r.text)
