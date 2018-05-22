from newperson import *
import json
# from json import dump, load


    # Класс собеседника

class Interlocutor(Person):

    #

    def __str__(self):
        line = "%s\n%s\n%s\n%s\n%s\n%s\n" % (self.name,
        self.sex, self.age, self.growth,
        '; '.join(self.employment), '; '.join(self.hobby))
        return line

    # Открытие данных о собеседнике

    def opening(self):

        interlocutor = Interlocutor()
        f = open('interlocutor', 'r')
        data = json.loads(f.read())
        # for i in data:
            # print(data[i])

        for attr, value in interlocutor.__dict__.items():
            for d in data:
                if str(d) == str(attr):
                    setattr(interlocutor, attr, data[d])
        f.close()
        return interlocutor

    # Запрос на обновление информации о собеседнике

    def request(self):
        self.name = input ("Введите Ваше имя: ")
        self.sex = 'temp'
        while self.sex == 'temp':
            temp = input ("Ваш пол(м/ж): ")
            if temp == "м":
                self.sex = 'm'
            elif temp == "ж":
                self.sex = 'f'
        self.age = input ("Введите Ваш возраст: ")
        self.growth = input ("Введите Ваш рост: ")
        self.employment = (input ("Введите род Вашей деятельности(работающий, школьник, студент...): "), '; true')
        self.hobby = (input ("Введите Ваши увлечения, разделяя их точкой с запятой с пробелом: "), '; true')
        print()
        return self

    # Сохранение данных о собеседнике

    def save(self):

        f = open('interlocutor','w')
        f.write(json.dumps(self.__dict__, ensure_ascii=0, indent=4, sort_keys=1))
        f.close()

    # Вывод информации о собеседнике

    def printing(self):
        print('Имя:', self.name)
        print('Пол:', self.sex)
        print('Возраст:', self.age)
        print('Рост:', self.growth)
        print('Занятость:', self.employment)
        print('Хобби:', self.hobby)

        print(self)

def mainInterloc():
    interlocutor = Interlocutor()
    interlocutor.request()
    interlocutor.save()
    interlocutor.printing()
    interlocutor = interlocutor.opening()
    interlocutor.printing()
    return interlocutor

if __name__ == '__main__':
    mainInterloc()
