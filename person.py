from tkinter import *


class Person():                 #Личность
    pass

class Male(Person):             #Мужчина
    pass

class Female(Person):           #Женщина
    pass

class Child(Person):            #Ребенок
    pass

class Teen(Person):             #Подросток
    pass

class Adult(Person):            #Взрослый
    pass

class Aged(Person):             #В возрасте
    pass

class Boy(Male, Child):         #Мальчик
    pass

class Guy(Male, Teen):          #Парень
    pass

class Man(Male, Adult):         #Мужчина
    pass

class OldMan(Male, Aged):       #Мужчина в возрасте
    pass

class Girlie(Female, Child):    #Девочка
    pass

class Girl(Female, Teen):       #Девушка
    pass

class Woman(Female, Adult):     #Женщина
    pass

class OldWoman(Female, Aged):   #Женщина в возрасте
    pass

#lena = Girl(shhirt = kletchataya)
