from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

W_Width, W_Height = 800, 800
rain_drops = []

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

rain_direction = 0
background_color = (0.0, 0.0, 0.0)
rain_speed = 1.5 
house_visible = True

def draw_house():
    if house_visible:
        glColor3f(1.5, 1.5, 0.0)
        glBegin(GL_QUADS)
        glVertex2f(300, 100)
        glVertex2f(500, 100)
        glVertex2f(500, 300)
        glVertex2f(300, 300)
        glEnd()

        glColor3f(0.5, 0.35, 0.05)
        glBegin(GL_QUADS)
        glVertex2f(400, 100)
        glVertex2f(450, 100)
        glVertex2f(450, 250)
        glVertex2f(400, 250)
        glEnd()

def draw_roof():
    if house_visible:
        glColor3f(0.0, 1.0, 1.0)
        glBegin(GL_TRIANGLES)
        glVertex2f(250, 300)
        glVertex2f(550, 300)
        glVertex2f(400, 500)
        glEnd()

def draw_raindrop(x, y):
    glPointSize(3)
    glBegin(GL_POINTS)
    r, g, b = background_color
    if r > 0.5 and g > 0.5 and b > 0.5:
        glColor3f(0.0, 0.0, 0.0)
    if r < 0.5 and g < 0.5 and b < 0.5:    
        glColor3f(1.0, 1.0, 1.0)
    glVertex2f(x, y)
    glEnd()

def move_rain():
    global rain_direction
    for drop in rain_drops:
        drop.y -= rain_speed

        if drop.y < 0:
            drop.x = random.uniform(0, W_Width)
            drop.y = W_Height

    for i in range(abs(rain_direction)):
        for drop in rain_drops:
            if rain_direction < 0:
                drop.x -= 0.1
            elif rain_direction > 0:
                drop.x += 0.1
            else:
                drop.x = drop.x

def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(*background_color, 0.0)

    for drop in rain_drops:
        draw_raindrop(drop.x, drop.y)

    draw_house()
    draw_roof()

    glutSwapBuffers()

def animate():
    move_rain()
    glutPostRedisplay()

def keyboardListener(key, x, y):
    global rain_direction, background_color, house_visible

    if key == b'a' or key == b'A' or key == GLUT_KEY_LEFT:
        rain_direction -= 1
    elif key == b'd' or key == b'D' or key == GLUT_KEY_RIGHT:
        rain_direction += 1
    elif key == b'm':
        r, g, b = background_color
        r += 0.2
        g += 0.2
        b += 0.2
        background_color = (r, g, b)
    elif key == b'n':
        r, g, b = background_color
        r -= 0.2
        g -= 0.2
        b -= 0.2
        background_color = (r, g, b)
    elif key == b'v':
        house_visible = not house_visible

    glutPostRedisplay()

glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(100, 100)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutCreateWindow(b"Rainy House")
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(0, W_Width, 0, W_Height)

for i in range(1000):
    rain_drops.append(Point(x=random.uniform(0, W_Width), y=random.uniform(0, W_Height)))

glutDisplayFunc(draw_scene)
glutIdleFunc(animate)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(keyboardListener)
glutMainLoop()
