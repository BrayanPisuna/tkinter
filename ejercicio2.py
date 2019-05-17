from Tkinter import *
master = Tk()
whatever_you_do = "Whatever you do will be insignificant, but itis very important that you doit.\n(Mahatma Gandhi)"
msg = Message(master, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack( )
mainloop( )