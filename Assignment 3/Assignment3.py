from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

radius = 0
xc = 250
yc = 250
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

def iterate():
    glViewport(0, 0, 500, 500) #viewport size x, y, width, height same as window size
    glMatrixMode(GL_PROJECTION) #projection matrix
    glLoadIdentity() #replace the current matrix with identity matrix and starts us a fresh because matrix transforms such as glOrtho and glRotate cumulate, basically puts us at (0, 0, 0)
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0) #multiply the current matrix with an orthographic matrix and replaces the current matrix with the result
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    
    
def mouse_click(button, state, x, y):
    global radius, xc, yc        
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        xc = x
        yc = 500 - y
        glutDisplayFunc(showScreen)
        glutPostRedisplay()
        
        
def showScreen():
    global radius, xc, yc
    glClearColor(1.0, 1.0, 1.0, 1.0) #set the background color to white. RGB and Alpha
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glLoadIdentity()
    iterate()
    glColor3f(0.0, 0.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    draw_circle(radius, xc, yc)
    glutSwapBuffers()


def animate():
    #//codes for any changes in Models, Camera
    global radius
    
    radius = (radius + 1) % 180
    time.sleep(0.01)  # Delay for 1 second
    glutPostRedisplay()
    
    


glutInit() #initialize glut library
glutInitDisplayMode(GLUT_RGBA) #set the initial display mode with color
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0) #window position in computer display, for this code it will be top left corner
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)
glutMouseFunc(mouse_click)
glutIdleFunc(animate)
glutMainLoop()

