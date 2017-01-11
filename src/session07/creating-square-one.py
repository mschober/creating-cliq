import simplegui

def draw(canvas):
    canvas.draw_polygon(
        [(0,0), (100,0), (100,100), (0,100)],
        5,
        "Blue",
        "Pink"
        )

frame = simplegui.create_frame("Home", 300, 200)
frame.set_draw_handler(draw)
frame.start()
