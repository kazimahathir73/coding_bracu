from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
import sys

WINDOW_WIDTH = 480
WINDOW_HEIGHT = 650
BUTTON_HEIGHT = 20
BUTTON_WIDTH = 60
BUTTON_SPACING = 10
TOP_MARGIN = BUTTON_HEIGHT + 2 * BUTTON_SPACING
BOWL_SPEED = 10
DIAMOND_SIZE = 20
BOWL_SIZE = 100

class AABB:
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h
    
    def collides_with(self, other):
        return (self.x < other.x + other.w and # x_min_1 < x_max_2
                self.x + self.w > other.x  and # x_max_1 > m_min_2
                self.y < other.y + other.h and # y_min_1 < y_max_2
                self.y + self.h > other.y)     # y_max_1 > y_min_2

bowl = AABB(WINDOW_WIDTH / 2, 30, BOWL_SIZE, 10)
diamond = AABB(WINDOW_WIDTH / 2, WINDOW_HEIGHT - TOP_MARGIN, DIAMOND_SIZE, DIAMOND_SIZE)
restart_button = AABB(BUTTON_SPACING + BUTTON_WIDTH / 2, WINDOW_HEIGHT - BUTTON_SPACING - BUTTON_HEIGHT / 2, BUTTON_WIDTH, BUTTON_HEIGHT)
pause_button = AABB(2 * BUTTON_SPACING + 1.5 * BUTTON_WIDTH, WINDOW_HEIGHT - BUTTON_SPACING - BUTTON_HEIGHT / 2, BUTTON_WIDTH, BUTTON_HEIGHT)
exit_button = AABB(3 * BUTTON_SPACING + 2.5 * BUTTON_WIDTH, WINDOW_HEIGHT - BUTTON_SPACING - BUTTON_HEIGHT / 2, BUTTON_WIDTH, BUTTON_HEIGHT)
diamond_falling_speed = 0.04
score = 0
score_interval = 0
game_over = False
paused = False

def draw_aabb(box):
    glBegin(GL_LINES)
    glVertex2f(box.x - box.w / 2, box.y - box.h / 2)
    glVertex2f(box.x + box.w / 2, box.y - box.h / 2)
    glVertex2f(box.x + box.w / 2, box.y - box.h / 2)
    glVertex2f(box.x + box.w / 2, box.y + box.h / 2)
    glVertex2f(box.x + box.w / 2, box.y + box.h / 2)
    glVertex2f(box.x - box.w / 2, box.y + box.h / 2)
    glVertex2f(box.x - box.w / 2, box.y + box.h / 2)
    glVertex2f(box.x - box.w / 2, box.y - box.h / 2)
    glEnd()

def draw_aabb_diamond(box):
    glBegin(GL_LINES)
    glVertex2f(box.x, box.y + box.h / 2)
    glVertex2f(box.x + box.w / 2, box.y)
    glVertex2f(box.x + box.w / 2, box.y)
    glVertex2f(box.x, box.y - box.h / 2)
    glVertex2f(box.x, box.y - box.h / 2)
    glVertex2f(box.x - box.w / 2, box.y)
    glVertex2f(box.x - box.w / 2, box.y)
    glVertex2f(box.x, box.y + box.h / 2)
    
    glEnd()

def draw_restart_button(button):
    glColor3f(0.0, 1.0, 1.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(button.x - button.w / 4, button.y)
    glVertex2f(button.x + button.w / 4, button.y + button.h / 4)
    glVertex2f(button.x + button.w / 4, button.y - button.h / 4)
    glEnd()

def draw_pause_button(button):
    glColor3f(1.0, 1.0, 0.0)
    bar_width = button.w / 8
    glBegin(GL_QUADS)
    glVertex2f(button.x - bar_width, button.y + button.h / 4)
    glVertex2f(button.x - bar_width, button.y - button.h / 4)
    glVertex2f(button.x, button.y - button.h / 4)
    glVertex2f(button.x, button.y + button.h / 4)
    glVertex2f(button.x + bar_width, button.y + button.h / 4)
    glVertex2f(button.x + bar_width, button.y - button.h / 4)
    glVertex2f(button.x + 2 * bar_width, button.y - button.h / 4)
    glVertex2f(button.x + 2 * bar_width, button.y + button.h / 4)
    glEnd()

def draw_exit_button(button):
    glColor3f(1.0, 0.0, 0.0)
    line_length = button.h / 4
    glBegin(GL_LINES)
    glVertex2f(button.x - line_length, button.y + line_length)
    glVertex2f(button.x + line_length, button.y - line_length)
    glVertex2f(button.x - line_length, button.y - line_length)
    glVertex2f(button.x + line_length, button.y + line_length)
    glEnd()

def draw_resume_button(button):
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(button.x - button.w / 6, button.y - button.h / 4)
    glVertex2f(button.x - button.w / 6, button.y + button.h / 4)
    glVertex2f(button.x + button.w / 3, button.y)
    glEnd()

def draw_buttons():
    glColor3f(0.5, 0.5, 0.5)
    draw_aabb(restart_button)
    draw_aabb(pause_button)
    draw_aabb(exit_button)
    
    draw_restart_button(restart_button)
    if not paused:
        draw_pause_button(pause_button)
    else:
        draw_resume_button(pause_button)
    draw_exit_button(exit_button)

def display():
    global game_over, paused, score
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    if not game_over:
        glColor3f(1.0, 1.0, 1.0)
        draw_aabb(bowl)
        glColor3f(1.0, 0.0, 0.0)
        draw_aabb_diamond(diamond)
    draw_buttons()
    show_score()
    if game_over:
        show_game_over()
    glutSwapBuffers()

def show_score():
    glColor3f(1.0, 1.0, 1.0)
    glWindowPos2i(10, WINDOW_HEIGHT - 50)
    score_display = f"Score: {score}"
    for char in score_display:
        glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(char))

def show_game_over():
    glColor3f(1.0, 0.0, 0.0) 
    glWindowPos2i(WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2)
    game_over_text = "GAME OVER!!!!!"
    for char in game_over_text:
        glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(char))
    glWindowPos2i(WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2 - 20)
    final_score_text = f"Final Score: {score}"
    for char in final_score_text:
        glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(char))


def respawn_diamond():
    global diamond
    diamond.x = random.randint(diamond.w // 2, WINDOW_WIDTH - diamond.w // 2)
    diamond.y = WINDOW_HEIGHT - diamond.h // 2 - TOP_MARGIN - 20

def update_diamond_speed():
    global diamond_falling_speed, score, score_interval
    if score_interval >= 3:
        diamond_falling_speed += 0.01
        score_interval = 0

def check_collision_and_update_score():
    global score, diamond, game_over, score_interval, bowl
    if not game_over:
        distance_x = abs(bowl.x - diamond.x)
        distance_y = abs(bowl.y - diamond.y)
        half_width_sum = (bowl.w / 2) + (diamond.w / 2)
        half_height_sum = (bowl.h / 2) + (diamond.h / 2)
        if distance_x < half_width_sum and distance_y < half_height_sum:
            score += 1
            score_interval += 1
            update_diamond_speed()
            respawn_diamond()
        elif diamond.y < bowl.y - bowl.h / 2:
            game_over = True

def keyboard_special(key, x, y):
    global bowl
    if key == GLUT_KEY_LEFT:
        if bowl.x - bowl.w / 2 > BOWL_SPEED:
            bowl.x -= BOWL_SPEED
    elif key == GLUT_KEY_RIGHT:
        if bowl.x + bowl.w / 2 < WINDOW_WIDTH - BOWL_SPEED:
            bowl.x += BOWL_SPEED
    glutPostRedisplay()


def mouse_click(button, state, x, y):
    global paused, game_over, score, diamond, score_interval
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        converted_y = WINDOW_HEIGHT - y

        if restart_button.x - restart_button.w / 2 <= x <= restart_button.x + restart_button.w / 2 and restart_button.y - restart_button.h / 2 <= converted_y <= restart_button.y + restart_button.h / 2:
            game_over = False
            score = 0
            score_interval = 0
            diamond_falling_speed = 0.04
            respawn_diamond()
            print("Starting over!!!")

        elif pause_button.x - pause_button.w / 2 <= x <= pause_button.x + pause_button.w / 2 and pause_button.y - pause_button.h / 2 <= converted_y <= pause_button.y + pause_button.h / 2:
            paused = not paused

        elif exit_button.x - exit_button.w / 2 <= x <= exit_button.x + exit_button.w / 2 and exit_button.y - exit_button.h / 2 <= converted_y <= exit_button.y + exit_button.h / 2:
            glutLeaveMainLoop()

    glutPostRedisplay()

def animation():
    global diamond, diamond_falling_speed, game_over, paused
    if not game_over and not paused:
        diamond.y -= diamond_falling_speed
        if diamond.y < 0: 
            game_over = True
        check_collision_and_update_score()
    glutPostRedisplay()

def initialize():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
glutCreateWindow(b"OpenGL AABB Collision Detection")
glutDisplayFunc(display)
glutIdleFunc(animation)
glutSpecialFunc(keyboard_special)
glutMouseFunc(mouse_click)
initialize()
glutMainLoop()