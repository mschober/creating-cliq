cliq = Character()            
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
