import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Global variables
rain_speed = 1
wind_speed = 0
rain_offset_x = 0
raindrops = [[random.randint(0, 1000), random.randint(0, 1000)] for _ in range(400)]
background_brightness = [0.5, 0.8, 1.0, 1.0]
raincolor=[0.0, 0.0, 0.0]

def draw_point(x, y, size):
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def draw_line(x1, y1, x2, y2, width):
    glLineWidth(width)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()


def draw_triangle(x1, y1, x2, y2, x3, y3):
    glBegin(GL_TRIANGLES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()


def draw_rectangle(x1, y1, x2, y2):
    glBegin(GL_QUADS)
    glVertex2f(x1, y1)
    glVertex2f(x2, y1)
    glVertex2f(x2, y2)
    glVertex2f(x1, y2)
    glEnd()


def update_rainfall():
    global raindrops
    for i in range(len(raindrops)):
        raindrops[i][1] = (raindrops[i][1] - rain_speed) % 1000
        raindrops[i][0] = (raindrops[i][0] + wind_speed) % 1000
    glutPostRedisplay()


def handle_special_keys(key, x, y):
    global rain_offset_x, wind_speed
    if rain_offset_x < 70:
        if key == GLUT_KEY_RIGHT:
            rain_offset_x += 3
            wind_speed += 1
        elif key == GLUT_KEY_LEFT:
            rain_offset_x -= 3
            wind_speed -= 1
    glutPostRedisplay()


def handle_keyboard_input(key, x, y):
    global background_brightness
    if key == b'd' and (background_brightness[0] <= 0.5 or background_brightness[1]<=0.8 or background_brightness[2]<=1.0 or background_brightness[3]<=1.0):
        if background_brightness[0]<=0.5:
            background_brightness[0] += 0.2
            raincolor[0]-=0.2
        if background_brightness[1]<=0.8:
            background_brightness[1] += 0.25
            raincolor[1]-=0.2
        if background_brightness[2]<=1.0:
            background_brightness[2] += 0.3
            raincolor[2]-=0.2
        if background_brightness[3]<=1.0:
            background_brightness[3] += 0.3
        
    elif key == b'n' and (background_brightness[0] >= 0.0 or background_brightness[1]<=0.0 or background_brightness[2]<=0.0 or background_brightness[3]<=0.0):
            background_brightness[0] -= 0.2
            background_brightness[1] -= 0.25
            background_brightness[2] -= 0.3
            background_brightness[3] -= 0.3
            if raincolor[0]<=0.5:
                raincolor[0]+=.2
            if raincolor[1]<=0.8:
                raincolor[1]+=.2
            if raincolor[2]<=1.0:
                raincolor[2]+=.2
    glutPostRedisplay()


def configure_screen():
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def draw_house():
    # roof
    glColor3f(0.9, 0.3, 0.6)
    draw_triangle(220, 450, 440, 575, 660, 450)
    # walls
    glColor3f(0.9, 0.8, 0.6)
    draw_rectangle(260, 262, 620, 450)
    # door
    glColor3f(0.2, 0.4, 0.3)
    draw_rectangle(380, 262, 480, 387)
    # windows
    glColor3f(0.4, 0.8, 0.7)
    draw_rectangle(530, 350, 590, 410) 
    draw_rectangle(290, 350, 350, 410)  
    # outlines
    glColor3f(0.0, 0.0, 0.0)
    draw_line(220, 450, 660, 450, 5)
    draw_line(220, 450, 440, 575, 5)
    draw_line(440, 575, 660, 450, 5)
    draw_line(260, 450, 260, 262, 5)
    draw_line(620, 450, 620, 262, 5)
    draw_line(260, 262, 620, 262, 5)
    draw_line(380, 262, 380, 387, 2)
    draw_line(480, 262, 480, 387, 2)
    draw_line(380, 387, 480, 387, 2)
    # window
    for x in (530, 290):
        draw_line(x, 350, x + 60, 350, 3)
        draw_line(x, 410, x + 60, 410, 3)
        draw_line(x, 380, x + 60, 380, 3)
        draw_line(x, 350, x, 410, 3)
        draw_line(x + 60, 350, x + 60, 410, 3)
        draw_line(x + 30, 350, x + 30, 410, 3)


def render_scene():
    global raindrops, rain_offset_x, background_brightness
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    configure_screen()
    glClearColor(background_brightness[0], background_brightness[1], background_brightness[2], background_brightness[3])
    # draw ground
    glColor3f(0.3, 0.7, 0.3)
    draw_rectangle(0, 0, 1000, 350)
    # draw housen
    draw_house()
    # draw rain
    glColor3f(raincolor[0], raincolor[1], raincolor[2])
    for drop in raindrops:
        draw_line(drop[0], drop[1], drop[0] + rain_offset_x, drop[1] - 20, 1.3)
    
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(1000, 1000)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"Assignment 1 Task 01")
glutDisplayFunc(render_scene)
glutIdleFunc(update_rainfall)
glutKeyboardFunc(handle_keyboard_input)
glutSpecialFunc(handle_special_keys)
glutMainLoop()


#################################TASK2##############################################

# import random
# import time
# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *


# w_width, w_height = 500, 500

# class Particle:
#     def __init__(self, x, y):
#         self.x, self.y = x, y
#         self.color = (random.random(), random.random(), random.random())
#         self.direction = [random.choice([-1, 1]) for _ in range(2)]
#         self.speed = 0.3
#         self.blink = False
#         self.blink_timer = time.time()

#     def render(self, blink):
#         if blink and (time.time() - self.blink_timer) >= 0.3:
#             if self.blink==True:
#                 self.blink=False
#             else:
#                 self.blink=True

#             self.blink_timer = time.time()
#         if self.blink==True:
#             glColor3f(0.0,0.0,0.0)
#         else:
#             glColor3f(*self.color)
#         glPointSize(5)
#         glBegin(GL_POINTS)
#         glVertex2f(self.x, self.y)
#         glEnd()
    
#     def update_position(self, stop):
#         if stop:
#             return
#         self.x += self.direction[0] * self.speed
#         self.y += self.direction[1] * self.speed
        
#         # Boundary conditions
#         if not -500 < self.x < 500:
#             self.direction[0] *= -1
#         if not -500 < self.y < 500:
#             self.direction[1] *= -1

# class ParticleScene:
#     def __init__(self):
#         self.particles = []
#         self.blink = False
#         self.stop = False

#     def get_opengl_coords(self, mx, my):
#         px = (mx / w_width) * 1000 - 500
#         py = 500 - (my / w_height) * 1000
#         return px, py
    
#     def handle_mouse_click(self, button, state, x, y):
#         if state == GLUT_DOWN:
#             if button == GLUT_LEFT_BUTTON:
#                 if self.blink==True:
#                     self.blink=False
#                 else:
#                     self.blink=True
#                 for p in self.particles:
#                     p.blink_timer = time.time()
#             elif button == GLUT_RIGHT_BUTTON:
#                 px, py = self.get_opengl_coords(x, y)
#                 self.particles.extend([Particle(px, py) for _ in range(5)])
#         glutPostRedisplay()
    
#     def process_key_inputs(self, key, x, y):
#         if key == b' ':
#             self.stop = not self.stop
            
#         glutPostRedisplay()
    
#     def handle_special_keys(self, key, x, y):
#         if key == GLUT_KEY_UP:
#             for p in self.particles:
#                 p.speed += 0.3
#         elif key == GLUT_KEY_DOWN:
#             for p in self.particles:
#                 p.speed = max(0.7, p.speed - 0.07)
#         glutPostRedisplay()

#     def render_scene(self):
#         glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#         glLoadIdentity()

#         for p in self.particles:
#             p.render(self.blink)

#         glutSwapBuffers()

#     def animate(self):
#         for p in self.particles:
#             p.update_position(self.stop)
#         glutPostRedisplay()

# def initialize_opengl():
#     glClearColor(0, 0, 0, 0)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     gluOrtho2D(-500, 500, -500, 500)
#     glMatrixMode(GL_MODELVIEW)

# scene = ParticleScene()

# glutInit()
# glutInitWindowSize(w_width, w_height)
# glutInitWindowPosition(0, 0)
# glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
# glutCreateWindow(b"Assignment 01 Task 02")
# initialize_opengl()
# glutDisplayFunc(scene.render_scene)
# glutIdleFunc(scene.animate)
# glutMouseFunc(scene.handle_mouse_click)
# glutKeyboardFunc(scene.process_key_inputs)
# glutSpecialFunc(scene.handle_special_keys)
# glutMainLoop()