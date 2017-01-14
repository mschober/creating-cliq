import simplegui

size = 50
grid_spot = 0,0

def square_coords_from_grid(size, grid_spot):
    return [(0,0), (50,0), (50,50), (0,50)]

points = square_coords_from_grid(size, grid_spot)
    

def draw(canvas):
    canvas.draw_polygon(
        points, 3, "Blue", "Green"    
    )
    
frame = simplegui.create_frame("Home", 500, 500)
frame.set_draw_handler(draw)
frame.start()
