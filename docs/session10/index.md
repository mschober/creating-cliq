# Session 10
> Moving the snake into the open world. Take a moment to refresh your memory on the state of things in session09.
Constants can be used to resize the screen and the starting base.

### Might look like this: clean grid
![clean grid](https://drive.google.com/uc?export=download&id=0B3SFnARVIcGLbTM4LXBVVXpPcjA)

> If we want to capture new squares the snake needs to move on the grid and keep track of leaving the base, colliding with itself, re-entring the base. But before we worry about collisions lets dust off our memory of how the movement is currently implemented. Velocities were used to constantly move in whichever the most recent direction was. Lets comment the body of each of the directional if statements and create stub functions for each direction.

## Code snippet before changing
```python
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

```

## New stubs

```python
    def move_right(self):
        pass
    
    def move_left(self):
		pass
    
    def move_up(self):
        pass
    
    def move_down(self):
        pass
```

## Refactoring the bodies into the stubs and commenting the velocites.

```python
    def move_right(self):
        print "move right"

        #self.circle_shape.update_x(Character.move_dist)
        #Character.vel = [Character.move_dist, 0]

    def move_left(self):
        print "move left"

        #self.circle_shape.update_x(-Character.move_dist)    
        #Character.vel = [-Character.move_dist, 0]

    def move_up(self):
        print "move up"

        #self.circle_shape.update_y(-Character.move_dist)
        #Character.vel = [0, -Character.move_dist]
    
    def move_down(self):
        print "move down"

        #self.circle_shape.update_y(Character.move_dist)
        #Character.vel = [0, Character.move_dist]
    
    def move (self, key):

        #check if key is in key_map array. 
        #Character: this class name
        if key in Character.key_map.values():
            if key == Character.key_map["right"]:
                move_right()
                
            if key == Character.key_map["left"]:
                move_left()
                
            if key == Character.key_map["up"]:
                move_up()
                
            if key == Character.key_map["down"]:
                move_down()
```
