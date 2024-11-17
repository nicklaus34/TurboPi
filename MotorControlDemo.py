#!/usr/bin/python3
# coding=utf8
import sys
sys.path.append('/home/pi/TurboPi/')
import time
import signal
import ros_robot_controller_sdk as rrc

if sys.version_info.major == 2:
    print('Please run this program with python!')
    sys.exit(0)
    
board = rrc.Board()

start = True
def Stop(signum, frame):
    global start

    start = False
    print('关闭中...')
    board.set_motor_duty([[1, 0], [2, 0], [3, 0], [4, 0]])  

signal.signal(signal.SIGINT, Stop)




def drive_forward(velocity, duration):
    if velocity>100:
        velocity=100
    if velocity<-100:
        velocity=-100
    if duration<=0:
        return -1
    runtime=0
    while runtime < duration:
        board.set_motor_duty([[1, -velocity]])  
        board.set_motor_duty([[2, velocity]])  
        board.set_motor_duty([[3, -velocity]])  
        board.set_motor_duty([[4, velocity]])
        time.sleep(1)
        runtime += 1
    board.set_motor_duty([[1, 0]])  
    board.set_motor_duty([[2, 0]])  
    board.set_motor_duty([[3, 0]])  
    board.set_motor_duty([[4, 0]])



def drive_backward(velocity, duration):
    if velocity>100:
        velocity=100
    if velocity<-100:
        velocity=-100
    if duration<=0:
        return -1
    runtime=0
    while runtime < duration:
        board.set_motor_duty([[1, velocity]])  
        board.set_motor_duty([[2, -velocity]])  
        board.set_motor_duty([[3, velocity]])  
        board.set_motor_duty([[4, -velocity]])
        time.sleep(1)
        runtime += 1
    board.set_motor_duty([[1, 0]])  
    board.set_motor_duty([[2, 0]])  
    board.set_motor_duty([[3, 0]])  
    board.set_motor_duty([[4, 0]])


def drive_left(velocity, duration):
    if velocity>100:
        velocity=100
    if velocity<-100:
        velocity=-100
    if duration<=0:
        return -1
    runtime=0
    while runtime < duration:
        board.set_motor_duty([[1, -velocity]])  
        board.set_motor_duty([[2, -velocity]])  
        board.set_motor_duty([[3, velocity]])  
        board.set_motor_duty([[4, velocity]])
        time.sleep(1)
        runtime += 1
    board.set_motor_duty([[1, 0]])  
    board.set_motor_duty([[2, 0]])  
    board.set_motor_duty([[3, 0]])  
    board.set_motor_duty([[4, 0]])

def drive_right(velocity, duration):
    if velocity>100:
        velocity=100
    if velocity<-100:
        velocity=-100
    if duration<=0:
        return -1
    runtime=0
    while runtime < duration:
        board.set_motor_duty([[1, velocity]])  
        board.set_motor_duty([[2, velocity]])  
        board.set_motor_duty([[3, -velocity]])  
        board.set_motor_duty([[4, -velocity]])
        time.sleep(1)
        runtime += 1
    board.set_motor_duty([[1, 0]])  
    board.set_motor_duty([[2, 0]])  
    board.set_motor_duty([[3, 0]])  
    board.set_motor_duty([[4, 0]])





if __name__ == '__main__':
    
    print("Drive forward for 2 seconds at 50% speed demo and also backward lololol.")
    drive_forward(100,2)
    drive_backward(100,2)
    drive_right(100,2)
    drive_left(100,2)

