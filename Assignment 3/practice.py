from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window_height = 1000
window_width = 1000

def draw_circle(radius, xc, yc):
    glBegin(GL_POINTS)
    x = 0
    y = radius
    d = 1 - radius
    draw_points(x, y, xc, yc)
    while y > x:
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1
        draw_points(x, y, xc, yc)
    glEnd()
    
def draw_points(x, y, xc, yc):
    glVertex2f(x + xc, y + yc)
    glVertex2f(-x + xc, y + yc)
    glVertex2f(x + xc, -y + yc)
    glVertex2f(-x + xc, -y + yc)
    glVertex2f(y + xc, x + yc)
    glVertex2f(-y + xc, x + yc)
    glVertex2f(y + xc, -x + yc)
    glVertex2f(-y + xc, -x + yc)
    
def initialize():
    glViewport(0, 0, window_width, window_height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, window_width, 0.0, window_height, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
def show_screen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(2.0)
    glBegin(GL_POINTS)
    draw_circle(100, 200, 200)
    glEnd()
    
    glutSwapBuffers()
    
glutInit()
glutInitWindowSize(window_width, window_height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) #	//Depth, Double buffer, RGB color

# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"Open Coding Practice")

#glutKeyboardFunc(keyboardListener)
glutDisplayFunc(show_screen)	#display callback function

#glutIdleFunc(animate)	#what you want to do in the idle time (when no drawing is occuring)
#glutSpecialFunc(specialKeyListener)

glEnable(GL_DEPTH_TEST)
initialize()
glutMainLoop()		#The main loop of OpenGL