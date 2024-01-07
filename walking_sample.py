#!/usr/bin/env python3

import pybullet as p
import pybullet_data
import numpy as np
import sys
sys.path.append('./walking')
from kinematics import *
from foot_step_planner import *
from preview_control import *
from walking import *
from random import random 
from time import sleep
# import csv
import time

def walking_sim_demo(walking_speed_factor=1.0, goal_pos_x=1.0, goal_pos_y=0.0, goal_pos_theta=0.0):
  try:
    TIME_STEP = 0.001
    physicsClient = p.connect(p.GUI)
    p.setPhysicsEngineParameter(enableFileCaching=0)
    p.resetSimulation()
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0, 0, -9.8)
    p.setTimeStep(TIME_STEP)

    planeId = p.loadURDF("urdf/urdf/plane.urdf", [0, 0, 0])
    RobotId = p.loadURDF("urdf/urdf/thmos_mix.urdf", [0, 0, 0.43])  #0.43

    # 设置相机的初始位置和方向
    camera_distance = 1.0  # 相机到查看点的距离
    camera_yaw = 50  # 水平旋转角度
    camera_pitch = -35  # 垂直旋转角度
    camera_target_position = [0, 0, 0.5]  # 相机要指向的目标点

    # 重置相机视角
    p.resetDebugVisualizerCamera(cameraDistance=camera_distance,
                                cameraYaw=camera_yaw,
                                cameraPitch=camera_pitch,
                                cameraTargetPosition=camera_target_position)

    index = {p.getBodyInfo(RobotId)[0].decode('UTF-8'):-1,}
    for id in range(p.getNumJoints(RobotId)):
      index[p.getJointInfo(RobotId, id)[12].decode('UTF-8')] = id

    left_foot0  = p.getLinkState(RobotId, index['L_leg_6_link'])[0]
    right_foot0 = p.getLinkState(RobotId, index['R_leg_6_link'])[0]

    print(f'state:\nleft:{left_foot0}\nright:{right_foot0}')

    joint_angles = []
    for id in range(p.getNumJoints(RobotId)):
      if p.getJointInfo(RobotId, id)[3] > -1:
        joint_angles += [0,]

    left_foot  = [ left_foot0[0]-0.0,  left_foot0[1]+0.01,  left_foot0[2]-0.04]
    right_foot = [right_foot0[0]-0.0, right_foot0[1]-0.01, right_foot0[2]-0.04]

    pc = preview_control(0.01, 1.0, 0.30)
    walk = walking(RobotId, left_foot, right_foot, joint_angles, pc)

    index_dof = {p.getBodyInfo(RobotId)[0].decode('UTF-8'):-1,}
    for id in range(p.getNumJoints(RobotId)):
      index_dof[p.getJointInfo(RobotId, id)[12].decode('UTF-8')] = p.getJointInfo(RobotId, id)[3] - 7

    #goal position (x, y) theta
    t1 = time.time()
    foot_step = walk.setGoalPos([goal_pos_x, goal_pos_y, goal_pos_theta])
    print(f'set goal time:{time.time()-t1}')

    print("foot_step:",foot_step)
    j = 0
    while p.isConnected():
      j += 1
      if j >= 10:
        joint_angles,lf,rf,xp,n = walk.getNextPos()

        j = 0
        if n == 0:
          if (len(foot_step) <= 5):
            x_goal, y_goal, th = random()-0.5, random()-0.5, random()-0.5
            foot_step = walk.setGoalPos([x_goal, y_goal, th])
            break
          else:
            foot_step = walk.setGoalPos()

      for id in range(p.getNumJoints(RobotId)):
        qIndex = p.getJointInfo(RobotId, id)[3]
        if qIndex > -1:
          if 'leg' in p.getJointInfo(RobotId, id)[1].decode('UTF-8'):
            p.setJointMotorControl2(RobotId, id, p.POSITION_CONTROL, joint_angles[qIndex-15]) # R_leg_1 to L_leg_6: 15-26
      
      # 获取机器人的位置
      robot_pos, robot_orn = p.getBasePositionAndOrientation(RobotId)
      
      # 更新摄像机视角以跟随机器人
      p.resetDebugVisualizerCamera(cameraDistance=camera_distance,
                                  cameraYaw=camera_yaw,
                                  cameraPitch=camera_pitch,
                                  cameraTargetPosition=robot_pos)
      
      p.stepSimulation()
      sleep(walking_speed_factor/1000)
  #   print(f'total walking time:{time.time()-t1}')
  finally:
    p.resetSimulation()
    p.disconnect()
    print('PyBullet disconnected!')