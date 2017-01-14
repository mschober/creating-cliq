import simplegui

# abstract the points based on the size

size = 50
grid_spot = 3,2

def square_coords_from_grid(size, grid_spot):
    x = grid_spot[0]
    y = grid_spot[1]
    points = [(x,y), (x+1,y), (x+1,y+1), (x,y+1)]
    scaled_points = map(lambda point:
                        (point[0]*size,point[1]*size), 
                    points)
    print scaled_points
    return scaled_points

points = square_coords_from_grid(size, grid_spot)

def draw(canvas):
    canvas.draw_polygon(
        points, 3, "Blue", "Green"    
    )

keymap = {
    "left": 37,
    "right": 39,
    "down": 40,
    "up": 38
}    
    
def move(key):
    if keymap["left"] == key:
        print "left"
    elif keymap["right"] == key:
        print "right"
    elif keymap["up"] == key:
        print "up"
    elif keymap["down"] == key:
        print "down"
    else :
        print "unused"
    
frame = simplegui.create_frame("Home", 500, 500)
frame.set_draw_handler(draw)
frame.set_keydown_handler(move)
frame.start()

