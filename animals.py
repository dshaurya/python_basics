class Things:
	pass
class Inanimate(Things):
	pass
class Animate (Things):
	pass
class Animals(Animate):
	def breathe(self):
		print('breathing')
	def move(self):
		print('moving')
	def eat_food(self):
		print('eating food')

eat_food()



class Animals(Animate):
	def breathe(self):
		print('breathing')
	def move(self):
		print('moving')
	def eat_food(self):
		print('eating food')

animals = Animals()
animals.move()
