from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random


W_Width, W_Height = 800, 600

points = [] 
point_speed = 0.1
is_frozen = False
is_blinking = False
background_color = (0.0, 0.0, 0.0)
blink_time = 500

def generate_random_point(x, y):
    color = (random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), random.uniform(0.0, 1.0))
    direction = (random.choice([-1, 1]), random.choice([-1, 1]))
    points.append((x, y, color, direction, point_speed))

def increase_point_speed():
    global point_speed
    point_speed += 0.1
    for i in range(len(points)):
        x, y, color, direction, speed = points[i]
        points[i] = (x, y, color, direction, point_speed)

def decrease_point_speed():
    global point_speed
    if point_speed > 0.1:
        point_speed -= 0.1
        for i in range(len(points)):
            x, y, color, direction, speed = points[i]
            points[i] = (x, y, color, direction, point_speed)

def blink_points():
    global blink_time
    glutPostRedisplay()
    glutTimerFunc(blink_time, blink_points, 0)

def toggle_freeze():
    global is_frozen
    is_frozen = not is_frozen
    if is_frozen:
        glutIdleFunc(None)
    else:
        glutIdleFunc(animate)

def toggle_blink():
    global is_blinking
    is_blinking = not is_blinking
    if is_blinking:
        glutIdleFunc(blink_points)
    else:
        glutIdleFunc(animate)

def move_points():
    if not is_frozen:
        for i in range(len(points)):
            x, y, color, direction, speed = points[i]
            new_x = x + direction[0] * speed
            new_y = y + direction[1] * speed

            if new_x < 0 or new_x > W_Width:
                direction = (-direction[0], direction[1])
            if new_y < 0 or new_y > W_Height:
                direction = (direction[0], -direction[1])

            points[i] = (new_x, new_y, color, direction, speed)

def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(*background_color, 0.0)

    for x, y, color, _, _ in points:
        glPointSize(5)
        glBegin(GL_POINTS)
        glColor3f(*color)
        glVertex2f(x, y)
        glEnd()

    glutSwapBuffers()

def animate():
    move_points()
    if is_frozen or is_blinking:
        glutIdleFunc(None)
    else:
        glutIdleFunc(animate)
    glutPostRedisplay()

def mouse_click(button, state, x, y):
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        generate_random_point(x, W_Height - y)
    elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        toggle_freeze()
        toggle_blink()

def keyboardListener(key, x, y):
    if key == b' ':
        toggle_freeze()
    elif key == b'w':
        increase_point_speed()
    elif key == b's':
        decrease_point_speed()

glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(100, 100)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutCreateWindow(b"Amazing Box")

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(0, W_Width, 0, W_Height)
glutDisplayFunc(draw_scene)
glutIdleFunc(animate)
glutMouseFunc(mouse_click)
glutKeyboardFunc(keyboardListener)
glutTimerFunc(blink_time, blink_points, 0)
glutMainLoop()