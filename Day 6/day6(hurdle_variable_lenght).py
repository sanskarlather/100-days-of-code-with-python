#Reeborgs world hurdle with variable length
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    
    turn_left()
    while wall_on_right() and not wall_in_front():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
        
    
    