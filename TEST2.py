class Person():                 #Личность
    def __init__(self, name = 'temp', sex = 'm', age = 20, growth = 160, employment = ('working', 'false'), hobby = ('gardening', 'programming', 'false'), relationship = 50):
        self.name = name
        self.sex = sex
        self.age = age
        self.growth = growth
        self.employment = employment
        self.hobby = hobby
        self.relationship = relationship

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

class Gardening(Passive):                       #садоводство
    pass


if __name__ == '__main__':
    michelle = Person(name = 'Michelle', sex = 'f', age = 18, growth = 130, employment = ('working', 'true'), hobby = ('gardening', 'programming', 'true'))
    lena = Person(name = 'lena', sex = 'f', age = 18, growth = 165, employment = ('working', 'true'), hobby = ( 'gardening', 'programming', 'true'))

    # [0..7] = f1(l,m) = b
    # [0..33] = f(b, lena, michelle)
    # if michelle.employment == lena.employment and michelle.hobby == lena.hobby:
    #     lena.relationship = 100
    #     print('восторг, дружба = ', lena.relationship)
    # elif michelle.employment == lena.employment or michelle.hobby == lena.hobby:
    #     lena.relationship = 75
    #     print('радость, дружба = ', lena.relationship)
    # else:
    #     print('безмятежность, дружба = ', lena.relationship)

def FirstStage(michelle, interlocutor):
    a = digitize(michelle.employment)/digitize(interlocutor.employment)
    b = digitize(michelle.hobby)/digitize(interlocutor.hobby)


def digitize(str = 'workong'):
    l = list(str)
    a = 0
    for x in l: a+=ord(x)
    return a
