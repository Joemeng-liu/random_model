# -*- coding:utf-8 -*-
""" class model  by lmj"""
import pybullet as p
import time
import pybullet_data
from random_table import *
from save_p import *


class one_model(object):
    def __init__(self, path, nameid, radius, x, y, z=0):
        self.y = y
        self.x = x
        self.nameid = nameid
        self.path = path
        self.radius = radius
        self.z = z

    def set_position(self, pose, orientation):
        """et poisition"""
        self.pose = pose
        self.orientation = orientation

    def model_size(self):
        """ size from center"""
        return self.x, self.y, self.z

    def parent_child(self, parent_model, child_model):
        """ choose parent, child"""
        self.parent = parent_model
        self.child = child_model

    def get_radius(self):
        return self.radius

def load_model(name, model_list):
    p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())  # optionally
    print("path", pybullet_data.getDataPath())
    p.setGravity(0, 0, -10)
    planeId = p.loadURDF("plane.urdf")
    cubeStartPos = [0, 0, 0.0]
    cubeStartOrientation = p.getQuaternionFromEuler([0, 0, 0])
    boxId = p.loadURDF("table/table.urdf", cubeStartPos, cubeStartOrientation)
    collision_object = []
    model_nameid = []
    classfull = False
    while len(collision_object) < 40:
        """"by czy"""
        if not classfull:
            for i in range(len(model_list)):
                classflag = False
                while not classflag:
                    classflag, collision_object = generate_object(model_list, collision_object, i)
            classfull = True
        flag, collision_object = generate_object(model_list, collision_object)
    for i in range(len(collision_object)):
        """by lmj"""
        cubeStartOrientation = p.getQuaternionFromEuler([0.0, 0.0, collision_object[i][1][5]])
        if collision_object[i][2].path == "model/chouti/urdf/chouti.urdf":
            many = randint(0, 15)
            if many != 0 and many < 5:
                joints = np.random.randint(0, 4, size=many)
                model_nameid.append(
                    p.loadURDF(collision_object[i][2].path, collision_object[i][1][:3], cubeStartOrientation))
                for jo in joints:
                    p.resetJointState(model_nameid[i], jo, 0.1)
                continue
        model_nameid.append(p.loadURDF(collision_object[i][2].path, collision_object[i][1][:3], cubeStartOrientation))
    for i in range(300):
        p.stepSimulation()
        time.sleep(1. / 240.)
        img_arr = p.getCameraImage(640, 640)
        arr = img_arr[2]
        arr = cv2.cvtColor(arr, cv2.COLOR_RGBA2BGR)
        cv2.imshow("Hello", arr)
        key = cv2.waitKey(1)
        print(i, k)
        if key & 0xff == ord('s'):
            optional_picture(arr, name)
            name += 1
        if key & 0xff == ord('q'):
            break
    cubePos, cubeOrn = p.getBasePositionAndOrientation(model_nameid[2])
    print(cubePos, cubeOrn)
    p.disconnect()
    return name

