from tkinter import *

class Person():                 #Личность
    def __init__(self, name = 'temp', sex = 'm', age = 20, growth = 160, employment = 'temp', hobby = 'temp'):
        self.name = name
        self.sex = sex
        self.age = age
        self.growth = growth
        self.employment = employment
        self.hobby = hobby



class Male(Person):             #Мужчина
    def __init__(self):
        self.sex = 'm'

    def __eq__(self, obj):
        return self.sex == obj.sex

class Female(Person):           #Женщина
    def __init__(self):
        self.sex = 'f'

    def __eq__(self, obj):
        return self.sex == obj.sex

class Child(Person):            #Ребенок
    def __init__(self, age = 7):
        self.age = age

    def __eq__(self, obj):
        return obj.age < 15

class Teen(Person):             #Подросток
    def __init__(self, age = 16):
        self.age = age

    def __eq__(self, obj):
        return 14 < obj.age < 20

class Adult(Person):                         #Взрослый
    def __init__(self, age = 32):
        self.age = age

    def __eq__(self, obj):
        return 20 < obj.age < 45

class Aged(Person):                          #В возрасте
    def __init__(self, age = 50):
        self.age = age

    def __eq__(self, obj):
        return 45 < obj.age

class Growth(Person):                        #рост
    def __init__(self):
        self.growth = growth

    def __eq__(self, obj):
        return self.growth == obj.growth

class Low(Growth):                      #низкого роста
    def __init__(self, growth = 160):
        self.growth = growth

    def __eq__(self, obj):
        return  obj.growth < 165 if obj.sex == 'm' else obj.growth < 155

class Medium(Growth):                   #среднего роста
    def __init__(self, growth = 180):
        self.growth = growth

    def __eq__(self, obj):
        return  164 < obj.growth < 185 if obj.sex == 'm' else 154 < obj.growth < 170

class High(Growth):                     #высокого роста
    def __init__(self, growth = 190):
        self.growth = growth

    def __eq__(self, obj):
        return  184 < obj.growth if obj.sex == 'm' else 169 < obj.growth


class Employment(Person):                 #род деятельности
    def __init__(self, employment):
        self.employment = employment

    def __eq__(self, obj):
        return self.employment == obj.employment

class School(Employment):                     #школьник
    def __init__(self):
        self.employment = 'school'

class Student(Employment):                    #студент
    def __init__(self):
        self.employment = 'student'

class Working(Employment):                    #работающий
    def __init__(self):
        self.employment = 'working'

class Pensioner(Employment):                   #пенсионер
    def __init__(self):
        self.employment = 'pensioner'

class Unemployed(Employment):                  #безработный
    def __init__(self):
        self.employment = 'unemployed'

class Hobby(Person):                            #хобби
    def __init__(self, hobby):
        self.hobby = hobby

    def __eq__(self, obj):
        return self.hobby == obj.hobby

class Active(Hobby):                            #активные (подробнее о классификации по ссылке https://medaboutme.ru/obraz-zhizni/publikacii/stati/hobbi/kakie_byvayut_khobbi/)
    pass

class Sport(Active):
    pass                            #спорт

class Football(Sport):
    pass                          #футбол

class Basketball(Sport):
    pass                        #баскетбол

class Hockey(Sport):
    pass                            #хоккей

class Tennis(Sport):
    pass                            #теннис

class Skiing(Sport):
    pass                            #лыжи

class Dance(Active):
    pass                            #танцы

class BicycleRiding(Active):
    pass                    #езда на велосипеде

class Travelling(Active):
    pass                       #путешествовать

class Hunting(Active):
    pass                          #охота

class Fishing(Active):
    pass                          #рыболовство

class Passive(Hobby):                           #пассивные
    pass

class Music(Passive):                           #музыка
    pass

class Photographing(Passive):                   #фотографирование
    pass

class Programming(Passive):                     #программирование
    pass

class Cook(Passive):                            #кулинария
    pass

class Needlework(Passive):                      #рукоделие
    pass

class BoardGames(Passive):                      #настольные игры
    pass

class Reading(Passive):                         #чтение
    pass


class Reaction():
	def __init__(self):
		self.text = ""
		self.id = 'base'


class Base(Reaction):
	pass

class Incorporation(Reaction):				#Инкорпорация
	def __init__(self, level = 0):
		self.text = "Инкорпорация"
		self.id = 'Incorporation'

class Serenity(Incorporation):				#Инкорпорация: безмятежность(нет пнг)
	def __init__(self, level = 1):
		self.id = 'Serenity'

class Joy(Incorporation):					#Инкорпорация: радость
	def __init__(self, level = 2):
		self.id = 'Joy'

class Delight(Incorporation):				#Инкорпорация: восторг
	def __init__(self, level = 3):
		self.id = 'Delight'

class Rejection(Reaction):					#Отвержение
	def __init__(self, level = 0):
		self.id = 'Rejection'

class Boredom(Rejection):					#Отвержение: скука
	def __init__(self, level = 1):
		self.id = 'Boredom'

class Displeasure(Rejection):				#Отвержение: неудовольствие
	def __init__(self, level = 2):
		self.id = 'Displeasure'

class Disgust(Rejection):			 		#Отвержение: отвращение
	def __init__(self, level = 3):
		self.id = 'Disgust'

class Patronage(Reaction):					#Протекция
	def __init__(self, level = 0):
		self.id = 'Patronage'

class Alarm(Patronage):						#Протекция: тревога
	def __init__(self, level = 1):
		self.id = 'Alarm'

class Fear(Patronage):						#Протекция: страх
	def __init__(self, level = 2):
		self.id = 'Fear'

class Horror(Patronage):					#Протекция: ужас(нет пнг)
	def __init__(self, level = 3):
		self.id = 'Horror'

class Destruction(Reaction):				#Разрушение
	def __init__(self, level = 0):
		self.id = 'Destruction'

class Annoyance(Destruction):				#Разрушение: досада
	def __init__(self, level = 1):
		self.id = 'Annoyance'

class Spite(Destruction):					#Разрушение: злость
	def __init__(self, level = 2):
		self.id = 'Spite'

class Anger(Destruction):					#Разрушение: гнев
	def __init__(self, level = 3):
		self.id = 'Anger'

class Reproduction(Reaction): 				#Воспроизводство
	def __init__(self, level = 0):
		self.id = 'Reproduction'

class Excitation(Reproduction): 			#Воспроизводство: возбуждение
	def __init__(self, level = 1):
		self.id = 'Excitation'

class Surprise(Reproduction): 				#Воспроизводство: удивление
	def __init__(self, level = 2):
		self.id = 'Surprise'

class Amazement(Reproduction): 				#Воспроизводство: изумление
	def __init__(self, level = 3):
		self.id = 'Amazement'

class Reintegration(Reaction):				#Реинтеграция
	def __init__(self, level = 0):
		self.id = 'Reintegration'

class Sorrow(Reintegration):				#Реинтеграция: печаль
	def __init__(self, level = 1):
		self.id = 'Sorrow'

class Sadness(Reintegration):				#Реинтеграция: грусть
	def __init__(self, level = 2):
		self.id = 'Sadness'

class Grief(Reintegration):					#Реинтеграция: горе
	def __init__(self, level = 3):
		self.id = 'Grief'

class Orientation(Reaction):				#Ориентация
	def __init__(self, level = 0):
		self.id = 'Orientation'

class Interest(Orientation):				#Ориентация: интерес
	def __init__(self, level = 1):
		self.id = 'Interest'

class Expectation(Orientation):				#Ориентация: ожидание
	def __init__(self, level = 2):
		self.id = 'Expectation'

class Alertness(Orientation):				#Ориентация: настороженность
	def __init__(self, level = 3):
		self.id = 'Alertness'

class Exploration(Reaction):				#Исследование
	def __init__(self, level = 0):
		self.id = 'Exploration'

class Adoption(Exploration):				#Исследование: принятие
	def __init__(self, level = 1):
		self.id = 'Adoption'

class Trust(Exploration):					#Исследование: доверие
	def __init__(self, level = 2):
		self.id = 'Trust'

class Admiration(Exploration):				#Исследование: восхищение
	def __init__(self, level = 3):
		self.id = 'Admiration'

def firstStage(michelle, interlocutor):
    a = (digitize(michelle.employment)/digitize(interlocutor.employment)+digitize(michelle.hobby)/digitize(interlocutor.hobby))/2
    while a > 1:
        a-=1
    incorporation = a * 5
    rejection = a * 6
    patronage = a * 10
    destruction = a * 22
    reproduction = a * 15
    reintegration = a * 19
    orientation = a * 10
    exploration = a * 11
    return {incorporation: Incorporation(), rejection: Rejection(), patronage: Patronage(), destruction: Destruction(), reproduction: Reproduction(), reintegration: Reintegration(), orientation: Orientation(), exploration: Exploration()}

def secondStage(michelle, interlocutor, emo1stage):
    a = (digitize(michelle.employment)/digitize(interlocutor.employment)+digitize(michelle.hobby)/digitize(interlocutor.hobby))/2
    while a > 1:
        a-=1
    level1 = a * 20
    level2 = a * 10
    level3 = a * 22
    emotion_level = 0
    # reaction_name = emo1stage.keys()[0]
    if level1 > level2 and level1 > level3:
        emotion_level = 1
    elif level2 > level1 and level2 > level3:
        emotion_level = 2
    else: emotion_level = 3
    return emotion_level


def digitize(str):          #Преобразование кортежа в число
    a = 0
    for y in range(len(str)):
        l=list(str[y])
        for x in l: a+=ord(x)
    return a


if __name__ == '__main__':
    michelle = Person(name = 'Michelle', sex = 'f', age = 18, growth = 130, employment = ('working', 'true'), hobby = ('gardening', 'programming', 'true'))
    lena = Person(name = 'lena', sex = 'f', age = 18, growth = 165, employment = ('working', 'true'), hobby = ( 'gardening', 'programming', 'true'))
    # [0..7] = f1(l,m) = b
    # [0..33] = f(b, lena, michelle)
    x = firstStage(michelle, lena)
    emo1stage = max(x.keys())
    print(emo1stage)
    emo2stage = secondStage(michelle, lena, emo1stage)
    print(emo2stage)
