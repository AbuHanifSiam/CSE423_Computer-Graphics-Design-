
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

radius = 0
xc = 250
yc = 250
arr = []
freeze = False
growth_rate = 1

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
    global radius, xc, yc, arr
    if not freeze:
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            xc = x
            yc = 500 - y
            arr.append([0, xc, yc])
            print("Create", arr)
            glutDisplayFunc(showScreen)
            glutPostRedisplay()

def keyboard(key, x, y):
    global freeze, growth_rate
    if key == b' ':
        freeze = not freeze

def speacial_keyboard(key, x, y):
    global freeze, growth_rate
    if not freeze:
        if key == GLUT_KEY_LEFT:
            print("fast")
            growth_rate += 1
        if key == GLUT_KEY_RIGHT:
            print("slow")
            growth_rate -= 1
            if growth_rate < 1:
                growth_rate = 1

def showScreen():
    global radius, xc, yc, arr, freeze
    glClearColor(0.0, 0.8, 1.0, 1.0) #set the background color to white. RGB and Alpha
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(0.0, 0.0, 0.0) #set color to black
    for i in arr:
        draw_circle(i[0], i[1], i[2])
    glutSwapBuffers()

def animate():
    global radius, xc, yc, arr, growth_rate
    for i in arr:
        if not freeze:
            i[0] = (i[0] + growth_rate)
            if i[0] == 600:
                arr.pop(0)
                print("Delete")
    time.sleep(0.009)  # Delay for second
    glutPostRedisplay()

glutInit() #initialize glut library
glutInitDisplayMode(GLUT_RGBA) #set the initial display mode with color
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0) #window position in computer display, for this code it will be top left corner

glutCreateWindow(b"Assignment 3") #create a window with a title
glutDisplayFunc(showScreen) #set the display callback for the current window
glutIdleFunc(animate) #set the global idle callback
glutMouseFunc(mouse_click) #set the mouse callback for the current window
glutKeyboardFunc(keyboard) #set the keyboard callback for the current window
glutSpecialFunc(speacial_keyboard) #set the special keyboard callback for the current window
glutMainLoop() #enter the event processing loop


