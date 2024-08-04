import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

W_Width, W_Height = 700, 900
box_move = 0
dim_x = 0
pause = False
diamond_list = []
collision = False
points = 0

class Diamond:

    def __init__(self):
        self.x = random.randint(20, W_Width - 20)  # Randomize within the window width
        self.y = random.randint(W_Height - 100, W_Height - 50)  # Randomize near the top of the window
        self.speed = 2  # You can adjust the speed as needed
        self.color = [random.random(), random.random(), random.random()]

    def update(self):
        self.y -= self.speed

    def draw(self):
        color = self.color
        draw_line(self.x, self.y, self.x + 10, self.y + 20, color)
        draw_line(self.x, self.y, self.x + 10, self.y -20, color)
        draw_line(self.x + 20, self.y, self.x + 10, self.y + 20, color)
        draw_line(self.x + 20, self.y, self.x + 10, self.y - 20, color)

class Box:
    def __init__(self, box_move):
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.box_move = box_move

    def draw_box(self, box_move):
        box_color = [1, 1, 1]
        glColor3f(1, 1, 1)
        draw_line(275 + box_move, 40, 425 + box_move, 40, box_color)
        draw_line(275 + box_move, 40, 290 + box_move, 10, box_color)
        draw_line(425 + box_move, 40, 410 + box_move, 10, box_color)
        draw_line(290 + box_move, 10, 410 +box_move, 10, box_color)

    def collides_with(self, other, box_move):
        return (self.x < other.x + other.w and # x_min_1 < x_max_2
                self.x + self.w > other.x  and # x_max_1 > m_min_2
                self.y < other.y + other.h and # y_min_1 < y_max_2
                self.y + self.h > other.y)     # y_max_1 > y_min_2


def draw_line(x1, y1, x2, y2, color):
    zone = findZone(x1, x2, y1, y2)
    x1, y1 = convertZone(x1, y1, zone)
    x2, y2 = convertZone(x2, y2, zone)
    glPointSize(5)
    glBegin(GL_POINTS)
    midpointLine(x1, x2, y1, y2, zone, color)
    glEnd()

def midpointLine(x1, x2, y1, y2, zone, color):
    dx = x2 - x1
    dy = y2 - y1
    d = (2*dy) - dx
    ne = 2*(dy - dx)
    e = 2*dy
    x, y = x1, y1
    while (x <= x2):
        cx, cy = originalZone(x, y, zone)
        glColor3f(color[0], color[1], color[2])
        glVertex2f(cx, cy)
        x += 1
        if d > 0:
            y += 1
            d += ne
        else:
            d += e

def findZone(x1, x2, y1, y2):
    dx, dy = x2 - x1, y2 - y1
    if abs(dx) > abs(dy):
        if dx >= 0 and dy > 0:
            return 0
        elif dx < 0 and dy >= 0:
            return 3
        elif dx < 0 and dy <= 0:
            return 4
        elif dx >= 0 and dy < 0:
            return 7
    else:
        if dx >= 0 and dy > 0:
            return 1
        elif dx < 0 and dy >= 0:
            return 2
        elif dx < 0 and dy <= 0:
            return 5
        elif dx >= 0 and dy < 0:
            return 6

def convertZone(X, Y, zone):
    x, y = X, Y
    if zone == 1:
        x, y = Y, X
    elif zone == 2:
        x, y = Y, -X
    elif zone == 3:
        x, y = -X, Y
    elif zone == 4:
        x, y = -X, -Y
    elif zone == 5:
        x, y = -Y, -X
    elif zone == 6:
        x, y = -Y, X
    elif zone == 7:
        x, y = X, -Y

    return x, y

def originalZone(X, Y, zone):
    x, y = X, Y
    if zone == 1:
        x, y = Y, X
    elif zone == 2:
        x, y = -Y, X
    elif zone == 3:
        x, y = -X, Y
    elif zone == 4:
        x, y = -X, -Y
    elif zone == 5:
        x, y = -Y, -X
    elif zone == 6:
        x, y = Y, -X
    elif zone == 7:
        x, y = X, -Y

    return x, y

def backButton():
    glPointSize(5)
    backButtoncolor = [0, 0.7, 0.7]
    draw_line(40, 850, 90, 850, backButtoncolor)
    draw_line(40, 850, 60, 870, backButtoncolor)
    draw_line(40, 850, 60, 830, backButtoncolor)

def cancleButton():
    glPointSize(5)
    draw_line(600, 870, 650, 830, [1, 0, 0])
    draw_line(600, 830, 650, 870, [1, 0, 0])

def pauseButton():
    glPointSize(5)
    pauseplaycolor = [1, 1, 0]
    draw_line(330, 830, 330, 870, pauseplaycolor)
    draw_line(360, 830, 360, 870, pauseplaycolor)

def playButton():
    glPointSize(5)
    pauseplaycolor = [1, 1, 0]
    draw_line(330, 830, 330, 870, pauseplaycolor)
    draw_line(330, 830, 360, 850, pauseplaycolor)
    draw_line(330, 870, 360, 850, pauseplaycolor)

def init():
    gluOrtho2D(0, W_Width, 0, W_Height)
    glViewport(0, 0, W_Width, W_Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, W_Width, 0, W_Height, -1, 1)
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

box = Box(box_move)

def display():
    global box_move, pause, collision, diamond_list, points
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    if pause == False:
        pauseButton()
    else:
        playButton()
    backButton()
    cancleButton()
    # box
    box.draw_box(box_move)

    # diamond
    for diamond in diamond_list:
        diamond.draw()
        if pause == False:
            diamond.update()
        if box.collides_with(diamond, box_move):
            collision = True
            points += 1
            print('Collision')
        else:
            collision = False

    glutSwapBuffers()

def mouseListener(button, state, x, y):
    global pause, diamond_list
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        y = W_Height - y
        if x >= 330 and x <= 360 and y >= 830 and y <= 870:
            if pause == False:
                pause = True
            else:
                pause = False
        elif x >= 40 and x <= 90 and y >= 830 and y <= 870:
            print('Back')
            diamond_list.clear()
        elif x >= 600 and x <= 650 and y >= 830 and y <= 870:
            print('Cancel')
            glutLeaveMainLoop()
        else:
            diamond_list.append(Diamond())
    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global box_move, W_Width
    if key == GLUT_KEY_RIGHT and box_move <= 270:
        box_move += 5
    if key == GLUT_KEY_LEFT and box_move >= -270:
        box_move -= 5
    glutPostRedisplay()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"Tower Game")
init()
glutDisplayFunc(display)
glutIdleFunc(display)
glutMouseFunc(mouseListener)
glutSpecialFunc(specialKeyListener)
glutMainLoop()