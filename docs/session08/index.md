# Session 08
> Snake on the grid.

> Now that grid movement has been established we need to consider how to construct a snake on the grid. You can think of a snake as a list of points in order. Every time the snake head moves the previous head needs to be added to the body. Every time the print loop runs, print ever segment in the body and print the head. 

## Reviewing last week
> Take a look at where we left off last week. Using the existing velocity snake we added a grid to the board. If you didn't get a chance to complete the entire grid or randomize it, you can see the working code as well. Navigate to last weeks code, select all and copy, paste into a new [codeskulptor](http://www.codeskulptor.org/).

#### [Last Weeks Code](from_last_week.md)

### Remove the grid and stop the snake
> Now that we can create squares on the screen we want to clear it up again and create a blank canvas. 

> Comment the following lines

```python
# cliq = Character()            
# grid = SquareGrid() 
```

```python
    if ticker == 3:
    #    cliq.save_me()    
        ticker = 0
    # cliq.draw_me(canvas)    # draw circle
    # grid.draw_me(canvas)    # draw grid
```

```python
    if ticker == 3:
    #    cliq.save_me()    
        ticker = 0
    # cliq.draw_me(canvas)    # draw circle
    # grid.draw_me(canvas)    # draw grid
```

```python
# frame.set_keydown_handler(cliq.move) #for move circle******
```
> Then run the program and there should be nothing on the screen and no errors.


