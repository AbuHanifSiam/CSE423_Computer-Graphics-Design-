from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time

ballx = bally = 100
ball_size = 5
speed = 1
freeze = False
blink = False
time = 0
def draw_points(x, y, color= None):
    global blink,time,speed
    glPointSize(ball_size) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    speed = 0.1
    if blink == True:
        if time < 2000:
            #print(time)
            r = random.uniform(0,1)
            g = random.uniform(0,1)
            b = random.uniform(0,1)
            glColor3f(r,g,b)
            glVertex2f(x,y) #jekhane show korbe pixel
        elif time < 4000:
            #print(time)
            glColor3f(0.0,0.0,0.0)
            glVertex2f(x,y)
        else:
            time = 0
        time += 1
    else:
        r = random.uniform(0,1)
        g = random.uniform(0,1)
        b = random.uniform(0,1)
        glColor3f(r,g,b)
        glVertex2f(x,y)
    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    #glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    global freeze, blink, speed
    #point = []
    #if blink == False:
        #print("blink=false")
    speed = 0.1
    for i in range(10):
        x = random.randint(100,400)
        y = random.randint(100,400)
        #if freeze == False:
        draw_points(x,y)
            #point.append([x,y])
    #if blink == True:
        #print("blonk = True")
        #for i in range(len(point)):
            #x,y = point[i]
            #print(x,y)
            #draw_points(x,y, True)
        #blink = False
#        
    #if blink == True:
        #time.sleep(1)
        #blink = False
    #if blink == False:
        glutSwapBuffers()
#        
        


#subtask1, random point by clicking right button of mouse

def mouseListener(button, state, x, y):	
    #global ballx, bally, create_new
    global blink
    if button==GLUT_LEFT_BUTTON and state == GLUT_DOWN:

        blink = True
        print("blink")
    
    glutPostRedisplay()
        #print(x,y)
        #draw_points(x,y,"black")
            #ballx, bally = c_X, c_y
        
    #if button==GLUT_RIGHT_BUTTON:
        #if state == GLUT_DOWN: 	
            #create_new = convert_coordinate(x,y)
    # case GLUT_MIDDLE_BUTTON:
    #     //........

    #glutPostRedisplay()
    
    
#task 2, freeze and unfreeze
def keyboardListener(key, x, y):
    
    global freeze
    if key==b' ':
        freeze = not freeze

    glutPostRedisplay()


    

def specialKeyListener(key, x, y):
    global speed
    if key==GLUT_KEY_UP:
        
        speed += 1
    if key == GLUT_KEY_DOWN:
        speed -= 1
    
    glutPostRedisplay()


def animate():
    #//codes for any changes in Models, Camera
    
    if not freeze:
        glutPostRedisplay()
        #time.sleep(1.0/60)
        #global ballx, bally, speed
        #ballx=(ballx+speed)%50
        #bally=(bally+speed)%50

    #glutTimerFunc(10, animate, 0)
    
    
    
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"LAB01_TASK2") #window name
glutDisplayFunc(showScreen)
glutIdleFunc(animate)

glutKeyboardFunc(keyboardListener)#
glutMouseFunc(mouseListener)
#glutSpecialFunc(specialKeyListener)


glutMainLoop()

