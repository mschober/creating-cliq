import simplegui

def square_coordinates(size, initial_position):
    x = initial_position[0]
    y = initial_position[1]
    
    points = [
        (x,y), (x+1,y), (x+1,y+1), (x,y+1)
    ]

    new_points = []
    for point in points:
        x=point[0]
        y=point[1]
        new_point = (size*x, size*y)
        new_points.append(new_point)

    return new_points

x = 2
y = 1
size = 50
initial_position = (x,y)


def draw(canvas):
    size = 50
    x = 3
    y = 3 
    canvas.draw_polygon(
                [
                    (x, y),
                    ((x+size), y),
                    ((x+size), (y+size)),
                    (x, (y+size))
                ], 1, 'Green', 'Orange'
            )

frame = simplegui.create_frame("Home", 500,500)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
