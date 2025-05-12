from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

#camera
cam_mode = 0
cam_pos = [0, -500, 300]
cam_target = [0, 0, 0]
cam_up = [0, 0, 1]
cam_radius = 530
cam_angle_h = 0
cam_height = 300

#player
player_pos = [0.0, 0.0]
player_angle = 0.0
player_alive = True

#bullet 
bullets = []
enemies = []
num_enemies = 5

#grid
tile_size = 80
grid_size = 13
half_grid = (tile_size * grid_size) / 2
BOUND_MIN = -half_grid
BOUND_MAX = half_grid

#game
lives = 5
missed_shots = 0
score = 0
game_over = False

#cheat
cheat_mode = False
auto_shoot = False
cheat_rotation = 0

#camera-freeze mode
freeze_camera = False
freeze_angle = 0.0


fov_y = 120
GRID_LENGTH = 600


def random_enemy_position():
    return [random.uniform(BOUND_MIN, BOUND_MAX),random.uniform(BOUND_MIN, BOUND_MAX),15] 


for _ in range(num_enemies):
    enemies.append([*random_enemy_position(), 0.7, 1])




def restart_game():
    global player_pos, player_angle, bullets, enemies
    global lives, missed_shots, score, game_over, player_alive
    global cam_mode, cam_angle_h, cam_height
    global cheat_mode, auto_shoot, cheat_rotation
    global freeze_camera, freeze_angle

    player_pos = [0.0, 0.0]
    player_angle = 0.0
    bullets.clear()
    enemies[:] = [[*random_enemy_position(), 1.0, 1]
                  for _ in range(num_enemies)]
    lives = 5
    missed_shots = 0
    score = 0
    game_over = False
    player_alive = True

    cam_mode = 0
    cam_angle_h = 0
    cam_height = 300

    cheat_mode = False
    auto_shoot = False
    cheat_rotation = 0

    freeze_camera = False
    freeze_angle = 0.0


def draw_text(x, y, text, font=GLUT_BITMAP_HELVETICA_18):
    glColor3f(1,1,1)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0,1000,0,800)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix() 
    glLoadIdentity()
    glRasterPos2f(x,y)
    for ch in text:
        glutBitmapCharacter(font, ord(ch))
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)


def draw_walls():
    wall_height = 50.0
    base_z = -0.1

    def wall(color, verts):
        glColor3f(*color)
        glBegin(GL_QUADS)
        for v in verts:
            glVertex3f(*v)
        glEnd()

    wall((0,1,0), [(BOUND_MIN,BOUND_MIN,base_z),
                   (BOUND_MIN,BOUND_MAX,base_z),
                   (BOUND_MIN,BOUND_MAX,wall_height),
                   (BOUND_MIN,BOUND_MIN,wall_height)])
    wall((0,1,1), [(BOUND_MAX,BOUND_MIN,base_z),
                   (BOUND_MAX,BOUND_MAX,base_z),
                   (BOUND_MAX,BOUND_MAX,wall_height),
                   (BOUND_MAX,BOUND_MIN,wall_height)])
    wall((1,1,0.4), [(BOUND_MIN,BOUND_MIN,base_z),
                   (BOUND_MAX,BOUND_MIN,base_z),
                   (BOUND_MAX,BOUND_MIN,wall_height),
                   (BOUND_MIN,BOUND_MIN,wall_height)])
    wall((0,0,1), [(BOUND_MIN,BOUND_MAX,base_z),
                   (BOUND_MAX,BOUND_MAX,base_z),
                   (BOUND_MAX,BOUND_MAX,wall_height),
                   (BOUND_MIN,BOUND_MAX,wall_height)])


def draw_player():
    glPushMatrix()
    glTranslatef(player_pos[0], player_pos[1], 0)
    if player_alive: glRotatef(player_angle,0,0,1)
    else: glRotatef(90,0,1,0)

    def cube(color, pos, scale):
        glPushMatrix()
        glColor3f(*color)
        glTranslatef(*pos)
        glScalef(*scale)
        glutSolidCube(20)
        glPopMatrix()



    def cylinder(color,pos,axis):
        glPushMatrix()
        glColor3f(*color)
        glTranslatef(*pos)
        glRotatef(*axis)
        gluCylinder(gluNewQuadric(),5,5,20,20,20)
        glPopMatrix()

    cylinder((0,0,1),(0,-15,25),(0,0,0,1))
    cylinder((0,0,1),(0,15,25),(0,0,0,1))
    cube((0.5,0.7,0.4),(0,0,65),(1,1.5,2))

    glPushMatrix(); glColor3f(0,0,0) 
    glTranslatef(0,0,95)
    glutSolidSphere(10,20,25) 
    glPopMatrix()

    cylinder((0.96,0.8,0.69),(0,-20,60),(90,0,1,0))
    cylinder((0.96,0.8,0.69),(0,20,60),(90,0,1,0))

    glPushMatrix() 
    glColor3f(0.3,0.3,0.3)
    glTranslatef(0,0,65) 
    glRotatef(90,0,1,0)
    gluCylinder(gluNewQuadric(),3,3,30,10,10); glPopMatrix()
    glPopMatrix()


def draw_enemies():
    global game_over
    if not game_over:
        for e in enemies:
            glPushMatrix()
            glTranslatef(e[0],e[1],e[2])
            glScalef(e[3],e[3],e[3])
            glColor3f(1,0,0)
            glutSolidSphere(15,20,20)
            glTranslatef(0,0,20)
            glColor3f(0,0,0)
            glutSolidSphere(10,20,20)
            glPopMatrix()


def draw_bullets():
    global game_over
    if not game_over:
        glColor3f(1,0,0)
        for b in bullets:
            glPushMatrix()
            glTranslatef(b['pos'][0], b['pos'][1], 65)
            angle = math.degrees(math.atan2(b['dir'][1], b['dir'][0]))    # Rotating the bullet to align with the gun direction
            glRotatef(angle, 0, 0, 1)
            glutSolidCube(8) 
            glPopMatrix()


def keyboard_listener(key,x,y):
    global player_pos,player_angle,cheat_mode,auto_shoot,cheat_rotation
    global player_alive,game_over,freeze_camera,freeze_angle

    if game_over and key in (b'r',b'R'):
        restart_game(); 
        glutPostRedisplay(); 
        return
    if not player_alive: 
        return

    step=10; rot=5
    nx,ny=player_pos[0],player_pos[1]

    if key==b'w' or key==b'W':
        nx+=step*math.cos(math.radians(player_angle))
        ny+=step*math.sin(math.radians(player_angle))
    elif key==b's' or key==b"S":
        nx-=step*math.cos(math.radians(player_angle))
        ny-=step*math.sin(math.radians(player_angle))
    elif key==b'a' or key==b'A': 
        player_angle+=rot
    elif key==b'd' or key==b'D': 
        player_angle-=rot
    elif key in (b'c',b'C'):
        cheat_mode=not cheat_mode
        if not cheat_mode: auto_shoot=False
    elif key in (b'v',b'V') and cheat_mode and cam_mode==1:
        freeze_camera=not freeze_camera
        if freeze_camera: freeze_angle=cheat_rotation

    if BOUND_MIN<=nx<=BOUND_MAX: 
        player_pos[0]=nx
    if BOUND_MIN<=ny<=BOUND_MAX: 
        player_pos[1]=ny
    glutPostRedisplay()


def special_key_listener(key,x,y):
    global cam_angle_h,cam_height
    if key==GLUT_KEY_LEFT: 
        cam_angle_h-=5
    elif key==GLUT_KEY_RIGHT: 
        cam_angle_h+=5
    elif key==GLUT_KEY_UP: 
        cam_height+=10
    elif key==GLUT_KEY_DOWN: 
        cam_height-=10


def mouse_listener(button,state,x,y):
    global bullets,cam_mode,auto_shoot
    if button==GLUT_LEFT_BUTTON and state==GLUT_DOWN:
        px,py=player_pos
        ang=math.radians(player_angle)
        bullets.append({'pos':[px,py],'dir':[math.cos(ang),math.sin(ang)]})
        print("Player Bullet Fired")
    elif button==GLUT_RIGHT_BUTTON and state==GLUT_DOWN:
        cam_mode=1-cam_mode
        auto_shoot=False


def animate():
    global enemies,bullets,missed_shots,lives,game_over,score
    global cheat_rotation,player_angle,player_alive
    if game_over: 
        glutPostRedisplay() 
        return
    for i,e in enumerate(enemies):
        dx, dy=player_pos[0]-e[0], player_pos[1]-e[1] #calculating distance to enemy
        dist=math.sqrt(dx*dx + dy*dy)
        if dist<20:
            lives-=1
            print(f"Remaining Player Life: {lives}")
            if lives<=0: 
                game_over=True
                player_alive=False

            enemies[i]=[*random_enemy_position(),1.0,1]
        else:
            spd=0.2
            e[0]+=dx/dist*spd 
            e[1]+=dy/dist*spd
            
        sc,dir=e[3],e[4]
        delta=0.01
        if dir==1:
            sc+=delta
            if sc>=1.5: 
                dir=-1
        else:
            sc-=delta
            if sc<=0.7: 
                dir=1
        e[3],e[4]=sc,dir
        
    new_bullet_list=[]

    for b in bullets:
        b['pos'][0]+=b['dir'][0]*15
        b['pos'][1]+=b['dir'][1]*15
        bx,by=b['pos']
        
        if not (BOUND_MIN<=bx<=BOUND_MAX and BOUND_MIN<=by<=BOUND_MAX):
            missed_shots+=1
            print(f"Bullet missed: {missed_shots}")
            if missed_shots>=10: 
                game_over=True 
                player_alive=False
            continue
        hit=False
        for j,e in enumerate(enemies):
            if math.dist([bx,by],[e[0],e[1]])<20*e[3]:

                enemies[j]=[*random_enemy_position(),1.0,1]
                score+=1 
                hit=True 
                break
        if not hit: new_bullet_list.append(b)
    bullets[:] = new_bullet_list
    
    if cheat_mode and not game_over:
        cheat_rotation=(cheat_rotation+2)%360
        player_angle=cheat_rotation
        for e in enemies:
            dx,dy=e[0]-player_pos[0],e[1]-player_pos[1]
            ang_e=math.degrees(math.atan2(dy,dx))%360
            diff=abs((ang_e-cheat_rotation+180)%360-180)
            if diff<1:
                cr=math.radians(cheat_rotation)
                bullets.append({'pos':[player_pos[0],player_pos[1]],'dir':[math.cos(cr),math.sin(cr)]})
                break
    
    glutPostRedisplay()


def setup_camera():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(fov_y,1.25,0.1,1500)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    if cam_mode==0:
        ang=math.radians(cam_angle_h)
        cam_pos[0]=player_pos[0]+cam_radius*math.cos(ang)
        cam_pos[1]=player_pos[1]+cam_radius*math.sin(ang)
        cam_pos[2]=cam_height
        cam_target[0]=player_pos[0]
        cam_target[1]=player_pos[1]
        cam_target[2]=60
    else:
        if cheat_mode:
            ang=math.radians(freeze_angle if freeze_camera else cheat_rotation)
        else:
            ang=math.radians(player_angle)
        cam_pos[0]=player_pos[0]+10*math.cos(ang)
        cam_pos[1]=player_pos[1]+10*math.sin(ang)
        cam_pos[2]=95
        cam_target[0]=player_pos[0]+50*math.cos(ang)
        cam_target[1]=player_pos[1]+50*math.sin(ang)
        cam_target[2]=80
    gluLookAt(*cam_pos,*cam_target,*cam_up)


def show_screen():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glViewport(0, 0, 1000, 800)

    setup_camera()

    #generating grid
    for x in range(grid_size):
        for y in range(grid_size):
            if (x + y) % 2 == 0:
                glColor3f(0.7, 0.5, 0.95)
            else:
                glColor3f(1.0, 1.0, 1.0)
            sx = -half_grid + x * tile_size
            sy = -half_grid + y * tile_size
            glBegin(GL_QUADS)
            glVertex3f(sx, sy, 0)
            glVertex3f(sx + tile_size, sy, 0)
            glVertex3f(sx + tile_size, sy + tile_size, 0)
            glVertex3f(sx, sy + tile_size, 0)
            glEnd()

    draw_player()
    draw_walls()
    draw_enemies()
    draw_bullets()

    # text
    if not game_over:
        draw_text(10, 710, f"Player Life remaining: {lives}")
        draw_text(10, 650, f"Game Score: {score}")
        draw_text(10, 680, f"Player Bullet Missed: {missed_shots}")
    else:
        draw_text(10, 710, f"Game is Over. Your score is {score}. ")
        draw_text(10, 680, f"Press 'R' to RESTART the Game.")


    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
    glutInitWindowSize(1000,800)
    glutInitWindowPosition(0,0)
    glutCreateWindow(b"3D Shooter Game Optimized")
    glutDisplayFunc(show_screen)
    glutKeyboardFunc(keyboard_listener)
    glutSpecialFunc(special_key_listener)
    glutMouseFunc(mouse_listener)
    glutIdleFunc(animate)
    glEnable(GL_DEPTH_TEST)
    glutMainLoop()

if __name__ == "__main__":
    main()