import simplegui

SIZE = 25
SNAKE_COLOR = ("Gold", "Purple")
WINDOW = (500,500)
LEFT = "LEFT"
UP = "UP"
RIGHT = "RIGHT"
DOWN = "DOWN"

KEYMAP = {
    LEFT: 37,
    RIGHT: 39,
    DOWN: 40,
    UP: 38
}

def square_coords_from_grid(size, grid_spot):
    x = grid_spot[0]
    y = grid_spot[1]
    points = [(x,y), (x+1,y), (x+1,y+1), (x,y+1)]
    scaled_points = map(lambda point:
                        (point[0]*size,point[1]*size), 
                        points)
    print scaled_points
    return scaled_points

class Square(object):
    def __init__(self, point, size, color=SNAKE_COLOR):
        print point
        self.size = size
        self.point = point
        self.points = square_coords_from_grid(size, point)
        self.color = color
    
    def draw(self, canvas):
        canvas.draw_polygon(
        self.points, 3, self.color[0], self.color[1]
    )

    def set_color(self, color):
        self.color = color
    
class Snake:
    def __init__(self, square):
        self.head = square
        self.snake_map = {}
        self.poly_points = []
        self.add(square.point)
    
    def add(self, point):
        square = Square(point, self.head.size)
        pos_key = "%s-%s" % (point[0], point[1])
        self.snake_map[pos_key] = square
        self.head = square
        self.poly_points.append(map(lambda x: x*SIZE, point))
        
    def move_left(self):
        x = self.head.point[0] - 1
        y = self.head.point[1]
        self.add((x,y))
        
    def move_right(self):
        x = self.head.point[0] + 1
        y = self.head.point[1]
        self.add((x,y))
    
    def move_up(self):
        x = self.head.point[0]
        y = self.head.point[1] -1
        self.add((x,y))

    def move_down(self):
        x = self.head.point[0]
        y = self.head.point[1] +1
        self.add((x,y))

    def draw(self, canvas):
        for square in self.snake_map.values():
            square.draw(canvas)
        canvas.draw_polygon(self.poly_points, 3, "Red")
        
    def get_position_key(self):
        pos_key = "%s-%s" % (self.head.point[0], self.head.point[1])
        return pos_key

class HomeBase:
    
    def __init__(self, start_pos, size):
        self.start_pos = start_pos
        self.home_base_map = {}
        self.fill_home_base(size)
    #(0,0)          (9,0)            (19,0)
    
    
    
   #            (4,4)            (14,4)
    
    
   #            (4,14)           (14,14)
    
    
    #(0,19)         (9,19)           (19,19)
    def add(self, square):
        point = square.point
        pos_key = "%s-%s" % (point[0], point[1])
        self.home_base_map[pos_key] = square
        
    def fill_home_base(self, size):
        sp = self.start_pos
        tl_x = (3 * sp[0])/4
        tl_y = (3 * sp[1])/4
        for x in range(size):
            for y in range(size):
                square = Square((x + tl_x, y + tl_y), SIZE)
                self.add(square)

    def draw(self, canvas):
        for square in self.home_base_map.values():
            square.draw(canvas)

home_base = HomeBase((10,10), 5)
home_square = Square((9, 7), SIZE)
the_snake = Snake(home_square)
  
def move(key):
    global the_snake
    the_snake.head.set_color(("Green", "Blue"))
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
        
    snake_keys = the_snake.snake_map.keys();
    if the_snake.get_position_key() in home_base.home_base_map.keys():
        print "The snake is in the base, creating a new snake"
        the_snake = Snake(the_snake.head)
    print len(the_snake.snake_map.keys())

    #if not the_snake.get_position_key() in home_base.home_base_map.keys() and len(snake_keys) == 2:
    #    print "left the base!"
    #    the_snake = Snake(the_snake.head)
    #if the_snake.get_position_key() in home_base.home_base_map.keys() and len(snake_keys) != 2 :
    #    print "into the base!"
    #    the_snake = Snake(the_snake.head)
    #if the_snake.get_position_key() in home_base.home_base_map.keys() and len(snake_keys) == 2 :
    #   print "stays in the base"
    #    the_snake = Snake(the_snake.head)
        
def draw(canvas):
    the_snake.draw(canvas)
    home_base.draw(canvas)
    
frame = simplegui.create_frame("Home", *WINDOW)
frame.set_draw_handler(draw)
frame.set_keydown_handler(move)
frame.start()
