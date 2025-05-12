from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random
import time

#camera
cam_mode = 0
cam_pos = [0, -500, 300]
cam_target = [0, 0, 0]
cam_up = [0, 0, 1]
cam_radius = 530
cam_angle_h = 0
cam_height = 300

#snow_mode
snow_mode = False  
snow_flakes = []
MAX_SNOW_FLAKES = 300
SNOW_SPEED = 1.5
SNOW_FLAKE_SIZE = 1.5

rain_mode = False
snow_mode = False 

#Day&Night
day_mode = True  
sky_color_day = (0.53, 0.81, 0.98)
sky_color_night = (0.05, 0.05, 0.1)

#rain_mode
rain_mode = False
rain_drops = []  
MAX_RAIN_DROPS = 500
RAIN_SPEED = 5.0 

# coin_properties
coin_visible = False
coin_active_player = 0
coin_spawn_timer = 0
coin_spawn_interval = 5
power_up_active = False
last_coin_spawn_time = 0
coin_positions = []
coin_visible = False
coin_spawn_time = 0
COIN_DURATION = 3000  #3seconds in ms
COIN_RADIUS = 15
COIN_BONUS = 3  


# player
player1_pos = [-150.0, 0.0]
player1_angle = 0.0
player1_score = 0
player1_color = (0.2, 0.5, 0.8)

player2_pos = [150.0, 0.0]
player2_angle = 180.0
player2_score = 0
player2_color = (0.8, 0.2, 0.2)

active_player = 1 #current player

#key_states
key_states = {
    b'w': False, b'a': False, b's': False, b'd': False,  #player 1
    b'i': False, b'j': False, b'k': False, b'l': False   #player 2
}

#ball
ball_pos = [0.0, 0.0, 15.0]  
ball_velocity = [0.0, 0.0, 0.0]  
ball_possessed = 0  # 0: free 1: player1 2: player2

#field 
field_width = 600
field_height = 400
goal_width = 100
goal_depth = 30
goal_height = 50

#game_boundary
BOUND_MIN_X = -field_width // 2
BOUND_MAX_X = field_width // 2
BOUND_MIN_Y = -field_height // 2
BOUND_MAX_Y = field_height // 2

#game _state
cheat_mode = False  
game_over = False
game_time = 90
time_elapsed = 0
last_time = 0

#camera_view
fov_y = 120

possession_cooldown = 0
COOLDOWN_TIME = 20  # frames


def init_rain():
    global rain_drops
    rain_drops = []
    for _ in range(MAX_RAIN_DROPS):
        x = random.uniform(BOUND_MIN_X - 100, BOUND_MAX_X + 100)
        y = random.uniform(BOUND_MIN_Y - 100, BOUND_MAX_Y + 100)
        z = random.uniform(100, 500)  #generating at various heights
        rain_drops.append([x, y, z])

def check_player_collision():
    global player1_pos, player2_pos
    
    #distance between players
    dx = player1_pos[0] - player2_pos[0]
    dy = player1_pos[1] - player2_pos[1]
    distance = math.sqrt(dx*dx + dy*dy)
    
    
    min_distance = 40 
    
    if distance < min_distance:
        overlap = min_distance - distance
        
        #normalize direction vector
        if distance > 0:
            nx = dx / distance
            ny = dy / distance
        else:  #handle case where players are exactly on top of each other
            nx, ny = 1, 0
        
        #push players apart
        push_factor = overlap * 0.5
        player1_pos[0] += nx * push_factor
        player1_pos[1] += ny * push_factor
        player2_pos[0] -= nx * push_factor
        player2_pos[1] -= ny * push_factor
        
        #boundary checks after push
        player1_pos[0] = max(BOUND_MIN_X + 20, min(BOUND_MAX_X - 20, player1_pos[0]))
        player1_pos[1] = max(BOUND_MIN_Y + 20, min(BOUND_MAX_Y - 20, player1_pos[1]))
        player2_pos[0] = max(BOUND_MIN_X + 20, min(BOUND_MAX_X - 20, player2_pos[0]))
        player2_pos[1] = max(BOUND_MIN_Y + 20, min(BOUND_MAX_Y - 20, player2_pos[1]))

def draw_rain():
    if not rain_mode:
        return
    if day_mode:
        glColor3f(0.2, 0.4, 0.8)  
    else:
        glColor3f(0.7, 0.7, 1.0)  
        
    
    glBegin(GL_LINES)
    for drop in rain_drops:
        glVertex3f(drop[0], drop[1], drop[2])
        glVertex3f(drop[0], drop[1], drop[2] - 10)
    glEnd()

def update_rain():
    if not rain_mode:
        return
        
    for drop in rain_drops:
        #move rain downward
        drop[2] -= RAIN_SPEED
        
        #rain drop reset 
        if drop[2] < 0:
            drop[0] = random.uniform(BOUND_MIN_X - 100, BOUND_MAX_X + 100)
            drop[1] = random.uniform(BOUND_MIN_Y - 100, BOUND_MAX_Y + 100)
            drop[2] = random.uniform(300, 500)

def spawn_coins(count=1):
    global coin_positions, coin_visible, coin_spawn_time, last_coin_spawn_time
    coin_positions = []
    for _ in range(count):
        x = random.randint(BOUND_MIN_X + 50, BOUND_MAX_X - 50)
        y = random.randint(BOUND_MIN_Y + 50, BOUND_MAX_Y - 50)
        coin_positions.append([x, y, 10])
    coin_visible = True
    coin_spawn_time = int(time.time() * 1000) 
    last_coin_spawn_time = coin_spawn_time

def draw_coins():
    if not coin_visible:
        return
        
    glColor3f(1.0, 0.84, 0.0)
    for pos in coin_positions:
        glPushMatrix()
        glTranslatef(pos[0], pos[1], pos[2])
        glutSolidSphere(COIN_RADIUS, 20, 20)
        glPopMatrix()

def check_coin_collision():
    global coin_positions, coin_visible, player1_score, player2_score
    
    if not coin_visible:
        return
        
    for coin in coin_positions[:]: 
        #check collision with player 1
        dist1 = math.sqrt((player1_pos[0] - coin[0])**2 + (player1_pos[1] - coin[1])**2)
        if dist1 < COIN_RADIUS + 20:  
            player1_score += COIN_BONUS
            coin_positions.remove(coin)
            print(f"Player 1 collected a coin! +{COIN_BONUS} goals")
            
        #check collision with player 2
        dist2 = math.sqrt((player2_pos[0] - coin[0])**2 + (player2_pos[1] - coin[1])**2)
        if dist2 < COIN_RADIUS + 20:
            player2_score += COIN_BONUS
            coin_positions.remove(coin)
            print(f"Player 2 collected a coin! +{COIN_BONUS} goals")

def init_snow():
    global snow_flakes
    snow_flakes = []
    for _ in range(MAX_SNOW_FLAKES):
        x = random.uniform(BOUND_MIN_X - 200, BOUND_MAX_X + 200)
        y = random.uniform(BOUND_MIN_Y - 200, BOUND_MAX_Y + 200)
        z = random.uniform(100, 500)
        #slight horizontal movement for drifting effect
        dx = random.uniform(-0.3, 0.3)
        dy = random.uniform(-0.3, 0.3)
        snow_flakes.append([x, y, z, dx, dy])

def draw_snow():
    global snow_mode 
    if not snow_mode:
        return
    
    if day_mode:
        glColor3f(1.0, 1.0, 0.0) 
    else:
        glColor3f(1.0, 1.0, 1.0)
    glPointSize(SNOW_FLAKE_SIZE)
    glBegin(GL_POINTS)
    for flake in snow_flakes:
        glVertex3f(flake[0], flake[1], flake[2])
    glEnd()

def update_snow():
    global snow_flakes, snow_mode
    if not snow_mode:
        return
        
    for flake in snow_flakes:
        #snow falls slower than rain
        flake[0] += flake[3]  
        flake[1] += flake[4]  # y
        flake[2] -= SNOW_SPEED * random.uniform(0.5, 1.5)  # z fall
        
        #reset snowflakes that fall below ground
        if flake[2] < 0:
            flake[0] = random.uniform(BOUND_MIN_X - 200, BOUND_MAX_X + 200)
            flake[1] = random.uniform(BOUND_MIN_Y - 200, BOUND_MAX_Y + 200)
            flake[2] = random.uniform(300, 600)
            flake[3] = random.uniform(-0.3, 0.3)  
            flake[4] = random.uniform(-0.3, 0.3)  


def restart_game():
    global player1_pos, player1_angle, player2_pos, player2_angle
    global player1_score, player2_score, ball_pos, ball_velocity, ball_possessed
    global game_over, game_time, time_elapsed, active_player

    player1_pos = [-150.0, 0.0]
    player1_angle = 0.0
    player2_pos = [150.0, 0.0]
    player2_angle = 180.0
    
    player1_score = 0
    player2_score = 0
    
    ball_pos = [0.0, 0.0, 15.0]
    ball_velocity = [0.0, 0.0, 0.0]
    ball_possessed = 0
    
    game_over = False
    time_elapsed = 0
    active_player = 1


def draw_text(x, y, text, font=GLUT_BITMAP_HELVETICA_18):
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

def draw_sky():
    if day_mode:
        glClearColor(*sky_color_day, 1.0)
    else:
        glClearColor(*sky_color_night, 1.0)
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


def draw_field():
    #main field
    glColor3f(0.2, 0.7, 0.2)  #green
    glBegin(GL_QUADS)
    glVertex3f(BOUND_MIN_X, BOUND_MIN_Y, 0)
    glVertex3f(BOUND_MAX_X, BOUND_MIN_Y, 0)
    glVertex3f(BOUND_MAX_X, BOUND_MAX_Y, 0)
    glVertex3f(BOUND_MIN_X, BOUND_MAX_Y, 0)
    glEnd()
    
    #center line
    glColor3f(1.0, 1.0, 1.0)  #white
    glLineWidth(2.0)
    glBegin(GL_LINES)
    glVertex3f(0, BOUND_MIN_Y, 1)
    glVertex3f(0, BOUND_MAX_Y, 1)
    glEnd()
    
    #center circle
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_LOOP)
    for i in range(360):
        angle = math.radians(i)
        glVertex3f(50 * math.cos(angle), 50 * math.sin(angle), 1)
    glEnd()
    
    #calculate goal center position
    goal_center_y = (BOUND_MIN_Y + BOUND_MAX_Y) / 2
    
    #left goal-player 1
    glColor3f(0.3, 0.3, 0.3)
    draw_goal(BOUND_MIN_X, goal_center_y - goal_width/2, 0, -1)
    
    #right goal-player 2
    glColor3f(0.3, 0.3, 0.3)
    draw_goal(BOUND_MAX_X, goal_center_y - goal_width/2, 0, 1)
    
    #draw boundary walls with gaps for goals
    wall_height = 30
    glColor3f(1.0, 1.0, 1.0) 
    
    #left wall (split into two parts with gap for goal)
    #bottom part of left wall
    glBegin(GL_QUADS)
    glVertex3f(BOUND_MIN_X, BOUND_MIN_Y, 0)
    glVertex3f(BOUND_MIN_X, goal_center_y - goal_width/2, 0)
    glVertex3f(BOUND_MIN_X, goal_center_y - goal_width/2, wall_height)
    glVertex3f(BOUND_MIN_X, BOUND_MIN_Y, wall_height)
    glEnd()
    
    #top part of left wall
    glBegin(GL_QUADS)
    glVertex3f(BOUND_MIN_X, goal_center_y + goal_width/2, 0)
    glVertex3f(BOUND_MIN_X, BOUND_MAX_Y, 0)
    glVertex3f(BOUND_MIN_X, BOUND_MAX_Y, wall_height)
    glVertex3f(BOUND_MIN_X, goal_center_y + goal_width/2, wall_height)
    glEnd()
    
    #right wall (split into two parts with gap for goal)
    #bottom part of right wall
    glBegin(GL_QUADS)
    glVertex3f(BOUND_MAX_X, BOUND_MIN_Y, 0)
    glVertex3f(BOUND_MAX_X, goal_center_y - goal_width/2, 0)
    glVertex3f(BOUND_MAX_X, goal_center_y - goal_width/2, wall_height)
    glVertex3f(BOUND_MAX_X, BOUND_MIN_Y, wall_height)
    glEnd()
    
    #top part of right wall
    glBegin(GL_QUADS)
    glVertex3f(BOUND_MAX_X, goal_center_y + goal_width/2, 0)
    glVertex3f(BOUND_MAX_X, BOUND_MAX_Y, 0)
    glVertex3f(BOUND_MAX_X, BOUND_MAX_Y, wall_height)
    glVertex3f(BOUND_MAX_X, goal_center_y + goal_width/2, wall_height)
    glEnd()
    
    #bottom wall
    glBegin(GL_QUADS)
    glVertex3f(BOUND_MIN_X, BOUND_MIN_Y, 0)
    glVertex3f(BOUND_MAX_X, BOUND_MIN_Y, 0)
    glVertex3f(BOUND_MAX_X, BOUND_MIN_Y, wall_height)
    glVertex3f(BOUND_MIN_X, BOUND_MIN_Y, wall_height)
    glEnd()
    
    #top wall
    glBegin(GL_QUADS)
    glVertex3f(BOUND_MIN_X, BOUND_MAX_Y, 0)
    glVertex3f(BOUND_MAX_X, BOUND_MAX_Y, 0)
    glVertex3f(BOUND_MAX_X, BOUND_MAX_Y, wall_height)
    glVertex3f(BOUND_MIN_X, BOUND_MAX_Y, wall_height)
    glEnd()


def draw_goal(x, y, z, direction):
    depth = goal_depth * direction
    
    #back
    glBegin(GL_QUADS)
    glVertex3f(x + depth, y, z)
    glVertex3f(x + depth, y + goal_width, z)
    glVertex3f(x + depth, y + goal_width, z + goal_height)
    glVertex3f(x + depth, y, z + goal_height)
    glEnd()
    
    #top
    glBegin(GL_QUADS)
    glVertex3f(x, y, z + goal_height)
    glVertex3f(x, y + goal_width, z + goal_height)
    glVertex3f(x + depth, y + goal_width, z + goal_height)
    glVertex3f(x + depth, y, z + goal_height)
    glEnd()
    
    #left side
    glBegin(GL_QUADS)
    glVertex3f(x, y, z)
    glVertex3f(x + depth, y, z)
    glVertex3f(x + depth, y, z + goal_height)
    glVertex3f(x, y, z + goal_height)
    glEnd()
    
    #right side
    glBegin(GL_QUADS)
    glVertex3f(x, y + goal_width, z)
    glVertex3f(x + depth, y + goal_width, z)
    glVertex3f(x + depth, y + goal_width, z + goal_height)
    glVertex3f(x, y + goal_width, z + goal_height)
    glEnd()


def draw_player(pos, angle, color):
    glPushMatrix()
    glTranslatef(pos[0], pos[1], 0)
    glRotatef(angle, 0, 0, 1)
    
    #player body
    glColor3f(*color)
    glPushMatrix()
    glTranslatef(0, 0, 25)
    glScalef(1, 1, 2)
    glutSolidCube(20)
    glPopMatrix()
    
    #player head
    glPushMatrix()
    glColor3f(0.96, 0.8, 0.69)
    glTranslatef(0, 0, 55)
    glutSolidSphere(10, 20, 20)
    glPopMatrix()
    
    #player legs
    glColor3f(0.3, 0.3, 0.3)
    
    #left leg
    glPushMatrix()
    glTranslatef(-8, 0, 10)
    glScalef(0.5, 0.5, 1)
    glutSolidCube(20)
    glPopMatrix()
    
    #right leg
    glPushMatrix()
    glTranslatef(8, 0, 10)
    glScalef(0.5, 0.5, 1)
    glutSolidCube(20)
    glPopMatrix()
    
    glPopMatrix()


def draw_ball():
    glPushMatrix()
    glTranslatef(ball_pos[0], ball_pos[1], ball_pos[2])
    
    
    glColor3f(1.0, 1.0, 1.0)  #white base
    glutSolidSphere(10, 20, 20)
    
    
    glColor3f(0.0, 0.0, 0.0)  #black
    for i in range(6):
        glPushMatrix()
        glRotatef(60 * i, 0, 0, 1)
        glRotatef(45, 1, 0, 0)
        glTranslatef(0, 0, 8)
        glutSolidCube(5)
        glPopMatrix()
        
        glPushMatrix()
        glRotatef(60 * i, 0, 1, 0)
        glRotatef(45, 0, 0, 1)
        glTranslatef(0, 0, 8)
        glutSolidCube(5)
        glPopMatrix()
    
    glPopMatrix()


def keyboard_down(key, x, y):
    global key_states
    if key in key_states:
        key_states[key] = True
    glutPostRedisplay()

def keyboard_up(key, x, y):
    global key_states, rain_mode, day_mode, snow_mode
    global active_player, ball_possessed, game_over
    global possession_cooldown  

    if key in key_states:
        key_states[key] = False

    if game_over and key in (b'r', b'R'):
        restart_game()
        return

    if key in (b'tab', b'\t'):
        active_player = 3 - active_player


    if key == b' ':
        if ball_possessed == 1:
            kick_ball(player1_pos, player1_angle, 8.0)
            print("Player 1 kicked the ball")
    
    if key == b'o' or key == b'O':
        if ball_possessed == 2:
            kick_ball(player2_pos, player2_angle, 8.0)
            print("Player 2 kicked the ball")   

    if key == b'c' or key == b'C':
        global cheat_mode
        cheat_mode = not cheat_mode
        print(f"Cheat mode {'enabled' if cheat_mode else 'disabled'}")

    if key == b'n' or key == b'N':  #day/night mode
        day_mode = not day_mode

    if key == b'm' or key == b'M': #rain mode
        rain_mode = not rain_mode
        snow_mode = False 
        if rain_mode:
            init_rain()

    if key == b'p' or key == b'P': #snow mode
        snow_mode = not snow_mode
        rain_mode = False  
        if snow_mode:
            init_snow()

    glutPostRedisplay()

def handle_movement():
    global player1_pos, player1_angle, player2_pos, player2_angle
    
    step = 5 
    rot = 3
    original_p1_pos = player1_pos.copy()
    original_p2_pos = player2_pos.copy()
    
    #player 1 movement
    if key_states[b'w']:
        player1_pos[0] += step * math.cos(math.radians(player1_angle))
        player1_pos[1] += step * math.sin(math.radians(player1_angle))
    if key_states[b's']:
        player1_pos[0] -= step * math.cos(math.radians(player1_angle))
        player1_pos[1] -= step * math.sin(math.radians(player1_angle))
    if key_states[b'a']:
        player1_angle += rot
    if key_states[b'd']:
        player1_angle -= rot
    
    #player 2 movement
    if key_states[b'i']:
        player2_pos[0] += step * math.cos(math.radians(player2_angle))
        player2_pos[1] += step * math.sin(math.radians(player2_angle))
    if key_states[b'k']:
        player2_pos[0] -= step * math.cos(math.radians(player2_angle))
        player2_pos[1] -= step * math.sin(math.radians(player2_angle))
    if key_states[b'j']:
        player2_angle += rot
    if key_states[b'l']:
        player2_angle -= rot

    #check for collision after movement
    dx = player1_pos[0] - player2_pos[0]
    dy = player1_pos[1] - player2_pos[1]
    distance = math.sqrt(dx*dx + dy*dy)
    

    if distance < 40:
        player1_pos = original_p1_pos
        player2_pos = original_p2_pos
    
    #boundary checks
    player1_pos[0] = max(BOUND_MIN_X + 20, min(BOUND_MAX_X - 20, player1_pos[0]))
    player1_pos[1] = max(BOUND_MIN_Y + 20, min(BOUND_MAX_Y - 20, player1_pos[1]))
    player2_pos[0] = max(BOUND_MIN_X + 20, min(BOUND_MAX_X - 20, player2_pos[0]))
    player2_pos[1] = max(BOUND_MIN_Y + 20, min(BOUND_MAX_Y - 20, player2_pos[1]))


def kick_ball(player_pos, player_angle, power):
    global ball_possessed, ball_velocity, ball_pos
    print(f"Kick attempted by player with possession status: {ball_possessed}")  # Debug message

    if ball_possessed == 0:
        return 

    #calculate the direction based on player angle
    dir_x = math.cos(math.radians(player_angle))
    dir_y = math.sin(math.radians(player_angle))


    kick_power = power * 1.5 


    #set ball velocity
    ball_velocity[0] = dir_x * kick_power
    ball_velocity[1] = dir_y * kick_power
    ball_velocity[2] = kick_power * 0.5 


    ball_possessed = 0

    #move ball slightly forward to prevent immediate re-possession
    ball_pos[0] += dir_x * 20
    ball_pos[1] += dir_y * 20
    ball_pos[2] += 10  
    possession_cooldown = COOLDOWN_TIME
    print("Ball kicked!") 


def special_key_listener(key, x, y):
    global cam_angle_h, cam_height
    
    if key == GLUT_KEY_LEFT:
        cam_angle_h -= 5
    elif key == GLUT_KEY_RIGHT:
        cam_angle_h += 5
    elif key == GLUT_KEY_UP:
        cam_height += 10
    elif key == GLUT_KEY_DOWN:
        cam_height -= 10


def mouse_listener(button, state, x, y):
    global cam_mode
    
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        cam_mode = 1 - cam_mode


def animate():
    global cheat_mode, ball_possessed, player1_pos, player2_pos, player1_angle, player2_angle
    global cheat_mode, ball_possessed, player1_pos, player2_pos, player1_angle, player2_angle
    global cheat_mode
    global ball_pos, ball_velocity, ball_possessed
    global player1_pos, player2_pos, player1_score, player2_score
    global time_elapsed, game_over, last_time, rain_mode, snow_mode
    global possession_cooldown, coin_visible, coin_positions, last_coin_spawn_time

    if game_over:
        glutPostRedisplay()
        return

    handle_movement()
    check_player_collision()
    if rain_mode:
        update_rain()
    if snow_mode:
        update_snow()


    current_time = int(time.time() * 1000)  #current time in milliseconds

    if not coin_visible and current_time - last_coin_spawn_time >= coin_spawn_interval * 1000:
        spawn_coins()
        last_coin_spawn_time = current_time

    

    if current_time - last_coin_spawn_time > 15000:  #15 seconds interval
        spawn_coins()
        last_coin_spawn_time = current_time

    
    if cheat_mode:
        if ball_possessed == 1:
            dx = BOUND_MAX_X - player1_pos[0]
            dy = ((BOUND_MAX_Y + BOUND_MIN_Y) / 2) - player1_pos[1]
            angle = math.degrees(math.atan2(dy, dx))
            kick_ball(player1_pos, angle, 8.0)
            ball_possessed = 0 
        elif ball_possessed == 2:
            dx = BOUND_MIN_X - player2_pos[0]
            dy = ((BOUND_MAX_Y + BOUND_MIN_Y) / 2) - player2_pos[1]
            angle = math.degrees(math.atan2(dy, dx))
            kick_ball(player2_pos, angle, 8.0)
            ball_possessed = 0  

    check_coin_collision()

    if last_time == 0:
        last_time = current_time

    time_delta = (current_time - last_time) / 1000.0  #convert to seconds
    time_elapsed += time_delta
    last_time = current_time

    if time_elapsed >= game_time:
        game_over = True

    #update possession cooldown
    if possession_cooldown > 0:
        possession_cooldown -= 1


    if ball_possessed == 0:
        #apply velocity
        ball_pos[0] += ball_velocity[0]
        ball_pos[1] += ball_velocity[1]
        ball_pos[2] += ball_velocity[2]
        
        #apply gravity
        ball_velocity[2] -= 0.5
        
        #check for collision with players
        for player_id, (player_pos, player_angle) in enumerate([(player1_pos, player1_angle), (player2_pos, player2_angle)], 1):
            dx = ball_pos[0] - player_pos[0]
            dy = ball_pos[1] - player_pos[1]
            distance = math.sqrt(dx*dx + dy*dy)
            

            if distance < 30 and ball_pos[2] < 40: 
                #calculate reflection direction based on player's facing
                player_dir_x = math.cos(math.radians(player_angle))
                player_dir_y = math.sin(math.radians(player_angle))
                

                ball_velocity[0] = player_dir_x * 8
                ball_velocity[1] = player_dir_y * 8
                ball_velocity[2] = 3
                
                #move ball slightly away to prevent sticking
                ball_pos[0] += player_dir_x * 5
                ball_pos[1] += player_dir_y * 5
                ball_pos[2] += 5
                
                #check if we should give possession
                if possession_cooldown <= 0 and math.sqrt(ball_velocity[0]**2 + ball_velocity[1]**2) < 6:
                    ball_possessed = player_id
                    ball_velocity = [0, 0, 0]
        
        #ground collision
        if ball_pos[2] <= 10:
            ball_pos[2] = 10
            ball_velocity[2] = -ball_velocity[2] * 0.7  # Bounce with dampening
            
            #apply friction when on ground
            ball_velocity[0] *= 0.95
            ball_velocity[1] *= 0.95
            
            #stop the ball if moving very slowly
            if abs(ball_velocity[0]) < 0.1 and abs(ball_velocity[1]) < 0.1 and abs(ball_velocity[2]) < 0.1:
                ball_velocity = [0, 0, 0]
        
        #check for goals
        goal_center_y = (BOUND_MIN_Y + BOUND_MAX_Y) / 2
        
        #player 2 scores (ball enters left goal)
        if (ball_pos[0] <= BOUND_MIN_X and 
            (goal_center_y - goal_width/2) <= ball_pos[1] <= (goal_center_y + goal_width/2) and 
            ball_pos[2] < goal_height):
            player2_score += 1
            print(f"Goal for Player 2! Score: {player1_score}-{player2_score}")
            reset_after_goal()
                
        #player 1 scores (ball enters right goal)
        elif (ball_pos[0] >= BOUND_MAX_X and 
              (goal_center_y - goal_width/2) <= ball_pos[1] <= (goal_center_y + goal_width/2) and 
              ball_pos[2] < goal_height):
            player1_score += 1
            print(f"Goal for Player 1! Score: {player1_score}-{player2_score}")
            reset_after_goal()
        
        #wall collisions
        if ball_pos[0] <= BOUND_MIN_X:
            ball_pos[0] = BOUND_MIN_X
            ball_velocity[0] = -ball_velocity[0] * 0.7
        elif ball_pos[0] >= BOUND_MAX_X:
            ball_pos[0] = BOUND_MAX_X
            ball_velocity[0] = -ball_velocity[0] * 0.7
            
        if ball_pos[1] <= BOUND_MIN_Y:
            ball_pos[1] = BOUND_MIN_Y
            ball_velocity[1] = -ball_velocity[1] * 0.7
        elif ball_pos[1] >= BOUND_MAX_Y:
            ball_pos[1] = BOUND_MAX_Y
            ball_velocity[1] = -ball_velocity[1] * 0.7
        
        
        #checking if any player can possess the ball when it is nearly stopped
        if possession_cooldown <= 0:
            dist1 = math.sqrt((player1_pos[0] - ball_pos[0])**2 + (player1_pos[1] - ball_pos[1])**2)
            dist2 = math.sqrt((player2_pos[0] - ball_pos[0])**2 + (player2_pos[1] - ball_pos[1])**2)

            if dist1 < 35 and ball_pos[2] < 35:
                ball_possessed = 1
                ball_velocity = [0, 0, 0]
                print("Player 1 has the ball")
            elif dist2 < 35 and ball_pos[2] < 35:
                ball_possessed = 2
                ball_velocity = [0, 0, 0]
                print("Player 2 has the ball")

    #update ball position when possessed
    elif ball_possessed == 1:
        #position the ball in front of player 1
        offset = 30 
        ball_pos[0] = player1_pos[0] + offset * math.cos(math.radians(player1_angle))
        ball_pos[1] = player1_pos[1] + offset * math.sin(math.radians(player1_angle))
        ball_pos[2] = 15 
        
    elif ball_possessed == 2:
        #position the ball in front of player 2
        offset = 30
        ball_pos[0] = player2_pos[0] + offset * math.cos(math.radians(player2_angle))
        ball_pos[1] = player2_pos[1] + offset * math.sin(math.radians(player2_angle))
        ball_pos[2] = 15  

    glutPostRedisplay()



def reset_after_goal():
    global ball_pos, ball_velocity, ball_possessed, player1_pos, player2_pos
    
    #reset ball
    ball_pos = [0.0, 0.0, 15.0]
    ball_velocity = [0.0, 0.0, 0.0]
    ball_possessed = 0
    
    #reset players
    player1_pos = [-150.0, 0.0]
    player2_pos = [150.0, 0.0]


def setup_camera():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(fov_y, 1.25, 0.1, 1500)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    if cam_mode == 0: #third person
        ang = math.radians(cam_angle_h)
        cam_pos[0] = cam_radius * math.cos(ang)
        cam_pos[1] = cam_radius * math.sin(ang)
        cam_pos[2] = cam_height
        cam_target[0] = 0
        cam_target[1] = 0
        cam_target[2] = 0
    else:
        # first person active player
        if active_player == 1:
            pos = player1_pos
            angle = player1_angle
        else:
            pos = player2_pos
            angle = player2_angle
            
        ang = math.radians(angle)
        cam_pos[0] = pos[0] - 100 * math.cos(ang)
        cam_pos[1] = pos[1] - 100 * math.sin(ang)
        cam_pos[2] = 100
        cam_target[0] = pos[0] + 20 * math.cos(ang)
        cam_target[1] = pos[1] + 20 * math.sin(ang)
        cam_target[2] = 30
    
    gluLookAt(*cam_pos, *cam_target, *cam_up)


def show_screen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_sky()
    glLoadIdentity()
    glViewport(0, 0, 1000, 800)
    
    setup_camera()
    
    #game elements
    draw_field()
    draw_player(player1_pos, player1_angle, player1_color)
    draw_player(player2_pos, player2_angle, player2_color)
    draw_ball()
    draw_coins()
    if rain_mode:
        draw_rain()
    if snow_mode:
        draw_snow()
    
    #game info
    minutes = int(time_elapsed) // 60
    seconds = int(time_elapsed) % 60
    
    if not game_over:
        draw_text(10, 760, f"Score: Player 1 ({player1_score} - {player2_score}) Player 2")
        draw_text(10, 730, f"Time: {minutes:02d}:{seconds:02d}")
        draw_text(10, 700, f"Active Player: Player {active_player}")
        
        draw_text(10, 670, "Player 1: W,A,S,D to move, SPACE to kick")
        draw_text(10, 640, "Player 2: I,J,K,L to move, O to kick")
        draw_text(10, 610, "Press TAB to switch active camera view")


        if coin_visible:
            draw_text(10, 584, "Coin available! Catch it for 3x goals")
        if cheat_mode:
            draw_text(10, 554, "Cheat mode enabled! Press 'C' to disable")
        else:
            draw_text(10, 554, "Cheat mode disabled! Press 'C' to enable")
        if rain_mode:
            draw_text(10, 524, "Rain mode enabled! Press 'M' to disable")
        if snow_mode:
            draw_text(10, 524, "Snow mode enabled! Press 'P' to disable")

        
    else:
        draw_text(433, 400, "GAME OVER")
        if player1_score > player2_score:
            draw_text(442, 370, "Player 1 Wins!")
        elif player2_score > player1_score:
            draw_text(442, 370, "Player 2 Wins!")
        else:
            draw_text(442, 370, "It's a Draw!")
    
        draw_text(377, 340, "Press 'R' to restart the game")
    
    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1000, 800)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"3D 2-Player Football Game")
    glutDisplayFunc(show_screen)
    glutKeyboardFunc(keyboard_down) 
    glutKeyboardUpFunc(keyboard_up)  
    glutSpecialFunc(special_key_listener)
    glutMouseFunc(mouse_listener)
    glutIdleFunc(animate)
    glEnable(GL_DEPTH_TEST)
    glutMainLoop()

if __name__ == "__main__":
    main()