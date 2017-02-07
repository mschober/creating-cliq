# Session 10
> Moving the snake into the open world. Take moment to refresh your memory on the state of things in session09.
Constants can be used to resize the screen and the starting base.



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
