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


* Diff of code [here](https://github.com/bellcodo/creating-cliq/commit/a79a4b4b51b99102cd5fc12842fabaf615340b6f)
