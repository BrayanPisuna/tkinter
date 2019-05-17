from Tkinter import *

class App:
    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="salir", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="entrar", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def write_slogan(self):
       print ("Estamos aprendiendo a usar Tkinter!")
root = Tk()
app = App(root)
root.mainloop()