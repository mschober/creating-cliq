# Session 10
> Moving the snake into the open world. Take a moment to refresh your memory on the state of things in session09.
Constants can be used to resize the screen and the starting base.

Code from [Session09](https://raw.githubusercontent.com/bellcodo/creating-cliq/master/src/session09/splix.io)

### Might look like this: clean grid
![clean grid](https://drive.google.com/uc?export=download&id=0B3SFnARVIcGLbTM4LXBVVXpPcjA)

> If we want to capture new squares the snake needs to move on the grid and keep track of: leaving the base, colliding with itself, and re-entring the base. But before we worry about collisions lets dust off our memory of how the movement is currently implemented. Velocities were used to constantly move in whichever the most recent direction was. 

1. Find the movement code that is currently turned off. The method signature is `def move(self, key):`.
2. Comment the body of each of the directional statements.

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
3. Create stub functions for each direction.

	> New stubs

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
4. Move the commented functionality from the move function into the stubs.
	
	> Refactoring the bodies into the stubs and commenting the velocites.

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
> The move functions are in the class so they'll need `self.` added. (I missed that!). We also need to reenable the keyhandler down below.

```python
frame.set_keydown_handler(snake.move) #for move circle******
```

* Diff of code [here](https://github.com/bellcodo/creating-cliq/commit/a79a4b4b51b99102cd5fc12842fabaf615340b6f)

### Might look like this: directions
![directions](https://drive.google.com/uc?export=download&id=0B3SFnARVIcGLNGsxdHpCWVFSNXc)

> Reenabling the keydown handler for each of the cardinal directions is apart of a coding principle that reduces the liklihood you'll be scratching your head about what is broken and why. The idea is implement the simplest thing that you know keeps everything running correctly. Print statements in the bodies of each of the movement keys allows you to run the app again, press all the keys, and make sure there is not an interpretation error or that one of the keys doesn't print. Along with this philosophy lets pick 1 direction and try and implement a solution for moving the snake head. If it works for one direction it should be straight forward to adapt a solution for the others. Hint hint since the other directions are directly dependent on the same logic this is a great time to use a method to handle the logic. But feel free to start in the body of the `up` direction first and port the logic to a method after it is working.

> To move right what needs to happen? Update the `center_point` of the `circle_shape` on the snake by `1 square` width in the positive `x` direction.

```python
    def move_right(self):
        print "move right"
        curr_center = self.circle_shape.center_point
        next_center = (curr_center[0] + IN_SQUARES, curr_center[1])
        self.circle_shape.center_point = next_center
```

> Run the code and try moving to the right.

> The next step is to pull out a new function that takes a parameter indicating which direction to move. The four possible inputs are

```python
update_direction((1,0))  # right
update_direction((-1,0)) # left
update_direction((0,-1)) # up
update_direction((0,1))  # down
```

> The `1` represents moving on square in the grid, but you need to multiple by `IN_SQUARES` inside the `update_direction` function. Multipling both values in incoming `shift_point` can be done with either a `map` technique or a `for:each` loop.

#### Map
```python
	# Will multiply IN_SQUARES by both the x and y points in shift_point
        sqr_shift_point = map(lambda pt: pt*IN_SQUARES, shift_point)
```

#### For:Each
```python
	# Will multiply IN_SQUARES by both the x and y points in shift_point
	for pt in shift_point:
		sqr_shift_point = []
		sqr_shift_point.append(pt*IN_SQUARES)
```

> Once the `shift_point` has been updated to the grid square width, its time to sum the `x`'s and `y`'s of the `shift_point` and `center_point`. This can also be accomplished with either a `reduce` techinque or by simplying summing the `x`'s and `y`'s directly.

#### Reduce
```python
        pt = self.circle_shape.center_point
	# Will create a new point with the current position is summed with the shift amount.
        new_point = reduce(lambda x,y: (x[0]+y[0],x[1]+y[1]), [pt, sqr_shift_point])
```

#### Simple Assignment
```python
        pt = self.circle_shape.center_point
	# Will create a new point with the current position is summed with the shift amount.
        new_point = (
            pt[0] + sqr_shift_point[0], 
            pt[1] + sqr_shift_point[1], 
        )
```

> The final bit is to assign the `new_point` you've created to the `center_point` of the snake.

```python
        self.circle_shape.center_point = new_point
```

> Updating the rest of the directions is very simple because the function is designed for ease of use.

```python
    def move_left(self):
        print "move left"
        self.update_direction((-1,0))

        #self.circle_shape.update_x(-Character.move_dist)    
        #Character.vel = [-Character.move_dist, 0]

    def move_up(self):
        print "move up"
        self.update_direction((0,-1))

        #self.circle_shape.update_y(-Character.move_dist)
        #Character.vel = [0, -Character.move_dist]
    
    def move_down(self):
        print "move down"
        self.update_direction((0,1))

        #self.circle_shape.update_y(Character.move_dist)
        #Character.vel = [0, Character.move_dist]

```

> Hurray! the snake head is moving around the screen again, but this time in the grid instead of by pixel. As we did with the velocity snakes from before, each time the snake head moves we want to save a `new Square` in its `body_segments`. But we don't have a square object, so lets define that first.
