def rect_coords (length, height, startpos = (0, 0)) :
    x = startpos[0]
    y = startpos[1]
    return [
        (x, y),
        (x, y + height),
        (x + length, y + height),
        (x + length, y)  
    ]
