from tkinter import *


class Person():                 #Личность
    def __init__(self, sex = 'm', age = 20):
        self.sex = sex
        self.age = age

    def __eq__(self, obj):
        print(self.age, obj.age)
        return self.sex == obj.sex and self.age == obj.age


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
    def __init__(self, age = 17):
        self.age = age

    def __eq__(self, obj):
        return 14 < obj.age < 20

class Adult(Person):            #Взрослый
    def __init__(self, age = 32):
        self.age = age

    def __eq__(self, obj):
        return 20 < obj.age < 45

class Aged(Person):             #В возрасте
    def __init__(self, age = 50):
        self.age = age

    def __eq__(self, obj):
        return 45 < obj.age

# class Boy(Male, Child):         #Мальчик
#     pass
#
# class Guy(Male, Teen):          #Парень
#     pass
#
# class Man(Male, Adult):         #Мужчина
#     pass
#
# class OldMan(Male, Aged):       #Мужчина в возрасте
#     pass
#
# class Girlie(Female, Child):    #Девочка
#     pass
#
# class Girl(Female, Teen):       #Девушка
#     pass
#
# class Woman(Female, Adult):     #Женщина
#     pass
#
# class OldWoman(Female, Aged):   #Женщина в возрасте
#     pass

#lena = Girl(shhirt = kletchataya)
if __name__ == '__main__':
    lena = Person(sex = 'm', age = 18)
    f = Female()
    t = Teen()
    print(f == lena, lena == t)
