from logging import root
from tkinter import *
import emoji

root = Tk()
frame = Frame(root)
frame.pack()
# U+1F600	
def enterSmile():
    textDisplay.insert(14,u'\U0001F46D')
    return

textDisplay = Entry(frame,textvariable=emoji)
textDisplay.pack(side=TOP)
btn = Button(root,text='\U0001F46D',command=enterSmile)
btn.pack()


root.mainloop()