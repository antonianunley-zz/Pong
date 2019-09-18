try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
#PONG ANTONIA NUNLEY 

import random

BALL_SPEED = 3.978
X_DROP = random.randrange(23, 43)
Y_DROP = -(random.randrange(13, 23))

WIDTH = 1000
HEIGHT = 700
BALL_RADIUS = 20

PADDLE_OFF_WALL_X = 20
PADDLE_OFF_WALL_Y = 50

paddle_l_vel = 0
paddle_r_vel = 0

PADDLE_WIDTH = 12
paddle_l_start = [PADDLE_OFF_WALL_X, HEIGHT/2 - PADDLE_OFF_WALL_Y]
paddle_l_end = [PADDLE_OFF_WALL_X, HEIGHT/2 + PADDLE_OFF_WALL_Y]

paddle_r_start = [(WIDTH - 1) - PADDLE_OFF_WALL_X, HEIGHT/2 - PADDLE_OFF_WALL_Y]
paddle_r_end = [(WIDTH - 1) - PADDLE_OFF_WALL_X, HEIGHT/2 + PADDLE_OFF_WALL_Y]

right_points = 0
left_points = 0

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [X_DROP / BALL_SPEED, Y_DROP / BALL_SPEED]
    
    
def ball_start(X_DROP):
    global paddle_l_start, paddle_l_end, paddle_r_start, paddle_r_end, ball_pos, vel, Y_DROP
    
    Y_DROP = -(random.randrange(4, 9))
    
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    vel = [X_DROP / BALL_SPEED, Y_DROP / BALL_SPEED]
    
def keydown(key):
    global paddle_l_start, paddle_l_end, paddle_r_start, paddle_r_end, paddle_l_vel, paddle_r_vel
        
    if (key == simplegui.KEY_MAP['up']):
        paddle_r_start[1] += paddle_r_vel
        paddle_r_end[1] += paddle_r_vel
        paddle_r_vel = -4
        
    if (key == simplegui.KEY_MAP['down']):
        paddle_r_start[1] += paddle_r_vel
        paddle_r_end[1] += paddle_r_vel
        paddle_r_vel = +4
    
    if (key == simplegui.KEY_MAP['W']):
        paddle_l_start[1] += paddle_l_vel
        paddle_l_end[1] += paddle_l_vel
        paddle_l_vel = -4
        
    if (key == simplegui.KEY_MAP['S']):
        paddle_l_start[1] += paddle_l_vel
        paddle_l_end[1] += paddle_l_vel
        paddle_l_vel = +4
        
def keyup(key):
     global paddle_l_start, paddle_l_end, paddle_r_start, paddle_r_end, paddle_l_vel, paddle_r_vel
        
     if (key == simplegui.KEY_MAP['up']):
        #paddle_r_start[1] = 0
        #paddle_r_end[1] = 0
        paddle_r_vel = 0
        
     if (key == simplegui.KEY_MAP['down']):
        #paddle_r_start[1] = 0
        #paddle_r_end[1] = 0
        paddle_r_vel = 0
        
     if (key == simplegui.KEY_MAP['W']):
        #paddle_l_start[1] = 0
        #paddle_l_end[1] = 0
        paddle_l_vel = 0
        
     if (key == simplegui.KEY_MAP['S']):
        #paddle_l_start[1] = 0
        #paddle_l_end[1] = 0
        paddle_l_vel = 0
        
def wall_collision():
    global ball_pos
    global vel
        
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
    
    if ball_pos[0] <= BALL_RADIUS:
        vel[0] = -vel[0]
        
    if ball_pos[0] >= WIDTH-BALL_RADIUS:
        vel[0] = -vel[0]
       
    if ball_pos[1] <= BALL_RADIUS:
        vel[1] = -vel[1]
        
    if ball_pos[1] >= HEIGHT-BALL_RADIUS:
        vel[1] = -vel[1]

def paddle_collision():
    global paddle_l_start, paddle_l_end, paddle_r_start, paddle_r_end, ball_pos, vel, PADDLE_WIDTH
        
    if ball_pos[0] - (BALL_RADIUS + PADDLE_WIDTH) <= paddle_l_start[0] and ((ball_pos[1] - BALL_RADIUS or ball_pos[1] + BALL_RADIUS)  >= paddle_l_start[1] and (ball_pos[1] - BALL_RADIUS or ball_pos[1] 
                                                                                                                                                   + BALL_RADIUS) <= paddle_l_end[1]):
        vel[0] = -vel[0]
            
    if ball_pos[0] + (BALL_RADIUS + PADDLE_WIDTH) >= paddle_r_start[0] and ((ball_pos[1] + BALL_RADIUS or ball_pos[1] - BALL_RADIUS) >= paddle_r_start[1] and (ball_pos[1] - BALL_RADIUS or ball_pos[1] 
                                                                                                                                                  + BALL_RADIUS) <= paddle_r_end[1]):
        vel[0] = -vel[0]  
        
def point():
    global paddle_l_start, paddle_l_end, paddle_r_start, paddle_r_end, ball_pos, vel, right_points, left_points, BALL_RADIUS, WIDTH
        
    if ball_pos[0] < BALL_RADIUS:
        right_points = int(right_points)
        right_points += 1
        X_DROP = random.randrange(23, 33)
        ball_start(X_DROP)
        
    if ball_pos[0] > (WIDTH - BALL_RADIUS):
        left_points = int(left_points)
        left_points += 1
        X_DROP = random.randrange(23, 33)
        ball_start(-X_DROP)

def restart():
    global left_points, right_points, ball_pos, X_DROP, Y_DROP, BALL_SPEED, paddle_l_start, paddle_l_end, paddle_r_start, paddle_r_end, WIDTH, HEIGHT, PADDLE_OFF_WALL_Y, PADDLE_OFF_WALL_X
  
    left_points = 0
    right_points = 0
    
    paddle_l_start = [PADDLE_OFF_WALL_X, HEIGHT/2 - PADDLE_OFF_WALL_Y]
    paddle_l_end = [PADDLE_OFF_WALL_X, HEIGHT/2 + PADDLE_OFF_WALL_Y]

    paddle_r_start = [(WIDTH - 1) - PADDLE_OFF_WALL_X, HEIGHT/2 - PADDLE_OFF_WALL_Y]
    paddle_r_end = [(WIDTH - 1) - PADDLE_OFF_WALL_X, HEIGHT/2 + PADDLE_OFF_WALL_Y]


    
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
def draw(canvas):
    global HEIGHT, WIDTH, left_points, right_points, PADDLE_WIDTH, ball_pos, paddle_l_start, paddle_r_start, paddle_l_end, paddle_r_end, paddle_l_vel, paddle_r_vel
   
    paddle_l_start[1] += paddle_l_vel
    paddle_l_end[1] += paddle_l_vel
    paddle_r_start[1] += paddle_r_vel
    paddle_r_end[1] += paddle_r_vel
    
   
    point()
    wall_collision()
    paddle_collision()
    
    
    left_points = str(left_points)
    right_points = str(right_points)
    
    canvas.draw_text(left_points, ((WIDTH/2 - 50), 60), 45, 'aqua')
    canvas.draw_text(right_points, ((WIDTH/2 + 50), 60), 45, 'aqua')
    
    
    
    canvas.draw_line(paddle_l_start, paddle_l_end, PADDLE_WIDTH, "aqua")
    canvas.draw_line(paddle_r_start, paddle_r_end, PADDLE_WIDTH, "aqua")
    canvas.draw_line((WIDTH/2, 0), (WIDTH/2, HEIGHT), 2, "navy")
    canvas.draw_line((((paddle_l_start[0] + (PADDLE_WIDTH/2) + 1)) , 0), (((paddle_l_start[0] + (PADDLE_WIDTH/2) + 1)), HEIGHT), 2 , "navy")
    canvas.draw_line((((paddle_r_start[0] - (PADDLE_WIDTH/2) + 1)) , 0), (((paddle_r_start[0] - (PADDLE_WIDTH/2) + 1)), HEIGHT), 2 , "navy")
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "aqua", "black")     

frame = simplegui.create_frame("PONG", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("RESTART" , restart, 100)
frame.set_canvas_background("teal")
frame.start()
