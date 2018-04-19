from newperson import *

    # Класс собеседника

class Interlocutor(Person):

    # Открытие данных о собеседнике

    def opening(self):

        f = open('interlocutor.txt')
        interlocutor.name = f.readline()
        interlocutor.sex = f.readline()
        interlocutor.age = f.readline()
        interlocutor.growth = f.readline()
        interlocutor.employment = f.readline()
        interlocutor.hobby = f.readline()
        f.close()


    # Запрос на обновление информации о собеседнике

    def request(self):
        interlocutor.name = input ("Введите Ваше имя: ")
        while interlocutor.sex == 'temp':
            temp = input ("Ваш пол(м/ж): ")
            if temp == "м":
                interlocutor.sex = 'm'
            elif temp == "ж":
                interlocutor.sex = 'f'
        interlocutor.age = input ("Введите Ваш возраст: ")
        interlocutor.growth = input ("Введите Ваш рост: ")
        interlocutor.employment = input ("Введите род Вашей деятельности(работающий, школьник, студент...): ")
        interlocutor.hobby = input ("Введите Ваши увлечения: ")
        return interlocutor

    # Сохранение данных о собеседнике

    def save(self):
        f = open('interlocutor.txt', 'w')
        f.write(interlocutor.name + '\n' + interlocutor.sex + '\n' + interlocutor.age + '\n' + interlocutor.growth + '\n' + interlocutor.employment + '\n' + interlocutor.hobby)
        f.close()

    # Вывод информации о собеседнике

    def printing(self):

        print('Имя:', self.name)
        print('Пол:', self.sex)
        print('Возраст:', self.age)
        print('Рост:', self.growth)
        print('Занятость:', self.employment)
        print('Хобби:', self.hobby)


if __name__ == '__main__':

    interlocutor = Interlocutor()
    interlocutor.printing()
    interlocutor.request()
    interlocutor.printing()
