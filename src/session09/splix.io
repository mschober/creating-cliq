import simplegui, time, random

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
GLOBAL_DEFAULT_SQUARE_SIZE = 25
IN_SQUARES = GLOBAL_DEFAULT_SQUARE_SIZE
BASE_SHIFT_X = 5
BASE_SHIFT_Y = 5
GLOBAL_CIRCLE_RADIUS = 3
GLOBAL_NUM_ROWS = 10
GLOBAL_NUM_COLS = 10

def rect_coords (length, height, startpos = (0, 0)) :
    x = startpos[0]
    y = startpos[1]
    return [
        (x, y),
        (x, y + height),
        (x + length, y + height),
        (x + length, y)  
    ]

class SquareGrid:
    
    SQUARE_PIXEL_SIZE = GLOBAL_DEFAULT_SQUARE_SIZE
    NUM_ROWS = GLOBAL_NUM_ROWS
    NUM_COLS = GLOBAL_NUM_COLS
    
    def __init__(self):
        self.grid_elements = self.init_grid(
            WINDOW_WIDTH,
            WINDOW_HEIGHT
        )

    def init_grid(self, width, height):
        num_rows = self.NUM_ROWS
        num_cols = self.NUM_COLS
        grid_elements = []
        
        for x in range(num_rows):
            for y in range(num_cols):
                grid_elements.append((x+BASE_SHIFT_X,y+BASE_SHIFT_Y))
        return grid_elements

    def draw_me(self, canvas):
        size = self.SQUARE_PIXEL_SIZE
        for pos in self.grid_elements:
            x = pos[0] * size
            y = pos[1] * size
            canvas.draw_polygon(
                rect_coords(size, size, (x,y)),
                1, 'Green', 'Orange'
            )

class ShapeAttributes:
    def __init__ (self):
        self.line_width = 2
        self.line_color = "Aqua"
        self.fill_color = "Pink"

        # For color: http://www.codeskulptor.org/docs.html#Colors


class Circle:
    
    START_POINT_X = BASE_SHIFT_X*IN_SQUARES
    START_POINT_Y = BASE_SHIFT_Y*IN_SQUARES
    RADIUS = GLOBAL_CIRCLE_RADIUS
    
    def __init__ (self):
        x = self.START_POINT_X
        y = self.START_POINT_Y
        
        self.radius = self.RADIUS
        self.center_point = (x,y)

    '''
    def update_x (self, shift_x):
        self.center_point = (
            self.center_point[0] + shift_x,
            self.center_point[1]
        )

    def update_y (self, shift_y):
        self.center_point = (
            self.center_point[0],
            self.center_point[1] + shift_y
        )
    '''

class Body:

    def __init__(self):
        self.body_segments = []

    def append(self, segment):
        self.body_segments.append(segment)

    def list_segments(self):
        return list(self.body_segments)

class Character:
    key_map = {
        "left": 37,
        "up"  : 38,
        "right":39,
        "down": 40
    }

    move_dist = 5
    vel = [move_dist, 0]

    def __init__ (self):
        self.circle_shape = Circle()
        self.shape_attributes = ShapeAttributes()
        self.body = Body()

    def bumps_into_left_wall(self):
        return self.circle_shape.center_point[0] <= self.circle_shape.radius

    def morph_into_red_dot(self):
        self.shape_attributes.fill_color = "Red"
        self.circle_shape.radius = 50

    def morph_into_black_dot(self):
        self.shape_attributes.fill_color = "Black"
        self.circle_shape.radius = 9

    def morph_into_pink_dot(self):
        self.shape_attributes.fill_color = "Pink"
        self.circle_shape.radius = 30

    def morph_into_purple_dot(self):
        self.shape_attributes.fill_color = "Purple"
        self.circle_shape.radius = 60

    def bumps_into_right_wall(self):
        return self.circle_shape.center_point[0] >= WINDOW_WIDTH-self.circle_shape.radius

    def bumps_into_ceiling(self):
        return self.circle_shape.center_point[1] <= self.circle_shape.radius

    def bumps_into_floor(self):
        return self.circle_shape.center_point[1] >= WINDOW_HEIGHT-self.circle_shape.radius 

    def save_me(self):
        segment = self.circle_shape.center_point
        self.body.append(segment)

    def draw_me(self, canvas):
        self.draw_circle(canvas, self.circle_shape.center_point)
    
    def draw_circle(self, canvas, center):
        canvas.draw_circle(
                center,
                self.circle_shape.radius,
                self.shape_attributes.line_width,
                self.shape_attributes.fill_color,
                self.shape_attributes.fill_color    
            )

    def draw_me_2 (self, canvas):

        #=================add=======================
        #self.circle_shape.center_point[0] += Character.vel[0]
        # can't change value above. but can point to different reference
        self.circle_shape.center_point = (
            self.circle_shape.center_point[0] +  Character.vel[0],
            self.circle_shape.center_point[1] + Character.vel[1]
        )

        if self.bumps_into_left_wall():
            self.morph_into_red_dot()

        if self.bumps_into_right_wall():
            self.morph_into_black_dot()

        if self.bumps_into_ceiling():
            self.morph_into_pink_dot()

        if self.bumps_into_floor():
            self.morph_into_purple_dot()

        #self.circle_shape.center_point[1] += vel[1]

        self.draw_circle(canvas, self.circle_shape.center_point)

        for segment in self.body.list_segments():
            self.draw_circle(canvas, segment)
    # get input key press and move the circle
    def move (self, key):

        #check if key is in key_map array. 
        #Character: this class name
        if key in Character.key_map.values():
            if key == Character.key_map["right"]:
                print "move right"

                #self.circle_shape.update_x(Character.move_dist)
                Character.vel = [Character.move_dist, 0]

            if key == Character.key_map["left"]:
                print "move left"

                #self.circle_shape.update_x(-Character.move_dist)    
                Character.vel = [-Character.move_dist, 0]

            if key == Character.key_map["up"]:
                print "move up"

                #self.circle_shape.update_y(-Character.move_dist)
                Character.vel = [0, -Character.move_dist]
        if key == Character.key_map["down"]:
                print "move down"

                #self.circle_shape.update_y(Character.move_dist)
                Character.vel = [0, Character.move_dist]

snake = Character()            
grid = SquareGrid()                


ticker = 0
def draw(canvas):

        #canvas.draw_polygon(point_list, 
        #line_width, line_color, fill_color = color)    
    box1 = rect_coords(WINDOW_WIDTH, WINDOW_HEIGHT, startpos = (0, 0))
    #box2 = rect_coords(480, 480, startpos = (20, 20))
    canvas.draw_polygon(box1, 20, "Aqua") #draw rectangle
    #canvas.draw_polygon(box2, 20, "Pink")

#    print time.time().
    global ticker 
    ticker += 1
    if ticker == 3:
        #snake.save_me()    
        ticker = 0
    grid.draw_me(canvas)    # draw grid
    snake.draw_me(canvas)    # draw circle


    return


# add functions and handler to frame
#===================================================
frame = simplegui.create_frame("Home", WINDOW_WIDTH, WINDOW_HEIGHT)
frame.set_canvas_background("Silver")

frame.set_draw_handler(draw)
#frame.set_keydown_handler(snake.move) #for move circle******

frame.start()
