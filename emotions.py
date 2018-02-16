class Reaction():
	def __init__(self):
		self.face = "base.png"

	def __call__(self, reaction):
		self.face = reaction.face

class Incorporation(Reaction):
	def __init__(self, level = 0):
		self.face = "0.png"

class Serenity(Incorporation):
	def __init__(self, level = 1):
		self.face = "0.png"
		
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
