from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

circles = []
is_paused = False
max_radius = 800
growth_speed = 2

def circ_point(x, y, cx, cy):
    glVertex2f(x + cx, y + cy)
    glVertex2f(y + cx, x + cy)
    glVertex2f(y + cx, -x + cy)
    glVertex2f(x + cx, -y + cy)
    glVertex2f(-x + cx, -y + cy)
    glVertex2f(-y + cx, -x + cy)
    glVertex2f(-y + cx, x + cy)
    glVertex2f(-x + cx, y + cy)

def mid_circle(cx, cy, radius):
    d = 1 - radius
    x = 0
    y = radius

    circ_point(x, y, cx, cy)

    while x < y:
        if d < 0:
            d = d + 2 * x + 3
        else:
            d = d + 2 * x - 2 * y + 5
            y = y - 1
        x = x + 1
        circ_point(x, y, cx, cy)

def initialize():
    glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, WINDOW_WIDTH, 0.0, WINDOW_HEIGHT, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def show_screen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(0.447, 1.0, 0.973)
    glPointSize(2)
    glBegin(GL_POINTS)

    for x, y, radius in circles:
        mid_circle(x, y, radius)

    glEnd()

    glutSwapBuffers()

def keyboard_ordinary_keys(key):
    global is_paused
    if key == b' ':
        is_paused = not is_paused
    glutPostRedisplay()

def mouse_click(button, state, x, y):
    global circles
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        world_x, world_y = x, WINDOW_HEIGHT - y
        circles.append((world_x, world_y, 10))

def animation():
    if not is_paused:
        global circles
        for i in range(len(circles)):
            x, y, radius = circles[i]
            circles[i] = (x, y, radius + growth_speed)
    glutPostRedisplay()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Water Body Simulation")
glutDisplayFunc(show_screen)
glutIdleFunc(animation)
glutKeyboardFunc(keyboard_ordinary_keys)
glutMouseFunc(mouse_click)
glEnable(GL_DEPTH_TEST)
initialize()
glutMainLoop()
