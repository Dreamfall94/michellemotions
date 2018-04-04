from newperson import *
from tkinter import *
from emotions import *




class Michelle(Tk, Person):                 # Описание Мишель
    def __init__(self, name = 'Michelle', sex = 'f',
        age = 18, growth = 130, employment = ('working', 'true'),
        hobby = ('gardening', 'programming', 'true'), relationship = 0.7):

        super().__init__()

        # Параметры

        self.name = name
        self.sex = sex
        self.age = age
        self.growth = growth
        self.employment = employment
        self.hobby = hobby
        self.relationship = relationship

        # Исправить!!!!!

        self.lena = Person(name = 'lena', sex = 'f', age = 18,
            growth = 165, employment = ('working', 'true'),
            hobby = ( 'gardening', 'programming', 'true'))

        # Формирование эмоции

        self.emotion = Reaction()
        self.label = Label(self)
        self.label.configure(image = self.emotion.face)
        self.label.pack()
        self.after(500, self.loop)

        # Метод смены эмоции

    def change_emotion(self, emo):

        if self.emotion == emo:
            pass
        else:
            self.label.configure(image = emo.face)
            self.emotion = emo

    # Первая стадия: Определение 1 из 8 лепестков модели Плутчика

    def firstStage(self):

        a = (self.digitize(self.employment)/self.digitize(self.lena.employment)+
            self.digitize(self.hobby)/self.digitize(self.lena.hobby))/2

        while a > 1:
            a-=1
        incorporation = a * 5
        rejection = a * 6
        patronage = a * 70
        destruction = a * 10
        reproduction = a * 100
        reintegration = a * 190
        orientation = a * 20
        exploration = a * 110
        return {incorporation: 'Incorporation()', rejection: 'Rejection()',
            patronage: 'Patronage()', destruction: 'Destruction()',
            reproduction: 'Reproduction()', reintegration: 'Reintegration()',
            orientation: 'Orientation()', exploration: 'Exploration()'}

    # Вторая стадия: Определение конкретной эмоции

    def secondStage(self, emo1stage):

        a = (self.digitize(self.employment)/self.digitize(self.lena.employment)+
            self.digitize(self.hobby)/self.digitize(self.lena.hobby))/2


        while a > 1:
            a-=1
        # level1 = a * 20
        # level2 = a * 10
        level3 = a * 16
        if emo1stage == 'Incorporation()':
            return Delight()
        if emo1stage == 'Rejection()':
            return Disgust()
        if emo1stage == 'Patronage()':
            return Horror()
        if emo1stage == 'Destruction()':
            return Anger()
        if emo1stage == 'Reproduction()':
            return Amazement()
        if emo1stage == 'Reintegration()':
            return Grief()
        if emo1stage == 'Orientation()':
            return Alertness()
        if emo1stage == 'Exploration()':
            return Admiration()
        return


    # Преобразование кортежа в число

    def digitize(self, str):
        a = 0
        for y in range(len(str)):
            l=list(str[y])
            for x in l: a+=ord(x)
        return a

    # Основная часть программы

    def loop(self):

        x = self.firstStage()                           # Записываем словарь в переменную x
        emo1stage = max(x)                              # Записываем max значение словаря
        direction=x.get(emo1stage)                      # Определяем 1 из 8 лепестков модели Плутчика

        y = self.secondStage(direction)     # Узнаем эмоцию
        programPause = input("Press the <ENTER> key to continue...")
        self.change_emotion(y)                          # Смена эмоции
        self.after(500, self.loop)                      # Интервал цикла




if __name__ == '__main__':
    face = Michelle()
    face.attributes('-fullscreen', 1)
    face.configure(background="white")

    face.mainloop()
