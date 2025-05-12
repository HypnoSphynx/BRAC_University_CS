from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

# Grid settings
tile_size = 80
grid_size = 13
half_grid = (tile_size * grid_size) / 2
BOUND_MIN = -half_grid
BOUND_MAX = half_grid

class Player:
    def __init__(self):
        self.pos = [0.0, 0.0]
        self.angle = 0.0
        self.alive = True
        self.lives = 5
        self.missed_shots = 0
        self.score = 0
    
    def move(self, direction, step_size=10):
        nx, ny = self.pos[0], self.pos[1]
        if direction == 'forward':
            nx += step_size * math.cos(math.radians(self.angle))
            ny += step_size * math.sin(math.radians(self.angle))
        elif direction == 'backward':
            nx -= step_size * math.cos(math.radians(self.angle))
            ny -= step_size * math.sin(math.radians(self.angle))
        
        # Boundary check
        if BOUND_MIN <= nx <= BOUND_MAX:
            self.pos[0] = nx
        if BOUND_MIN <= ny <= BOUND_MAX:
            self.pos[1] = ny
    
    def rotate(self, amount):
        self.angle += amount
    
    def fire_bullet(self):
        ang = math.radians(self.angle)
        return {'pos': [self.pos[0], self.pos[1]], 
                'dir': [math.cos(ang), math.sin(ang)]}
    
    def take_damage(self):
        self.lives -= 1
        print(f"Remaining Player Life: {self.lives}")
        return self.lives <= 0
    
    def miss_shot(self):
        self.missed_shots += 1
        print(f"Bullet missed: {self.missed_shots}")
        return self.missed_shots >= 10
    
    def add_score(self, points=1):
        self.score += points
    
    def draw(self):
        glPushMatrix()
        glTranslatef(self.pos[0], self.pos[1], 0)
        if self.alive:
            glRotatef(self.angle, 0, 0, 1)
        else:
            glRotatef(90, 0, 1, 0)

        def cube(color, pos, scale):
            glPushMatrix()
            glColor3f(*color)
            glTranslatef(*pos)
            glScalef(*scale)
            glutSolidCube(20)
            glPopMatrix()

        cube((0, 0, 1), (0, -15, 30), (1, 1, 2.5))
        cube((0, 0, 1), (0, 15, 30), (1, 1, 2.5))
        cube((0.5, 0.7, 0.4), (0, 0, 60), (1, 1.5, 2))

        glPushMatrix()
        glColor3f(0, 0, 0)
        glTranslatef(0, 0, 95)
        glutSolidSphere(10, 20, 20)
        glPopMatrix()

        def cylinder(color, pos):
            glPushMatrix()
            glColor3f(*color)
            glTranslatef(*pos)
            glRotatef(90, 0, 1, 0)
            gluCylinder(gluNewQuadric(), 5, 5, 20, 20, 20)
            glPopMatrix()

        cylinder((0.96, 0.8, 0.69), (0, -20, 65))
        cylinder((0.96, 0.8, 0.69), (0, 20, 65))

        glPushMatrix()
        glColor3f(0.3, 0.3, 0.3)
        glTranslatef(0, 0, 65)
        glRotatef(90, 0, 1, 0)
        gluCylinder(gluNewQuadric(), 3, 3, 30, 10, 10)
        glPopMatrix()
        
        glPopMatrix()


class Enemy:
    def __init__(self):
        self.x = random.uniform(BOUND_MIN, BOUND_MAX)
        self.y = random.uniform(BOUND_MIN, BOUND_MAX)
        self.z = 15
        self.scale = 1.0
        self.scale_dir = 1  # 1 for increasing, -1 for decreasing
    
    @property
    def pos(self):
        return [self.x, self.y, self.z]
    
    def update(self, player_pos):
        # Move towards player
        dx, dy = player_pos[0] - self.x, player_pos[1] - self.y
        dist = math.hypot(dx, dy)
        
        if dist > 0:  # Avoid division by zero
            spd = 0.2
            self.x += dx / dist * spd
            self.y += dy / dist * spd
        
        # Pulsating animation
        delta = 0.01
        if self.scale_dir == 1:
            self.scale += delta
            if self.scale >= 1.5:
                self.scale_dir = -1
        else:
            self.scale -= delta
            if self.scale <= 0.7:
                self.scale_dir = 1
        
        # Check if enemy hit the player
        return dist < 20
    
    def check_bullet_hit(self, bullet_pos):
        bx, by = bullet_pos
        dist = math.dist([bx, by], [self.x, self.y])
        return dist < 20 * self.scale
    
    def draw(self):
        glPushMatrix()
        glTranslatef(self.x, self.y, self.z)
        glScalef(self.scale, self.scale, self.scale)
        glColor3f(1, 0, 0)
        glutSolidSphere(15, 20, 20)
        glTranslatef(0, 0, 20)
        glColor3f(0, 0, 0)
        glutSolidSphere(10, 20, 20)
        glPopMatrix()


class Game:
    def __init__(self):
        # Game state
        self.game_over = False
        
        # Player and enemy setup
        self.player = Player()
        self.enemies = [Enemy() for _ in range(5)]
        self.bullets = []
        
        # Camera settings
        self.cam_mode = 0
        self.cam_pos = [0, -500, 300]
        self.cam_target = [0, 0, 0]
        self.cam_up = [0, 0, 1]
        self.cam_radius = 530
        self.cam_angle_h = 0
        self.cam_height = 300
        
        # Cheat mode
        self.cheat_mode = False
        self.auto_shoot = False
        self.cheat_rotation = 0
        
        # Camera freeze toggle
        self.freeze_camera = False
        self.freeze_angle = 0.0
        
        # Other constants
        self.fov_y = 120
    
    def restart(self):
        self.__init__()
    
    def update(self):
        if self.game_over:
            return
        
        # Update enemies
        for i, enemy in enumerate(self.enemies):
            if enemy.update(self.player.pos):
                # Enemy hit player
                if self.player.take_damage():
                    self.game_over = True
                    self.player.alive = False
                # Respawn enemy
                self.enemies[i] = Enemy()
        
        # Update bullets
        new_bullet_list = []
        for b in self.bullets:
            b['pos'][0] += b['dir'][0] * 15
            b['pos'][1] += b['dir'][1] * 15
            bx, by = b['pos']
            
            # Check if bullet left the map
            if not (BOUND_MIN <= bx <= BOUND_MAX and BOUND_MIN <= by <= BOUND_MAX):
                if self.player.miss_shot():
                    self.game_over = True
                    self.player.alive = False
                continue
            
            # Check for enemy hits
            hit = False
            for j, enemy in enumerate(self.enemies):
                if enemy.check_bullet_hit(b['pos']):
                    self.enemies[j] = Enemy()
                    self.player.add_score()
                    hit = True
                    break
            
            if not hit:
                new_bullet_list.append(b)
        
        self.bullets = new_bullet_list
        
        # Handle cheat mode auto-shooting
        if self.cheat_mode and not self.game_over:
            self.cheat_rotation = (self.cheat_rotation + 2) % 360
            self.player.angle = self.cheat_rotation
            
            for enemy in self.enemies:
                dx, dy = enemy.x - self.player.pos[0], enemy.y - self.player.pos[1]
                ang_e = math.degrees(math.atan2(dy, dx)) % 360
                diff = abs((ang_e - self.cheat_rotation + 180) % 360 - 180)
                if diff < 1:
                    cr = math.radians(self.cheat_rotation)
                    self.bullets.append({'pos': [self.player.pos[0], self.player.pos[1]], 
                                        'dir': [math.cos(cr), math.sin(cr)]})
                    break
    
    def draw(self):
        # Setup camera
        self.setup_camera()
        
        # Draw floor
        self.draw_floor()
        
        # Draw game objects
        self.player.draw()
        self.draw_walls()
        
        for enemy in self.enemies:
            enemy.draw()
            
        self.draw_bullets()
        
        # Draw HUD
        self.draw_hud()
    
    def setup_camera(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(self.fov_y, 1.25, 0.1, 1500)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
        if self.cam_mode == 0:
            ang = math.radians(self.cam_angle_h)
            self.cam_pos[0] = self.player.pos[0] + self.cam_radius * math.cos(ang)
            self.cam_pos[1] = self.player.pos[1] + self.cam_radius * math.sin(ang)
            self.cam_pos[2] = self.cam_height
            self.cam_target[0] = self.player.pos[0]
            self.cam_target[1] = self.player.pos[1]
            self.cam_target[2] = 60
        else:
            if self.cheat_mode:
                ang = math.radians(self.freeze_angle if self.freeze_camera else self.cheat_rotation)
            else:
                ang = math.radians(self.player.angle)
            
            self.cam_pos[0] = self.player.pos[0] + 10 * math.cos(ang)
            self.cam_pos[1] = self.player.pos[1] + 10 * math.sin(ang)
            self.cam_pos[2] = 95
            self.cam_target[0] = self.player.pos[0] + 50 * math.cos(ang)
            self.cam_target[1] = self.player.pos[1] + 50 * math.sin(ang)
            self.cam_target[2] = 95
        
        gluLookAt(*self.cam_pos, *self.cam_target, *self.cam_up)
    
    def draw_floor(self):
        for x in range(grid_size):
            for y in range(grid_size):
                if (x + y) % 2 == 0:
                    glColor3f(0.7, 0.5, 0.95)  # Lavender
                else:
                    glColor3f(1.0, 1.0, 1.0)  # White
                
                sx = -half_grid + x * tile_size
                sy = -half_grid + y * tile_size
                glBegin(GL_QUADS)
                glVertex3f(sx, sy, 0)
                glVertex3f(sx + tile_size, sy, 0)
                glVertex3f(sx + tile_size, sy + tile_size, 0)
                glVertex3f(sx, sy + tile_size, 0)
                glEnd()
    
    def draw_walls(self):
        wall_height = 50.0
        base_z = -0.1

        def wall(color, verts):
            glColor3f(*color)
            glBegin(GL_QUADS)
            for v in verts:
                glVertex3f(*v)
            glEnd()

        wall((0, 1, 0), [(BOUND_MIN, BOUND_MIN, base_z),
                      (BOUND_MIN, BOUND_MAX, base_z),
                      (BOUND_MIN, BOUND_MAX, wall_height),
                      (BOUND_MIN, BOUND_MIN, wall_height)])
        wall((0, 1, 1), [(BOUND_MAX, BOUND_MIN, base_z),
                      (BOUND_MAX, BOUND_MAX, base_z),
                      (BOUND_MAX, BOUND_MAX, wall_height),
                      (BOUND_MAX, BOUND_MIN, wall_height)])
        wall((1, 1, 0.4), [(BOUND_MIN, BOUND_MIN, base_z),
                       (BOUND_MAX, BOUND_MIN, base_z),
                       (BOUND_MAX, BOUND_MIN, wall_height),
                       (BOUND_MIN, BOUND_MIN, wall_height)])
        wall((0, 0, 1), [(BOUND_MIN, BOUND_MAX, base_z),
                      (BOUND_MAX, BOUND_MAX, base_z),
                      (BOUND_MAX, BOUND_MAX, wall_height),
                      (BOUND_MIN, BOUND_MAX, wall_height)])
    
    def draw_bullets(self):
        glColor3f(1, 0, 0)
        for b in self.bullets:
            glPushMatrix()
            glTranslatef(b['pos'][0], b['pos'][1], 65)
            # Rotate the cube to align with the bullet direction
            angle = math.degrees(math.atan2(b['dir'][1], b['dir'][0]))
            glRotatef(angle, 0, 0, 1)
            # Draw a cube instead of a sphere
            glutSolidCube(8)  # Size 8 cube
            glPopMatrix()
    
    def draw_hud(self):
        if not self.game_over:
            draw_text(10, 710, f"Player Life remaining: {self.player.lives}")
            draw_text(10, 650, f"Game Score: {self.player.score}")
            draw_text(10, 680, f"Player Bullet Missed: {self.player.missed_shots}")
        else:
            draw_text(10, 710, f"Game is Over. Your score is {self.player.score}.")
            draw_text(10, 680, f"Press 'R' to RESTART the Game.")
    
    def handle_key(self, key):
        if self.game_over and key in (b'r', b'R'):
            self.restart()
            return True
        
        if not self.player.alive:
            return False
        
        if key == b'w' or key == b'W':
            self.player.move('forward')
        elif key == b's' or key == b'S':
            self.player.move('backward')
        elif key == b'a' or key == b'A':
            self.player.rotate(5)
        elif key == b'd' or key == b'D':
            self.player.rotate(-5)
        elif key in (b'c', b'C'):
            self.cheat_mode = not self.cheat_mode
            if not self.cheat_mode:
                self.auto_shoot = False
        elif key in (b'v', b'V') and self.cheat_mode and self.cam_mode == 1:
            self.freeze_camera = not self.freeze_camera
            if self.freeze_camera:
                self.freeze_angle = self.cheat_rotation
        
        return True
    
    def handle_special_key(self, key):
        if key == GLUT_KEY_LEFT:
            self.cam_angle_h -= 5
        elif key == GLUT_KEY_RIGHT:
            self.cam_angle_h += 5
        elif key == GLUT_KEY_UP:
            self.cam_height += 10
        elif key == GLUT_KEY_DOWN:
            self.cam_height -= 10
    
    def handle_mouse(self, button, state):
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            self.bullets.append(self.player.fire_bullet())
            print("Player Bullet Fired")
        elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
            self.cam_mode = 1 - self.cam_mode
            self.auto_shoot = False


# Draw 2D text (kept as a global function)
def draw_text(x, y, text, font=GLUT.BITMAP_HELVETICA_18):
    glColor3f(1, 1, 1)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, 1000, 0, 800)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix() 
    glLoadIdentity()
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(font, ord(ch))
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)


# Global game instance
game = Game()


# GLUT callback functions
def show_screen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glViewport(0, 0, 1000, 800)
    game.draw()
    glutSwapBuffers()


def keyboard_listener(key, x, y):
    if game.handle_key(key):
        glutPostRedisplay()


def special_key_listener(key, x, y):
    game.handle_special_key(key)
    glutPostRedisplay()


def mouse_listener(button, state, x, y):
    game.handle_mouse(button, state)
    glutPostRedisplay()


def animate():
    game.update()
    glutPostRedisplay()


# Main function
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1000, 800)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"3D Shooter Game with Classes")
    glutDisplayFunc(show_screen)
    glutKeyboardFunc(keyboard_listener)
    glutSpecialFunc(special_key_listener)
    glutMouseFunc(mouse_listener)
    glutIdleFunc(animate)
    glEnable(GL_DEPTH_TEST)
    glutMainLoop()


if __name__ == "__main__":
    main()