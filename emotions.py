from tkinter import PhotoImage

class Reaction():
	def __init__(self):
		self.id = 'base'
		self.face = PhotoImage(file =  "img/base.png")

	def __call__(self, reaction):
		self.face = reaction.face

	def __eq__(self, obj):
		return self.id == obj.id

class Base(Reaction):
	pass

class Incorporation(Reaction):
	def __init__(self, level = 0):
		self.id = 'Incorporation'
		self.face = PhotoImage(file =  "img/Incorporation/Incorporation1.png")

class Serenity(Incorporation):
	def __init__(self, level = 1):
		self.id = 'Serenity'
		self.face = PhotoImage(file =  "img/Incorporation/Incorporation2.png")

class Rejection(Reaction):
	def __init__(self, level = 0):
		self.face = "0.png"

class Patronage(Reaction):
	def __init__(self, level = 0):
		self.face = "0.png"

class Destruction(Reaction):
	def __init__(self, level = 0):
		self.face = "0.png"

class Reproduction(Reaction):
	def __init__(self, level = 0):
		self.face = "0.png"

class Reintegration(Reaction):
	def __init__(self, level = 0):
		self.face = "0.png"

class Orientation(Reaction):
	def __init__(self, level = 0):
		self.face = "0.png"

class Exploration(Reaction):
	def __init__(self, level = 0):
		self.face = "0.png"
