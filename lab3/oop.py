times_to_make_sound = 6
class Animal(object):
	def __init__(self,sound,name,age,favorite_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.favorite_color = favorite_color
	def eat(self, food):
			print("Yummy!!"+self.name+" is eating"+food)
	def description(self):
			print(self.name+" is " + str(self.age) + " years old and loves the color "+self.favorite_color)
	def make_sound(self, sound):
		print(self.sound*times_to_make_sound)
unicorn  = Animal("ahhhhh ", "love", 999999999999,"pink")
unicorn.eat(" rainbows")
unicorn.description()
unicorn.make_sound("ahhhhh")
class person (object):
	def __init__(self,name,age,city,gender,hair_color,favorite_food,sleep_time):B
		self.name = name
		self.age = age 
		self.city = city
		self.gender = gender 
		self.hair_color = hair_color
		self.favorite_food = favorite_food
		self.sleep_time = sleep_time
	def eat_favorite_food(self,favorite_food):
		print("my favorite food is"+self.favorite_food)
	def sleeping(self, sleep_time):
		print("every night I sleep "+str(self.sleep_time)+" hours")


Person1 = person("Sarah",15,"Jerusalem","female","gold"," pizza",18)
Person1.eat_favorite_food("Pizza")
Person1.sleeping(18)


