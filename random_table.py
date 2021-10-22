import numpy as np
from random import *

scale = np.array([1.5, 1, 0.05]) * 100
radius = np.array([10, 10, 10, 10, 10, 10])
pi = 3.1415926
k = 6


def check_circular_collision(x1, x2):
    """by czy"""
    if np.linalg.norm(x1[1][:2] - x2[1][:2]) < np.linalg.norm(x1[0] + x2[0]):
        return True
    else:
        return False


def check_collision(body, collision_object):
    """by czy"""
    for i in range(len(collision_object)):
        if check_circular_collision(body, collision_object[i]):
            return True
    else:
        return False


def generate_object(model_list, collision_object, k="random", color="random"):
    if k == "random":
        k = randint(0, len(model_list) - 1)
    if color == "random":
        color = randint(0, 3)
    r = model_list[k][color].radius
    pose = uniform(-0.75 + 1 / 3 * r, 0.75 - 1 / 3 * r), uniform(-0.5 + 1 / 3 * r, 0.5 - 1 / 3 * r), \
           model_list[k][color].z, 0.0, 0.0, uniform(0, 2 * pi)
    pose = np.array(pose)
    body = (r, pose, model_list[k][color])
    flag = check_collision(body, collision_object)
    if not flag:
        collision_object.append(body)
        return not flag, collision_object
    else:
        return flag, collision_object
