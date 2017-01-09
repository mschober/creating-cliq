import simplegui, time

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

# return rectangle coordinate
#===================================================
def rect_coords (length, height, startpos = (0, 0)) :
    return [
        (startpos[0], startpos[1]),
        (startpos[0], startpos[1] + height),
        (startpos[0] + length, startpos[1] + height),
        (startpos[0] + length, startpos[1])  
    ]






'''
canvas.draw_circle(center_point, radius, 
                  line_width, line_color, fill_color = color)
=> classes needed
   - ShapeAttributes: line_width, line_color, fill_color = color
   - Circle: center_point, radius, def: update_x, update_y
   - Character: def: draw circle, getKey> update x/y     
'''
#===================================================
class ShapeAttributes:
    def __init__ (self):
        self.line_width = 2
        self.line_color = "Aqua"
        self.fill_color = "Pink"
        
        # For color: http://www.codeskulptor.org/docs.html#Colors
        

class Circle:
    def __init__ (self):
        self.radius = 3
        self.center_point = (100, 100)
    
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
        
        
    #draw a circle on canvas
    #(center_point, radius, line_width, line_color, fill_color = color
    def draw_me (self, canvas):
        
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
           
        canvas.draw_circle (
            self.circle_shape.center_point,
            self.circle_shape.radius,
            self.shape_attributes.line_width,
            self.shape_attributes.line_color,
            self.shape_attributes.fill_color
        )
        
        for segment in self.body.list_segments():
            canvas.draw_circle(
                segment,
                self.circle_shape.radius /2,
                self.shape_attributes.line_width,
                self.shape_attributes.fill_color,
                self.shape_attributes.fill_color    
            )
    
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
        

class SquareGrid:
    
    class GridElement:
        def __init__(self):
            self.filled = False

    def __init__(self):
        self.grid_array = self.init_grid(
            WINDOW_WIDTH,
            WINDOW_HEIGHT
        )
        
    def init_grid(self, width, height):
        grid_elements = []
        for x in xrange(0, width, 50):
            ylist = []
            for y in xrange(0, height, 50):
                #print 'DEBUG - adding grid el %s, %s' % (x,y)
                ylist.append(self.GridElement())
            grid_elements.append(ylist)
        #print "DEBUG - size is: %s" % str(map(lambda x: str(len(x)), grid_elements))

        return grid_elements
    
    def draw_me(self, canvas):
        size = 50
        for x in xrange(len(self.grid_array[0])):
            canvas.draw_polygon(
                [
                    (x*size, size), 
                    (x*size+size, size), 
                    (x*size+size, size*2),
                    (x*size, size*2)
                ], 1, 'Green', 'Orange'
            )
            
cliq = Character()            
grid = SquareGrid()                


    
        
        

# draw on canvas
#===================================================
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
        cliq.save_me()    
        ticker = 0
    cliq.draw_me(canvas)    # draw circle
    grid.draw_me(canvas)    # draw grid
    
       
    return
 

# add functions and handler to frame
#===================================================
frame = simplegui.create_frame("Home", WINDOW_WIDTH, WINDOW_HEIGHT)
frame.set_canvas_background("Silver")

frame.set_draw_handler(draw)
frame.set_keydown_handler(cliq.move) #for move circle******

frame.start()

