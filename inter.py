from tkinter import *
from emotions import *

class Face(Tk):
    def __init__(self):
        super(Face, self).__init__()

        self.emotion = Reaction()

        self.label = Label(self)
        self.label.configure(image = self.emotion.face)
        self.label.pack()

    def change_emotion(emotion = Reaction()):
        pass


if __name__ == '__main__':
    face = Face()
    face.mainloop()
