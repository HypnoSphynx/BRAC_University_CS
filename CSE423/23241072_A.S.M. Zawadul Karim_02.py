from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time

#Window size
width, height = 500, 500
 
catcher_width = 100
catcher_height = 20
catcher_y = 30
catcher_x = width // 2

 
ball_size = 20
ball_x = random.randint(50, width - 50)
ball_y = height
ball_color = (random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))


score = 0
ball_speed = 100
paused = False
game_over = False
last_time = time.time()



def draw_point(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()



def find_zone(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    if abs(dx) >= abs(dy):
        if dx >= 0 and dy >= 0:
            return 0
        elif dx < 0 and dy >= 0:
            return 3
        elif dx < 0 and dy < 0:
            return 4
        else:
            return 7
    else:
        if dx >= 0 and dy >= 0:
            return 1
        elif dx < 0 and dy >= 0:
            return 2
        elif dx < 0 and dy < 0:
            return 5
        else:
            return 6

def convert_to_zone_0(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return y, -x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return -y, x
    elif zone == 7:
        return x, -y

def convert_from_zone_0(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return -y, x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return y, -x
    elif zone == 7:
        return x, -y

def draw_line(x1, y1, x2, y2):
    zone = find_zone(x1, y1, x2, y2)
    x1_, y1_ = convert_to_zone_0(x1, y1, zone)
    x2_, y2_ = convert_to_zone_0(x2, y2, zone)

    dx = x2_ - x1_
    dy = y2_ - y1_
    d = 2 * dy - dx
    incE = 2 * dy
    incNE = 2 * (dy - dx)
    x, y = x1_, y1_

    while x <= x2_:
        px, py = convert_from_zone_0(x, y, zone)
        draw_point(px, py)
        if d > 0:
            y += 1
            d += incNE
        else:
            d += incE
        x += 1

def draw_ball():
    half = ball_size // 2
    glColor3f(*ball_color)
    draw_line(ball_x, ball_y + half, ball_x + half, ball_y)
    draw_line(ball_x + half, ball_y, ball_x, ball_y - half)
    draw_line(ball_x, ball_y - half, ball_x - half, ball_y)
    draw_line(ball_x - half, ball_y, ball_x, ball_y + half)

def draw_catcher():
    top_width = catcher_width
    bottom_width = catcher_width * 0.6
    height_offset = catcher_height

    x1 = catcher_x - top_width // 2
    x2 = catcher_x + top_width // 2
    x3 = catcher_x - bottom_width // 2
    x4 = catcher_x + bottom_width // 2
    y1 = catcher_y + height_offset
    y2 = catcher_y

    if game_over:
        glColor3f(1.0, 0.0, 0.0)
    else:
        glColor3f(1.0, 1.0, 1.0)

    draw_line(int(x1), int(y1), int(x2), int(y1))
    draw_line(int(x2), int(y1), int(x4), int(y2))
    draw_line(int(x4), int(y2), int(x3), int(y2))
    draw_line(int(x3), int(y2), int(x1), int(y1))

def draw_buttons():
    glColor3f(0.0, 1.0, 1.0)
    draw_line(60, 440, 40, 460)
    draw_line(40, 460, 60, 480)
    draw_line(43, 460, 80, 460)

    glColor3f(1.0, 1.0, 0.0)
    if paused:

        draw_line(240, 440, 260, 460)
        draw_line(260, 460, 240, 480)
        draw_line(240, 480, 240, 440)
    else:
        draw_line(240, 440, 240, 480)
        draw_line(260, 440, 260, 480)

    glColor3f(1.0, 0.0, 0.0)
    draw_line(420, 440, 460, 480)
    draw_line(420, 480, 460, 440)

def check_collision():
    catcher_box = (catcher_x - catcher_width // 2, catcher_y, catcher_width, catcher_height)
    ball_box = (ball_x - 10, ball_y - 10, 20, 20)
    return (
        catcher_box[0] < ball_box[0] + ball_box[2] and
        catcher_box[0] + catcher_box[2] > ball_box[0] and
        catcher_box[1] < ball_box[1] + ball_box[3] and
        catcher_box[1] + catcher_box[3] > ball_box[1]
    )

def reset_ball():
    global ball_x, ball_y, ball_color
    ball_x = random.randint(50, width - 50)
    ball_y = height
    ball_color = (random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))

def end_game():
    global game_over
    game_over = True
    print(f"Game Over! Score: {score}")

def restart_game():
    global score, ball_speed, game_over, paused
    print("Starting Over!")
    score = 0
    ball_speed = 100
    paused = False
    game_over = False
    reset_ball()


def draw():
    global ball_y, score, ball_speed, last_time
    glClear(GL_COLOR_BUFFER_BIT)
    draw_buttons()
    draw_catcher()
    if not game_over:
        draw_ball()

    now = time.time()
    dt = now - last_time
    if not paused and not game_over:
        ball_y -= ball_speed * dt
        if check_collision():
            score += 1
            print(f"Score: {score}")
            ball_speed+=10
            reset_ball()
        elif ball_y < 0:
            end_game()
    last_time = now

    glColor3f(1.0, 1.0, 0.0)
    glutSwapBuffers()


def special_keys(key, x, y):
    global catcher_x
    if paused or game_over:
        return
    if key == GLUT_KEY_LEFT and catcher_x - catcher_width // 2 > 10:
        catcher_x -= 25
    elif key == GLUT_KEY_RIGHT and catcher_x + catcher_width // 2 < width - 10:
        catcher_x += 25

def mouse(button, state, x, y):
    global paused
    y = height - y
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if 40 < x < 60 and 440 < y < 480:
            restart_game()
        elif 240 < x < 260 and 440 < y < 480:
            paused = not paused
        elif 420 < x < 460 and 440 < y < 480:
            print("Goodbye! Score:", score)
            glutLeaveMainLoop()

def timer(v):
    glutPostRedisplay()
    glutTimerFunc(16, timer, 0)


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(width, height)
glutCreateWindow(b"Diamond Catcher")
glutDisplayFunc(draw)
glutSpecialFunc(special_keys)
glutMouseFunc(mouse)
glutTimerFunc(0, timer, 0)
glClearColor(0.0, 0.0, 0.0, 1.0)
gluOrtho2D(0, width, 0, height)
glPointSize(2)
glutMainLoop()


