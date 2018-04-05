from tkinter import PhotoImage

class Reaction():
	def __init__(self):
		self.text = ""
		self.id = 'base'
		self.face = PhotoImage(file =  "img/base.png")
		self.face = self.face.zoom(1, 1)
		self.face = self.face.subsample(1, 1)

	def __call__(self, reaction):
		self.face = reaction.face

	def __eq__(self, obj):
		return self.id == obj.id

class Base(Reaction):
	pass

class Incorporation(Reaction):				#Инкорпорация
	def __init__(self, level = 0):
		self.text = "Инкорпорация"
		self.id = 'Incorporation'
		self.face = PhotoImage(file =  "img/base.png")

class Serenity(Incorporation):				#Инкорпорация: безмятежность(нет пнг)
	def __init__(self, level = 1):
		self.id = 'Serenity'
		self.face = PhotoImage(file =  "img/base.png")

class Joy(Incorporation):					#Инкорпорация: радость
	def __init__(self, level = 2):
		self.id = 'Joy'
		self.face = PhotoImage(file =  "img/Incorporation/joy.png")

class Delight(Incorporation):				#Инкорпорация: восторг
	def __init__(self, level = 3):
		self.id = 'Delight'
		self.face = PhotoImage(file =  "img/Incorporation/delight.png")

class Rejection(Reaction):					#Отвержение
	def __init__(self, level = 0):
		self.id = 'Rejection'
		self.face = PhotoImage(file =  "img/base.png")

class Boredom(Rejection):					#Отвержение: скука
	def __init__(self, level = 1):
		self.id = 'Boredom'
		self.face = PhotoImage(file =  "img/Rejection/boredom.png")

class Displeasure(Rejection):				#Отвержение: неудовольствие
	def __init__(self, level = 2):
		self.id = 'Displeasure'
		self.face = PhotoImage(file =  "img/Rejection/displeasure.png")

class Disgust(Rejection):			 		#Отвержение: отвращение
	def __init__(self, level = 3):
		self.id = 'Disgust'
		self.face = PhotoImage(file =  "img/Rejection/disgust.png")

class Patronage(Reaction):					#Протекция
	def __init__(self, level = 0):
		self.id = 'Patronage'
		self.face = PhotoImage(file =  "img/base.png")

class Alarm(Patronage):						#Протекция: тревога
	def __init__(self, level = 1):
		self.id = 'Alarm'
		self.face = PhotoImage(file =  "img/Patronage/alarm.png")

class Fear(Patronage):						#Протекция: страх
	def __init__(self, level = 2):
		self.id = 'Fear'
		self.face = PhotoImage(file =  "img/Patronage/fear.png")

class Horror(Patronage):					#Протекция: ужас(нет пнг)
	def __init__(self, level = 3):
		self.id = 'Horror'
		self.face = PhotoImage(file =  "img/base.png")

class Destruction(Reaction):				#Разрушение
	def __init__(self, level = 0):
		self.id = 'Destruction'
		self.face = PhotoImage(file =  "img/base.png")

class Annoyance(Destruction):				#Разрушение: досада
	def __init__(self, level = 1):
		self.id = 'Annoyance'
		self.face = PhotoImage(file =  "img/Destruction/annoyance.png")

class Spite(Destruction):					#Разрушение: злость
	def __init__(self, level = 2):
		self.id = 'Spite'
		self.face = PhotoImage(file =  "img/Destruction/spite.png")

class Anger(Destruction):					#Разрушение: гнев
	def __init__(self, level = 3):
		self.id = 'Anger'
		self.face = PhotoImage(file =  "img/Destruction/anger.png")

class Reproduction(Reaction): 				#Воспроизводство
	def __init__(self, level = 0):
		self.id = 'Reproduction'
		self.face = PhotoImage(file =  "img/base.png")

class Excitation(Reproduction): 			#Воспроизводство: возбуждение
	def __init__(self, level = 1):
		self.id = 'Excitation'
		self.face = PhotoImage(file =  "img/Reproduction/excitation.png")

class Surprise(Reproduction): 				#Воспроизводство: удивление
	def __init__(self, level = 2):
		self.id = 'Surprise'
		self.face = PhotoImage(file =  "img/Reproduction/surprise.png")

class Amazement(Reproduction): 				#Воспроизводство: изумление
	def __init__(self, level = 3):
		self.id = 'Amazement'
		self.face = PhotoImage(file =  "img/Reproduction/amazement.png")

class Reintegration(Reaction):				#Реинтеграция
	def __init__(self, level = 0):
		self.id = 'Reintegration'
		self.face = PhotoImage(file =  "img/base.png")

class Sorrow(Reintegration):				#Реинтеграция: печаль
	def __init__(self, level = 1):
		self.id = 'Sorrow'
		self.face = PhotoImage(file =  "img/Reintegration/sorrow.png")

class Sadness(Reintegration):				#Реинтеграция: грусть
	def __init__(self, level = 2):
		self.id = 'Sadness'
		self.face = PhotoImage(file =  "img/Reintegration/sadness.png")

class Grief(Reintegration):					#Реинтеграция: горе
	def __init__(self, level = 3):
		self.id = 'Grief'
		self.face = PhotoImage(file =  "img/Reintegration/grief.png")
	    # self.face = self.face.zoom(1, 1)

class Orientation(Reaction):				#Ориентация
	def __init__(self, level = 0):
		self.id = 'Orientation'
		self.face = PhotoImage(file =  "img/base.png")

class Interest(Orientation):				#Ориентация: интерес
	def __init__(self, level = 1):
		self.id = 'Interest'
		self.face = PhotoImage(file =  "img/Orientation/interest.png")

class Expectation(Orientation):				#Ориентация: ожидание
	def __init__(self, level = 2):
		self.id = 'Expectation'
		self.face = PhotoImage(file =  "img/Orientation/expectation.png")

class Alertness(Orientation):				#Ориентация: настороженность
	def __init__(self, level = 3):
		self.id = 'Alertness'
		self.face = PhotoImage(file =  "img/Orientation/alertness.png")

class Exploration(Reaction):				#Исследование
	def __init__(self, level = 0):
		self.id = 'Exploration'
		self.face = PhotoImage(file =  "img/base.png")

class Adoption(Exploration):				#Исследование: принятие
	def __init__(self, level = 1):
		self.id = 'Adoption'
		self.face = PhotoImage(file =  "img/Exploration/adoption.png")

class Trust(Exploration):					#Исследование: доверие
	def __init__(self, level = 2):
		self.id = 'Trust'
		self.face = PhotoImage(file =  "img/Exploration/trust.png")

class Admiration(Exploration):				#Исследование: восхищение
	def __init__(self, level = 3):
		self.id = 'Admiration'
		self.face = PhotoImage(file =  "img/Exploration/admiration.png")
