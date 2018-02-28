    # class Person():                             #Личность
    #     def __init__(self,
    #                         sex = 'm',
    #                         age = 20,
    #                         growth = 178,
    #                         physique = 'medium',
    #                         employment = 'student',
    #                         emstate = 'funny',
    #                         hair = 'short',
    #                         hobby = 'football',
    #                         appearance = 'red shirt'):
    #         self.age = age                      #возраст
    #         self.growth = growth                #рост
    #         self.physique = physique            #телосложение
    #         self.employment = employment        #род деятельности
    #         self.emstate = emstate              #эмоциональное состояние
    #         self.hair = hair                    #волосы
    #         self.hobby = hobby                  #хобби
    #         self.appearance = appearance        #внешний вид


class Person():                 #Личность
    def __init__(self, name = 'temp', sex = 'm', age = 20, growth = 160):
        self.name = name
        self.sex = sex
        self.age = age
        self.growth = growth

    def __eq__(self, obj):
        print(self.name, obj.name)
        return self.sex == obj.sex and self.age == obj.age and self.growth == obj.growth



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

class Growth(Person):                       #рост
    def __init__(self):
        self.growth = growth

    def __eq__(self, obj):
        return self.growth == obj.growth

class LowMale(Growth):                      #низкий мужчина
    def __init__(self, growth = 160):
        self.growth = growth

    def __eq__(self, obj):
        return obj.growth < 165

class MediumMale(Growth):                   #мужчина среднего роста
    def __init__(self, growth = 180):
        self.growth = growth

    def __eq__(self, obj):
        return 164 < obj.growth < 185

class HighMale(Growth):                     #высокий мужчина
    def __init__(self, growth = 190):
        self.growth = growth

    def __eq__(self, obj):
        return 184 < obj.growth

class LowFemale(Growth):                      #низкая женщина
    def __init__(self, growth = 155):
        self.growth = growth

    def __eq__(self, obj):
        return obj.growth < 155

class MediumFemale(Growth):                   #женщина среднего роста
    def __init__(self, growth = 160):
        self.growth = growth

    def __eq__(self, obj):
        return 154 < obj.growth < 170

class HighFemale(Growth):                     #высокая женщина
    def __init__(self, growth = 180):
        self.growth = growth

    def __eq__(self, obj):
        return 169 < obj.growth

if __name__ == '__main__':
    lena = Person(name = 'lena', sex = 'm', age = 18, growth = 165)
    # vlad = Person(name = 'vlad', sex = 'm', age = 18, growth = 135)
    # sonya = Person(name = 'sonya', sex = 'f', age = 18, growth = 165)
    f = Female()
    t = Teen()
    l = MediumFemale()
    print(f == lena, t == lena, l == lena)
    # print (lena == vlad)
    # print (lena == sonya)
