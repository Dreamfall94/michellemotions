from math import e, exp
class Person():                 #Личность
    def __init__(self, name = 'temp', sex = 'temp', age = 20, growth = 160,
    employment = ['working', 'false'], hobby = ['gardening', 'programming',
    'false'], relationship = 0.5):
        self.name = name
        self.sex = sex
        self.age = age
        self.growth = growth
        self.employment = employment
        self.hobby = hobby
        self.relationship = relationship



if __name__ == '__main__':
    lena = Person(name = 'lena', sex = 'm', age = int(input('Возраст: ')),
    growth = 160, employment = 'student')
    # arr = []
    # i=0
    # while i < 5:
    #     arr.append(i)
    #     i+=1
    # print (arr)


    ages = [12.5, 17.5, 22.5, 67.5]
    feelAges = []
    maxFeel = 0
    for elem in ages:
        feelAges.append(e**(-((elem-int(lena.age))/15)**2))
        if maxFeel < e**(-((elem-int(lena.age))/15)**2):
            maxFeel = e**(-((elem-int(lena.age))/15)**2)
    feelAges.insert(0, maxFeel)
    print(feelAges)

    # print(e**(-((200-b)/4)**2), b1)
    # print(e**(-((200-c)/4)**2), c1)
