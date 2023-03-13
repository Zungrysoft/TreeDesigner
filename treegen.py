from export import export # lol
import random
import math


TRUNK_HEIGHT = 0
TRUNK_HEIGHT_VARIANCE = 1

TRUNK_THICKNESS = 2
TRUNK_THICKNESS_VARIANCE = 3

TRUNK_COLOR = 0
TRUNK_COLOR_VARIANCE = 0

TRUNK_THICKNESS = 0

def lerp(f, a, b):
    return (a*(1-f)) + (b*f)

def set(vx, pos, color):
    str = f"{pos[0]},{pos[1]},{pos[2]}"
    if color == None:
        vx.pop(str)
    else:
        vx[str] = color

def fill_box(vx, pos1, pos2, color):
    for x in range(min(pos1[0],pos2[0]), max(pos1[0],pos2[0])+1):
        for y in range(min(pos1[1],pos2[1]), max(pos1[1],pos2[1])+1):
            for z in range(min(pos1[2],pos2[2]), max(pos1[2],pos2[2])+1):
                set(vx, [x, y, z], color)

def get_point_on_trunk(p1, p2, height, thickness1, thickness2):
    z = p1 * height
    thickness = lerp(p1, thickness1, thickness2)
    angle = p2 * 2 * math.pi
    x = math.cos(angle) * thickness
    y = math.sin(angle) * thickness

    return [round(x), round(y), round(z)]

def generate_tree(params):
    vx = {}

    height = params[TRUNK_HEIGHT] + ((random.random()-0.5) * params[TRUNK_HEIGHT_VARIANCE])
    height *= 40

    for i in range(1000):
        a = random.random()
        b = random.random()
        pt1 = get_point_on_trunk(a, b, height, 5, 3)

        a = random.random()
        b = random.random()
        pt2 = get_point_on_trunk(a, b, height, 5, 3)

        fill_box(vx, pt1, pt1, [0.5, 0.3, 0.1])
        fill_box(vx, pt2, pt2, [0.5, 0.3, 0.1])

    return vx

# Return random spots within a square such that each spot is a minimum distance from the others
def choose_spots(radius, spacing):
    chosen = []

    # Search a bunch of random spots
    spots_to_try = int(radius**2 / 10)
    for i in range(spots_to_try):
        x = round((random.random() - 0.5) * 2 * radius)
        y = round((random.random() - 0.5) * 2 * radius)
        z = 0

        # Make sure this potential spot is far enough away from all of the other spots before adding it
        far_enough = True
        for c in chosen:
            if (x-c[0])**2 + (y-c[1])**2 < spacing**2:
                far_enough = False
                break

        if far_enough:
            chosen.append([x, y, z])

    return chosen

# Merge vxm into vx at a specific position
# Useful for placing smaller objects into a larger scene
def merge_at(vx, vxm, pos):
    for voxel in vxm:
        coords = voxel.split(',')
        x = int(coords[0]) + pos[0]
        y = int(coords[1]) + pos[1]
        z = int(coords[2]) + pos[2]
        set(vx, [x, y, z], vxm[voxel])

def generate_forest(params, radius, spacing):
    vx = {}
    spots = choose_spots(radius, spacing)
    print(spots)
    for spot in spots:
        tree = generate_tree(params)
        merge_at(vx, tree, spot)

    return vx


params = [0.5, 0.1, 0.5, 0.1]

export(generate_forest(params, 40, 15), "output")
