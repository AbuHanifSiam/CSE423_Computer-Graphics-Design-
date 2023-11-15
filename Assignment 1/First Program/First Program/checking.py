from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

W_Width, W_Height = 500, 500
random_points = []

def draw_points(x, y, size, color):
    glPointSize(size)
    glBegin(GL_POINTS)
    glColor3f(*color)
    glVertex2f(x, y)
    glEnd()

def generate_random_direction():
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    return x, y

def mouseListener(button, state, x, y):
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        c_X = (x - W_Width / 2) / (W_Width / 2)
        c_Y = (W_Height / 2 - y) / (W_Height / 2)
        color = [random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)]
        direction = generate_random_direction()
        random_points.append({'x': c_X, 'y': c_Y, 'color': color, 'direction': direction})
        glutPostRedisplay()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    for point_data in random_points:
        draw_points(point_data['x'], point_data['y'], 5, point_data['color'])

    glutSwapBuffers()

def animate(value):
    for point_data in random_points:
        point_data['x'] += 0.01 * point_data['direction'][0]
        point_data['y'] += 0.01 * point_data['direction'][1]

        # Wrap points to the screen
        point_data['x'] = point_data['x'] % 2 - 1
        point_data['y'] = point_data['y'] % 2 - 1

    glutPostRedisplay()
    glutTimerFunc(10, animate, 0)

def init():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1, 1, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
wind = glutCreateWindow(b"OpenGL Coding Practice")
init()
glutDisplayFunc(display)
glutTimerFunc(10, animate, 0)
glutMouseFunc(mouseListener)
glutMainLoop()