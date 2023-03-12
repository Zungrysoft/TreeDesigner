from export import export # lol
import random


TRUNK_HEIGHT = 0
TRUNK_HEIGHT_VARIANCE = 0

TRUNK_THICKNESS = 0
TRUNK_THICKNESS_VARIANCE = 0

TRUNK_COLOR = 0
TRUNK_COLOR_VARIANCE = 0

TRUNK_THICKNESS = 0




def generate_tree(params):
    ret = {
        "0,0,0": [0.6, 0.6, 0.6],
        "0,0,1": [0.5, 0.2, 0.2],
        "0,0,3": [1, 0, 0],
    }

    # for i in range(25):
    #     ret[f"{random.randint(-5,5)},{random.randint(-5,5)},{random.randint(-5,5)}"] = [random.random(), random.random(), random.random()]

    return ret


export(generate_tree(None), "output")
