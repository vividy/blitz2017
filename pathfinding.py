import re
import requests

BASE_URL = "http://game.blitz.codes:8081/pathfinding/direction"


def pathfinding( map, start, target):
    params = {'map': map.tiles, 'size' : map.size, 'start' : start, 'target' : target}

    r = requests.post(server_url + api_endpoint, params, timeout=10*60)
    if r.status_code == 200:
        print(r.json())
    else:
        print("Error path")
        print(r.text)
