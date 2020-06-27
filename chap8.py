class Things:
	pass
class Inanimate(Things):
	pass
class Animate (Things):
	pass
class Sidewalks(Inanimate):
	pass
class Animals(Animate):
	pass
class Mammals(Animals):
	pass
class Giraffes(Mammals):
	pass
class Inanimate(Things):
	pass
reginald = Giraffes()
def this_is_a_normal_function():
	print('I am a normal function')


this_is_a_normal_function()


class Animals(Animate):
	def breathe(self):
		print('breathing')
	def move(self):
		print('moving')
	def eat_food(self):
		print('eating food')

animals = Animals()
animals.move()
animals.eat_food()
class Mammals(Animals):
        def feed_young_with_milk(self):
                print('feeding young')
class Giraffes(Mammals):

        def eat_leaves_from_trees(self):
                print('eating leaves')
                
reginald = Giraffes()
harold = Giraffes()
reginald.move()
harold.eat_leaves_from_trees()
import turtle
avery = turtle.Pen()
kate = turtle.Pen()
avery.forward(50)
avery.right(90)
avery.forward(20)
kate.left(90)
kate.forward(100)
jacob = turtle.Pen()
jacob.left(180)
jacob.forward(80)
reginald = Giraffes()
reginald.move()
reginald.breathe()
reginald.eat_food()
reginald.feed_young_with_milk()
reginald.move()
class Giraffes(Mammals):
        def find_food(self):
                self.move()
                print("I've found food!")
                self.eat_food()
        def eat_leaves_from_trees(self):
                self.eat_food()
        def dance_a_jig(self):
                self.move()
                self.move()
                self.move()
                self.move()
                
reginald = Giraffes()
reginald.dance_a_jig()
class Giraffes:
        def __init__(self,spots):
                self.giraffe_spots = spots
ozwald = Giraffes(100)
gertrude = Giraffes(150)
print(ozwald.giraffe_spots)
print(gertrude.giraffe_spots)
def left_foot_forward(self):
    print('left foot forward')
def left_foot_backward(self):
    print('left foot backward')
def right_foot_backward(self):
    print('right foot forward')
def right_foot_forward(self):
    print('right foot forward')
dance = left_foot_forward lf cdeft_foot_backward right_foot_forward
reginald = Giraffes()
reginald.dance()

