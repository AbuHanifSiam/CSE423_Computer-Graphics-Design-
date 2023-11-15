from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math
import random
W_Width, W_Height = 800,800

ballx = bally = 800
speed = 1
ball_size = 2
create_new = False
background = "n"
rain_direction = 0
    
def buildHouse():
    glLineWidth(5)
    glBegin(GL_LINES)
    
    
    glColor3f(1.0, 1.0, 0.0)#1st right line
    glVertex2d(0,200)#1st point
    glVertex2d(200,50)#2nd left point
    
    glColor3f(1.0, 1.0, 0.0)#2nd left line
    glVertex2d(0,200)
    glVertex2d(-200,50)
    
    glColor3f(1.0, 1.0, 0.0)#3rd hori line
    glVertex2d(-200,50)
    glVertex2d(200,50)
#roof done

    glColor3f(1.0, 1.0, 0.0)#left wall
    glVertex2d(-200,50)
    glVertex2d(-200,-100)
    
    glColor3f(1.0, 1.0, 0.0)#right wall
    glVertex2d(200,50)
    glVertex2d(200,-100)
    
    glColor3f(1.0, 1.0, 0.0)#ground hori line
    glVertex2d(-200,-100)
    glVertex2d(200,-100)
#box done

    glColor3f(0.0, 1.0, 1.0)
    glVertex2d(-150,0)
    glVertex2d(-150,-100)
    
    glColor3f(0.0, 1.0, 1.0)
    glVertex2d(-100,0)
    glVertex2d(-100,-100)
    
    glColor3f(0.0, 1.0, 1.0)#3rd hori line
    glVertex2d(-150,0)
    glVertex2d(-100,0)
#door done

    glColor3f(0.0, 1.0, 1.0)#3rd hori line
    glVertex2d(150,0)
    glVertex2d(100,0)
    
    glColor3f(0.0, 1.0, 1.0)#3rd hori line
    glVertex2d(150,-50)
    glVertex2d(100,-50)
    
    glColor3f(0.0, 1.0, 1.0)#3rd hori line
    glVertex2d(150,0)
    glVertex2d(150,-50)

    glColor3f(0.0, 1.0, 1.0)#3rd hori line
    glVertex2d(100,0)
    glVertex2d(100,-50)    
    glEnd()
#window done
#house done


#Raindrop settings
num_raindrops = 200
raindrops = []

for i in range(num_raindrops):
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    speed = random.uniform(1, 5)
    raindrops.append([x, y, speed])

def draw_raindrops():
    glLineWidth(1)
    glBegin(GL_LINES)
    for drop in raindrops:
        x, y, speed = drop
        if background =="n":
            glColor3f(1.0, 1.0, 1.0)
        if background =="d":
            glColor3f(0.0, 0.0, 0.0)
        glVertex2f(x, y)
        glVertex2f(x+rain_direction, y + 10+rain_direction)  # Length of the raindrop
    glEnd()

def move_raindrops():
    for drop in raindrops:
        x, y, speed = drop
        drop[0] = drop[0]-rain_direction
        drop[1] -= speed
        if y < -400:
            drop[1] = 400
            drop[0] = random.randint(-400,W_Width) 
def animate():
    #//codes for any changes in Models, Camera
    glutPostRedisplay()
    global ballx, bally,speed
    ballx=(ballx+speed)%180
    bally=(bally+speed)%180       

def keyboardListener(key, x, y):
#    
    global background
    if key==b'n':
        background = "n"
        print("night")
    if key==b'd':
        background = "d"
        print("day")    

def specialKeyListener(key, x, y):
    global rain_direction
    if key == GLUT_KEY_LEFT:
        rain_direction += 5  # Move raindrops to the left
        print("left")
    elif key == GLUT_KEY_RIGHT:
        rain_direction -= 5  # Move raindrops to the right
        print("right")
    
          
def display():
    #//clear the display
    global background
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    if background == "d":
        glClearColor(1.0,1.0,1.0,1.0);	#//color black
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    if background == "n":
        glClearColor(0.0,0.0,0.0,0.0);	#//color white
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
    #//load the correct matrix -- MODEL-VIEW matrix
    glMatrixMode(GL_MODELVIEW)
    #//initialize the matrix
    glLoadIdentity()
    #//now give three info
    #//1. where is the camera (viewer)?
    #//2. where is the camera looking?
    #//3. Which direction is the camera's UP direction?
    gluLookAt(0,0,300,	0,0,0,	0,1,0)
    glMatrixMode(GL_MODELVIEW)
    
    buildHouse()
    #drawRaindrops()
    draw_raindrops()
    move_raindrops()
    glutSwapBuffers()
    
    
def init():
    #//clear the screen
    glClearColor(0,0,0,0)
    #//load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    #//initialize the matrix
    glLoadIdentity()
    #//give PERSPECTIVE parameters
    gluPerspective(104,	1,	1,	1000.0)
    # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.
    #//near distance
    #//far distance
    
glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) #	//Depth, Double buffer, RGB color

# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"OpenGL Coding Practice")
init()

glutKeyboardFunc(keyboardListener)
glutDisplayFunc(display)	#display callback function

glutIdleFunc(animate)	#what you want to do in the idle time (when no drawing is occuring)
glutSpecialFunc(specialKeyListener)
glutMainLoop()		#The main loop of OpenGL