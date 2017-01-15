home_square = Square((5, 5), SIZE)
the_snake = Snake(home_square)
  
def move(key):
    x = home_square.point[0]
    y = home_square.point[1]
    if KEYMAP[LEFT] == key:
        the_snake.move_left()
    elif KEYMAP[RIGHT] == key:
        the_snake.move_right()
    elif KEYMAP[UP] == key:
        the_snake.move_up()
    elif KEYMAP[DOWN] == key:
        the_snake.move_down()
    else :
        print "unused"

def draw(canvas):
    for square in the_snake.snake_map.values():
        square.draw(canvas)

    
frame = simplegui.create_frame("Home", *WINDOW)
frame.set_draw_handler(draw)
frame.set_keydown_handler(move)
frame.start()

