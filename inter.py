from tkinter import *
from emotions import *

class Face(Tk):
    def __init__(self):
        super(Face, self).__init__()

        self.emotion = Reaction()

        self.label = Label(self)
        self.label.configure(image = self.emotion.face)
        self.label.pack()

        self.emotion_to = Incorporation()
        self.after(500, self.change_emotion)

    def change_emotion(self):
        if self.emotion == self.emotion_to:
            pass
        else :
            self.label.configure(image = self.emotion_to.face)
            self.emotion = self.emotion_to


if __name__ == '__main__':
    face = Face()
    face.mainloop()
