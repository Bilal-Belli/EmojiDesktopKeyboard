from logging import root
from tkinter import *
from turtle import left
import emoji

root = Tk()
root.title('Emoji Keyboard')
root.iconbitmap('logo.ico')
# Designate Height and Width of our app
app_width = 550
app_height = 210
# The Height and Width of our pc screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2 ) - (app_height / 2)
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
#a9dce3
FirstBackGroung = Label(root,width="550",height="285",bg="#7689DE")
FirstBackGroung.place(x=0,y=0)
root.resizable(False,False)

frame = Frame(root, bd=5, bg="#a9dce3")
frame.pack(ipadx=5, ipady=5, padx=5, pady=5)
# U+1F600	
def enterSmile():
    textDisplay.insert(14,u'\U0001F46D')
    return
def enterd():
    textDisplay.insert(14,u'\U0001F46E')
    return

textDisplay = Entry(frame,width=82,font=("Arial", 20),textvariable=emoji)
textDisplay.pack(side=TOP)
# first line of keyboard
btn = Button(root,text='\U0001F46D',command=enterSmile,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn.place(x=5,y=70)
btn2 = Button(root,text='\U0001F46E',command=enterd,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn2.place(x=74,y=70)
btn3 = Button(root,text='\U0001F46E',command=enterd,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn3.place(x=75,y=70)
btn4 = Button(root,text='\U0001F46E',command=enterd,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn4.place(x=144,y=70)
btn5 = Button(root,text='\U0001F46E',command=enterd,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn5.place(x=215,y=70)
btn6 = Button(root,text='\U0001F46E',command=enterd,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn6.place(x=285,y=70)
btn7 = Button(root,text='\U0001F46E',command=enterd,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn7.place(x=354,y=70)
btn8 = Button(root,text='\U0001F46E',command=enterd,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn8.place(x=424,y=70)
btn9 = Button(root,text='\U0001F46E',command=enterd,width=4,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn9.place(x=492,y=70)
# second keyboad line
btn10 = Button(root,text='\U0001F46D',command=enterSmile,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn10.place(x=5,y=115)
btn11 = Button(root,text='\U0001F46E',command=enterd,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn11.place(x=74,y=115)
btn12 = Button(root,text='\U0001F46E',command=enterd,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn12.place(x=75,y=115)
btn14 = Button(root,text='\U0001F46E',command=enterd,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn14.place(x=144,y=115)
btn15 = Button(root,text='\U0001F46E',command=enterd,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn15.place(x=215,y=115)
btn16 = Button(root,text='\U0001F46E',command=enterd,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn16.place(x=285,y=115)
btn17 = Button(root,text='\U0001F46E',command=enterd,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn17.place(x=354,y=115)
btn18 = Button(root,text='\U0001F46E',command=enterd,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn18.place(x=424,y=115)
btn19 = Button(root,text='\U0001F46E',command=enterd,width=4,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn19.place(x=492,y=115)
# third keyboad line
btn20 = Button(root,text='\U0001F46D',command=enterSmile,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn20.place(x=5,y=160)
btn21 = Button(root,text='\U0001F46E',command=enterd,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn21.place(x=74,y=160)
btn22 = Button(root,text='\U0001F46E',command=enterd,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn22.place(x=75,y=160)
btn24 = Button(root,text='\U0001F46E',command=enterd,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn24.place(x=144,y=160)
btn25 = Button(root,text='\U0001F46E',command=enterd,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn25.place(x=215,y=160)
btn26 = Button(root,text='\U0001F46E',command=enterd,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn26.place(x=285,y=160)
btn27 = Button(root,text='\U0001F46E',command=enterd,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn27.place(x=354,y=160)
btn28 = Button(root,text='\U0001F46E',command=enterd,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn28.place(x=424,y=160)
btn29 = Button(root,text='\U0001F46E',command=enterd,width=4,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn29.place(x=492,y=160)


# hover the buttons effect
# def hoverActive(boton, color1, color2, color3):
# 	boton.configure(bg=color1)
# 	def fuera(e):
# 		boton.configure(bg=color1)
# 	def dentro(e):
# 		boton.configure(bg=color2)
# 	def activo(e):
# 		boton.configure(activebackground=color3)
# 	boton.bind("<Enter>", dentro)
# 	boton.bind("<Leave>", fuera)
# 	boton.bind("<ButtonPress-1>", activo)

root.mainloop()