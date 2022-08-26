from logging import root
from tkinter import *
from turtle import left
import emoji

global lastIndex
lastIndex=24
listOfEmojis=['\U0001F60E ', '\U0001F913 ', '\U0001F9D0 ', '\U0001F626 ', '\U0001F627 ', '\U0001F628 ', '\U0001F630 ', '\U0001F625 ', '\U0001F622 ', '\U0001F62D ', '\U0001F631 ', '\U0001F616 ', '\U0001F623 ', '\U0001F61E ', '\U0001F613 ', '\U0001F629 ', '\U0001F62B ', '\U0001F971 ', '\U0001F624 ', '\U0001F621 ', '\U0001F620 ', '\U0001F92C ', '\U0001F608 ', '\U0001F47F ', '\U0001F480 ', '\U0001F62E ', '\U0001F62F ', '\U0001F632 ', '\U0001F633 ', '\U0001F97A ', '\U0001F4A9 ', '\U0001F921 ', '\U0001F479 ', '\U0001F47A ', '\U0001F47B ', '\U0001F47D ', '\U0001F47E ', '\U0001F916 ', '\U0001F63A ', '\U0001F638 ', '\U0001F639 ', '\U0001F63B ', '\U0001F63C ', '\U0001F63D ', '\U0001F640 ', '\U0001F63F ', '\U0001F63E ', '\U0001F648 ', '\U0001F649 ', '\U0001F64A ', '\U0001F48C ', '\U0001F498 ', '\U0001F49D ', '\U0001F496 ', '\U0001F497 ', '\U0001F493 ', '\U0001F49E ', '\U0001F495 ', '\U0001F49F ','\U0001F9E1 ', '\U0001F49B ', '\U0001F49A ', '\U0001F499 ', '\U0001F48B ', '\U0001F4AF ', '\U0001F4A2 ', '\U0001F4A5 ', '\U0001F4AB ', '\U0001F4A6 ', '\U0001F4A8 ', '\U0001F573 ', '\U0001F4AC ', '\U0001F441 ', '\U0001F5E8 ', '\U0001F5E8 ', '\U0001F5EF ', '\U0001F5EF ', '\U0001F4AD ', '\U0001F4A4 ', '\U0001F44B ', '\U0001F44B ', '\U0001F44B ', '\U0001F44B ', '\U0001F44B ', '\U0001F91A ', '\U0001F91A ', '\U0001F91A ', '\U0001F91A ', '\U0001F91A ', '\U0001F590 ', '\U0001F590 ', '\U0001F590 ', '\U0001F590 ', '\U0001F590 ', '\U0001F590 ', '\U0001F91E ', '\U0001F91E ', '\U0001F91E ', '\U0001F91E ', '\U0001F91E ', '\U0001F91F ', '\U0001F91F ', '\U0001F91F ', '\U0001F91F ', '\U0001F91F ', '\U0001F918 ', '\U0001F918 ', '\U0001F918 ', '\U0001F918 ', '\U0001F918 ', '\U0001F919 ', '\U0001F919 ', '\U0001F919 ', '\U0001F919 ', '\U0001F919 ', '\U0001F44D ', '\U0001F44D ', '\U0001F44D ', '\U0001F44D ', '\U0001F44D ', '\U0001F44E ', '\U0001F44E ', '\U0001F44E ', '\U0001F44E ', '\U0001F44E ', '\U0001F44A ', '\U0001F44A ', '\U0001F44A ', '\U0001F44A ', '\U0001F44A ', '\U0001F91B ', '\U0001F91B ', '\U0001F91B ', '\U0001F91B ', '\U0001F91B ', '\U0001F91C ', '\U0001F91C ', '\U0001F91C ', '\U0001F91C ', '\U0001F91C ', '\U0001F44F ', '\U0001F44F ', '\U0001F44F ', '\U0001F44F ', '\U0001F91D ', '\U0001F91D ', '\U0001F91D ', '\U0001F64F ', '\U0001F64F ', '\U0001F64F ', '\U0001F4AA ', '\U0001F4AA ', '\U0001F4AA ', '\U0001F4AA ', '\U0001F4AA ', '\U0001F9BE ', '\U0001F9BF ', '\U0001F9B5 ', '\U0001F9B5 ', '\U0001F9B6 ', '\U0001F9B6 ', '\U0001F442 ', '\U0001F442 ', '\U0001F9BB ', '\U0001F9BB ', '\U0001F443 ', '\U0001F443 ', '\U0001F443 ', '\U0001F9E0 ', '\U0001F9B7 ', '\U0001F9B4 ', '\U0001F440 ', '\U0001F441 ', '\U0001F445 ', '\U0001F444 ', '\U0001F347 ', '\U0001F348 ', '\U0001F349 ', '\U0001F34A ', '\U0001F34B ', '\U0001F34C ', '\U0001F34D ', '\U0001F96D ', '\U0001F34E ', '\U0001F34F ', '\U0001F350 ', '\U0001F351 ', '\U0001F352 ', '\U0001F353 ', '\U0001F95D ', '\U0001F345 ', '\U0001F965 ', '\U0001F951 ', '\U0001F346 ', '\U0001F954 ', '\U0001F955 ', '\U0001F33D ', '\U0001F336 ', '\U0001F336 ', '\U0001F952 ', '\U0001F96C ', '\U0001F966 ', '\U0001F9C4 ', '\U0001F9C5 ', '\U0001F95C ', '\U0001FAD8 ', '\U0001F330 ', '\U0001F96F ', '\U0001F95E ', '\U0001F9C7 ', '\U0001F9C0 ', '\U0001F356 ', '\U0001F357 ', '\U0001F969 ', '\U0001F953 ', '\U0001F354 ', '\U0001F35F ', '\U0001F355 ', '\U0001F32D ', '\U0001F96A ', '\U0001F32E ', '\U0001F358 ', '\U0001F359 ', '\U0001F35A ', '\U0001F35B ', '\U0001F35C ', '\U0001F35D ', '\U0001F360 ', '\U0001F362 ', '\U0001F363 ', '\U0001F364 ', '\U0001F365 ', '\U0001F96E ', '\U0001F361 ', '\U0001F95F ', '\U0001F960 ', '\U0001F961 ', '\U0001F366 ', '\U0001F367 ', '\U0001F368 ', '\U0001F369 ', '\U0001F36A ', '\U0001F382 ', '\U0001F370 ', '\U0001F9C1 ', '\U0001F967 ', '\U0001F36B ', '\U0001F36C ', '\U0001F36D ', '\U0001F36E ', '\U0001F3E0 ', '\U0001F3E1 ', '\U0001F3E2 ', '\U0001F3E3 ', '\U0001F3E4 ', '\U0001F3E5 ', '\U0001F3E6 ', '\U0001F3E8 ', '\U0001F3E9 ', '\U0001F3EA ', '\U0001F3EB ', '\U0001F3EC ', '\U0001F3ED ', '\U0001F3EF ', '\U0001F3F0 ', '\U0001F492 ', '\U0001F691 ', '\U0001F692 ', '\U0001F693 ', '\U0001F694 ', '\U0001F695 ', '\U0001F696 ', '\U0001F697 ', '\U0001F698 ', '\U0001F699 ', '\U0001F94E ', '\U0001F3C0 ', '\U0001F3D0 ', '\U0001F3C8 ', '\U0001F3C9 ', '\U0001F3BE ', '\U0001F94F ', '\U0001F3B3 ', '\U0001F3CF ', '\U0001F3D1 ', '\U0001F3D2 ', '\U0001F94D ', '\U0001F3D3 ', '\U0001F3F8 ', '\U0001F94A ', '\U0001F94B ', '\U0001F945 ',  '\U0001F3A3 ', '\U0001F93F ', '\U0001F3BD ', '\U0001F3BF ', '\U0001F6F7 ', '\U0001F94C ', '\U0001F3AF ', '\U0001FA80 ', '\U0001FA81 ', '\U0001F52B ', '\U0001F3B1 ', '\U0001F52E ', '\U0001F3AE ', '\U0001F453 ', '\U0001F576 ', '\U0001F576 ', '\U0001F97D ', '\U0001F97C ', '\U0001F9BA ', '\U0001F454 ', '\U0001F455 ', '\U0001F456 ', '\U0001F9E3 ', '\U0001F9E4 ', '\U0001F9E5 ', '\U0001F9E6 ', '\U0001F457 ', '\U0001F458 ', '\U0001F97B ', '\U0001FA71 ', '\U0001FA72 ', '\U0001FA73 ', '\U0001F459 ', '\U0001F45A ',  '\U0001F4FF ', '\U0001F484 ', '\U0001F48D ', '\U0001F48E ', '\U0001F451 ', '\U0001F452 ', '\U0001F3A9 ', '\U0001F393 ', '\U0001F9E2 ', '\U0001F507 ', '\U0001F508 ', '\U0001F509 ', '\U0001F50A ', '\U0001F4E2 ', '\U0001F4E3 ', '\U0001F4EF ', '\U0001F514 ', '\U0001F515 ', '\U0001F3BC ', '\U0001F3B5 ', '\U0001F3B6 ', '\U0001F399 ', '\U0001F399 ', '\U0001F39A ', '\U0001F39A ', '\U0001F39B ', '\U0001F39B ', '\U0001F3A4 ', '\U0001F3A7 ', '\U0001F4FB ', '\U0001F4F1 ', '\U0001F4F2 ',  '\U0001F4DE ', '\U0001F4DF ', '\U0001F4E0 ', '\U0001F39E ', '\U0001F39E ', '\U0001F4FD ', '\U0001F4FD ', '\U0001F3AC ', '\U0001F4FA ', '\U0001F4F7 ', '\U0001F4F8 ', '\U0001F4F9 ', '\U0001F4FC ', '\U0001F50D ', '\U0001F50E ', '\U0001F56F ', '\U0001F56F ', '\U0001F4A1 ', '\U0001F526 ', '\U0001F534 ', '\U0001F7E0 ', '\U0001F7E1 ', '\U0001F7E2 ', '\U0001F535 ', '\U0001F7E3 ', '\U0001F7E4 ',  '\U0001F7E5 ', '\U0001F7E7 ', '\U0001F7E8 ', '\U0001F7E9 ', '\U0001F7E6 ', '\U0001F7EA ', '\U0001F7EB ',  '\U0001F1E9 ']
listOfFunctions=['enter1F60E', 'enter1F913 ', 'enter1F9D0 ', 'enter1F626 ', 'enter1F627 ', 'enter1F628 ', 'enter1F630 ', 'enter1F625 ', 'enter1F622 ', 'enter1F62D ', 'enter1F631 ', 'enter1F616 ', 'enter1F623 ', 'enter1F61E ', 'enter1F613 ', 'enter1F629 ', 'enter1F62B ', 'enter1F971 ', 'enter1F624 ', 'enter1F621 ', 'enter1F620 ', 'enter1F92C ', 'enter1F608 ', 'enter1F47F ', 'enter1F480 ','enter1F62E ', 'enter1F62F ', 'enter1F632 ', 'enter1F633 ', 'enter1F97A ', 'enter1F4A9 ', 'enter1F921 ', 'enter1F479 ', 'enter1F47A ', 'enter1F47B ', 'enter1F47D ', 'enter1F47E ', 'enter1F916 ', 'enter1F63A ', 'enter1F638 ', 'enter1F639 ', 'enter1F63B ', 'enter1F63C ', 'enter1F63D ', 'enter1F640 ', 'enter1F63F ', 'enter1F63E ', 'enter1F648 ', 'enter1F649 ', 'enter1F64A ', 'enter1F48C ', 'enter1F498 ', 'enter1F49D ', 'enter1F496 ', 'enter1F497 ', 'enter1F493 ', 'enter1F49E ', 'enter1F495 ', 'enter1F49F ', 'enter1F9E1 ', 'enter1F49B ', 'enter1F49A ', 'enter1F499 ', 'enter1F48B ', 'enter1F4AF ', 'enter1F4A2 ', 'enter1F4A5 ', 'enter1F4AB ', 'enter1F4A6 ', 'enter1F4A8 ', 'enter1F573 ', 'enter1F4AC ', 'enter1F441 ', 'enter1F5E8 ', 'enter1F5E8 ', 'enter1F5EF ', 'enter1F5EF ', 'enter1F4AD ', 'enter1F4A4 ', 'enter1F44B ', 'enter1F44B ', 'enter1F44B ', 'enter1F44B ', 'enter1F44B ', 'enter1F91A ', 'enter1F91A ', 'enter1F91A ', 'enter1F91A ', 'enter1F91A ', 'enter1F590 ', 'enter1F590 ', 'enter1F590 ', 'enter1F590 ', 'enter1F590 ', 'enter1F590 ', 'enter1F91E ', 'enter1F91E ', 'enter1F91E ', 'enter1F91E ', 'enter1F91E ', 'enter1F91F ', 'enter1F91F ', 'enter1F91F ', 'enter1F91F ', 'enter1F91F ', 'enter1F918 ', 'enter1F918 ', 'enter1F918 ', 'enter1F918 ', 'enter1F918 ', 'enter1F919 ', 'enter1F919 ', 'enter1F919 ', 'enter1F919 ', 'enter1F919 ', 'enter1F44D ', 'enter1F44D ', 'enter1F44D ', 'enter1F44D ', 'enter1F44D ', 'enter1F44E ', 'enter1F44E ', 'enter1F44E ', 'enter1F44E ', 'enter1F44E ', 'enter1F44A ', 'enter1F44A ', 'enter1F44A ', 'enter1F44A ', 'enter1F44A ', 'enter1F91B ', 'enter1F91B ', 'enter1F91B ', 'enter1F91B ', 'enter1F91B ', 'enter1F91C ', 'enter1F91C ', 'enter1F91C ', 'enter1F91C ', 'enter1F91C ', 'enter1F44F ', 'enter1F44F ', 'enter1F44F ', 'enter1F44F ', 'enter1F91D ', 'enter1F91D ', 'enter1F91D ', 'enter1F64F ', 'enter1F64F ', 'enter1F64F ', 'enter1F4AA ', 'enter1F4AA ', 'enter1F4AA ', 'enter1F4AA ', 'enter1F4AA ', 'enter1F9BE ', 'enter1F9BF ', 'enter1F9B5 ', 'enter1F9B5 ', 'enter1F9B6 ', 'enter1F9B6 ', 'enter1F442 ', 'enter1F442 ', 'enter1F9BB ', 'enter1F9BB ', 'enter1F443 ', 'enter1F443 ', 'enter1F443 ', 'enter1F9E0 ', 'enter1F9B7 ', 'enter1F9B4 ', 'enter1F440 ', 'enter1F441 ', 'enter1F445 ', 'enter1F444 ', 'enter1F347 ', 'enter1F348 ', 'enter1F349 ', 'enter1F34A ', 'enter1F34B ', 'enter1F34C ', 'enter1F34D ', 'enter1F96D ', 'enter1F34E ', 'enter1F34F ', 'enter1F350 ', 'enter1F351 ', 'enter1F352 ', 'enter1F353 ', 'enter1F95D ', 'enter1F345 ', 'enter1F965 ', 'enter1F951 ', 'enter1F346 ', 'enter1F954 ', 'enter1F955 ', 'enter1F33D ', 'enter1F336 ', 'enter1F336 ', 'enter1F952 ', 'enter1F96C ', 'enter1F966 ', 'enter1F9C4 ', 'enter1F9C5 ', 'enter1F95C ', 'enter1FAD8 ', 'enter1F330 ', 'enter1F96F ', 'enter1F95E ', 'enter1F9C7 ', 'enter1F9C0 ', 'enter1F356 ', 'enter1F357 ', 'enter1F969 ', 'enter1F953 ', 'enter1F354 ', 'enter1F35F ', 'enter1F355 ', 'enter1F32D ', 'enter1F96A ', 'enter1F32E ', 'enter1F358 ', 'enter1F359 ', 'enter1F35A ', 'enter1F35B ', 'enter1F35C ', 'enter1F35D ', 'enter1F360 ', 'enter1F362 ', 'enter1F363 ', 'enter1F364 ', 'enter1F365 ', 'enter1F96E ', 'enter1F361 ', 'enter1F95F ', 'enter1F960 ', 'enter1F961 ', 'enter1F366 ', 'enter1F367 ', 'enter1F368 ', 'enter1F369 ', 'enter1F36A ', 'enter1F382 ', 'enter1F370 ', 'enter1F9C1 ', 'enter1F967 ', 'enter1F36B ', 'enter1F36C ', 'enter1F36D ', 'enter1F36E ', 'enter1F3E0 ', 'enter1F3E1 ', 'enter1F3E2 ', 'enter1F3E3 ', 'enter1F3E4 ', 'enter1F3E5 ', 'enter1F3E6 ', 'enter1F3E8 ', 'enter1F3E9 ', 'enter1F3EA ', 'enter1F3EB ', 'enter1F3EC ', 'enter1F3ED ', 'enter1F3EF ', 'enter1F3F0 ', 'enter1F492 ', 'enter1F691 ', 'enter1F692 ', 'enter1F693 ', 'enter1F694 ', 'enter1F695 ', 'enter1F696 ', 'enter1F697 ', 'enter1F698 ', 'enter1F699 ',  'enter1F94E ', 'enter1F3C0 ', 'enter1F3D0 ', 'enter1F3C8 ', 'enter1F3C9 ', 'enter1F3BE ', 'enter1F94F ', 'enter1F3B3 ', 'enter1F3CF ', 'enter1F3D1 ', 'enter1F3D2 ', 'enter1F94D ', 'enter1F3D3 ', 'enter1F3F8 ', 'enter1F94A ', 'enter1F94B ', 'enter1F945 ',  'enter1F3A3 ', 'enter1F93F ', 'enter1F3BD ', 'enter1F3BF ', 'enter1F6F7 ', 'enter1F94C ', 'enter1F3AF ', 'enter1FA80 ', 'enter1FA81 ', 'enter1F52B ', 'enter1F3B1 ', 'enter1F52E ', 'enter1F3AE ', 'enter1F453 ', 'enter1F576 ', 'enter1F576 ', 'enter1F97D ', 'enter1F97C ', 'enter1F9BA ', 'enter1F454 ', 'enter1F455 ', 'enter1F456 ', 'enter1F9E3 ', 'enter1F9E4 ', 'enter1F9E5 ', 'enter1F9E6 ', 'enter1F457 ', 'enter1F458 ', 'enter1F97B ', 'enter1FA71 ', 'enter1FA72 ', 'enter1FA73 ', 'enter1F459 ', 'enter1F45A ', 'enter1F4FF ', 'enter1F484 ', 'enter1F48D ', 'enter1F48E ', 'enter1F451 ', 'enter1F452 ', 'enter1F3A9 ', 'enter1F393 ', 'enter1F9E2 ', 'enter1F507 ', 'enter1F508 ', 'enter1F509 ', 'enter1F50A ', 'enter1F4E2 ', 'enter1F4E3 ', 'enter1F4EF ', 'enter1F514 ', 'enter1F515 ', 'enter1F3BC ', 'enter1F3B5 ', 'enter1F3B6 ', 'enter1F399 ', 'enter1F399 ', 'enter1F39A ', 'enter1F39A ', 'enter1F39B ', 'enter1F39B ', 'enter1F3A4 ', 'enter1F3A7 ', 'enter1F4FB ', 'enter1F4F1 ', 'enter1F4F2 ',  'enter1F4DE ', 'enter1F4DF ', 'enter1F4E0 ', 'enter1F39E ', 'enter1F39E ', 'enter1F4FD ', 'enter1F4FD ', 'enter1F3AC ', 'enter1F4FA ', 'enter1F4F7 ', 'enter1F4F8 ', 'enter1F4F9 ', 'enter1F4FC ', 'enter1F50D ', 'enter1F50E ', 'enter1F56F ', 'enter1F56F ', 'enter1F4A1 ', 'enter1F526 ', 'enter1F534 ', 'enter1F7E0 ', 'enter1F7E1 ', 'enter1F7E2 ', 'enter1F535 ', 'enter1F7E3 ', 'enter1F7E4 ',  'enter1F7E5 ', 'enter1F7E7 ', 'enter1F7E8 ', 'enter1F7E9 ', 'enter1F7E6 ', 'enter1F7EA ', 'enter1F7EB ',  'enter1F1E9 ', ]

root = Tk()
root.title('Emoji Keyboard')
root.iconbitmap('logo.ico')
app_width = 550
app_height = 240
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2 ) - (app_height / 2)
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
FirstBackGroung = Label(root,width="550",height="285",bg="#7689DE")
FirstBackGroung.place(x=0,y=0)
root.resizable(False,False)

frame = Frame(root, bd=5, bg="#a9dce3")#for text output
frame.pack(ipadx=5, ipady=5, padx=5, pady=5)
textDisplay = Entry(frame,width=82,font=("Arial", 20),textvariable=emoji)
textDisplay.pack(side=TOP)
# 3 lines of keyboard (first open of application)
def enter1F600 ():
    textDisplay.insert(0,u'\U0001F600 ')
    return
btn1=Button(root,text='\U0001F600 ',command=enter1F600 ,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn1.place(x=5,y=70)
def enter1F603 ():
    textDisplay.insert(0,u'\U0001F603 ')
    return
btn2=Button(root,text='\U0001F603 ',command=enter1F603 ,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn2.place(x=74,y=70)
def enter1F604 ():
    textDisplay.insert(0,u'\U0001F604 ')
    return
btn3=Button(root,text='\U0001F604 ',command=enter1F604 ,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn3.place(x=144,y=70)
def enter1F601 ():
    textDisplay.insert(0,u'\U0001F601 ')
    return
btn4=Button(root,text='\U0001F601 ',command=enter1F601 ,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn4.place(x=215,y=70)
def enter1F606 ():
    textDisplay.insert(0,u'\U0001F606 ')
    return
btn5=Button(root,text='\U0001F606 ',command=enter1F606 ,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn5.place(x=285,y=70)
def enter1F605 ():
    textDisplay.insert(0,u'\U0001F605 ')
    return
btn6=Button(root,text='\U0001F605 ',command=enter1F605 ,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn6.place(x=354,y=70)
def enter1F923 ():
    textDisplay.insert(0,u'\U0001F923 ')
    return
btn7=Button(root,text='\U0001F923 ',command=enter1F923 ,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn7.place(x=424,y=70)
def enter1F602 ():
    textDisplay.insert(0,u'\U0001F602 ')
    return
btn8=Button(root,text='\U0001F602 ',command=enter1F602 ,width=4,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn8.place(x=492,y=70)
def enter1F642 ():
    textDisplay.insert(0,u'\U0001F642 ')
    return
btn9=Button(root,text='\U0001F642 ',command=enter1F642 ,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn9.place(x=5,y=115)
def enter1F643 ():
    textDisplay.insert(0,u'\U0001F643 ')
    return
btn10=Button(root,text='\U0001F643 ',command=enter1F643 ,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn10.place(x=74,y=115)
def enter1F609 ():
    textDisplay.insert(0,u'\U0001F609 ')
    return
btn11=Button(root,text='\U0001F609 ',command=enter1F609 ,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn11.place(x=144,y=115)
def enter1F60A ():
    textDisplay.insert(0,u'\U0001F60A ')
    return
btn12=Button(root,text='\U0001F60A ',command=enter1F60A ,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn12.place(x=215,y=115)
def enter1F607 ():
    textDisplay.insert(0,u'\U0001F607 ')
    return
btn13=Button(root,text='\U0001F607 ',command=enter1F607 ,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn13.place(x=285,y=115)
def enter1F92A ():
    textDisplay.insert(0,u'\U0001F92A ')
    return
btn14=Button(root,text='\U0001F92A ',command=enter1F92A ,width=4,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn14.place(x=492,y=160)
def enter1F970 ():
    textDisplay.insert(0,u'\U0001F970 ')
    return
btn15=Button(root,text='\U0001F970 ',command=enter1F970 ,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn15.place(x=354,y=115)
def enter1F60D ():
    textDisplay.insert(0,u'\U0001F60D ')
    return
btn16=Button(root,text='\U0001F60D ',command=enter1F60D ,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn16.place(x=424,y=115)
def enter1F929 ():
    textDisplay.insert(0,u'\U0001F929 ')
    return
btn17=Button(root,text='\U0001F929 ',command=enter1F929 ,width=4,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn17.place(x=492,y=115)
def enter1F618 ():
    textDisplay.insert(0,u'\U0001F618 ')
    return
btn18=Button(root,text='\U0001F618 ',command=enter1F618 ,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn18.place(x=5,y=160)
def enter1F617 ():
    textDisplay.insert(0,u'\U0001F617 ')
    return
btn19=Button(root,text='\U0001F617 ',command=enter1F617 ,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn19.place(x=74,y=160)
def enter1F61A ():
    textDisplay.insert(0,u'\U0001F61A ')
    return
btn20=Button(root,text='\U0001F61A ',command=enter1F61A ,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn20.place(x=144,y=160)
def enter1F619 ():
    textDisplay.insert(0,u'\U0001F619 ')
    return
btn21=Button(root,text='\U0001F619 ',command=enter1F619 ,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn21.place(x=215,y=160)
def enter1F61C ():
    textDisplay.insert(0,u'\U0001F61C ')
    return
btn22=Button(root,text='\U0001F61C ',command=enter1F61C ,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn22.place(x=424,y=160)
def enter1F60B ():
    textDisplay.insert(0,u'\U0001F60B ')
    return
btn23=Button(root,text='\U0001F60B ',command=enter1F60B ,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn23.place(x=285,y=160)
def enter1F61B ():
    textDisplay.insert(0,u'\U0001F61B ')
    return
btn24=Button(root,text='\U0001F61B ',command=enter1F61B ,width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn24.place(x=354,y=160)
# other functions for others emojis thats are not showed on first open of application
def enter1F60E ():
    textDisplay.insert(0,u'\U0001F60E ')
    return
def enter1F913 ():
    textDisplay.insert(0,u'\U0001F913 ')
    return
def enter1F9D0 ():
    textDisplay.insert(0,u'\U0001F9D0 ')
    return
def enter1F626 ():
    textDisplay.insert(0,u'\U0001F626 ')
    return
def enter1F627 ():
    textDisplay.insert(0,u'\U0001F627 ')
    return
def enter1F628 ():
    textDisplay.insert(0,u'\U0001F628 ')
    return
def enter1F630 ():
    textDisplay.insert(0,u'\U0001F630 ')
    return
def enter1F625 ():
    textDisplay.insert(0,u'\U0001F625 ')
    return
def enter1F622 ():
    textDisplay.insert(0,u'\U0001F622 ')
    return
def enter1F62D ():
    textDisplay.insert(0,u'\U0001F62D ')
    return
def enter1F631 ():
    textDisplay.insert(0,u'\U0001F631 ')
    return
def enter1F616 ():
    textDisplay.insert(0,u'\U0001F616 ')
    return
def enter1F623 ():
    textDisplay.insert(0,u'\U0001F623 ')
    return
def enter1F61E ():
    textDisplay.insert(0,u'\U0001F61E ')
    return
def enter1F613 ():
    textDisplay.insert(0,u'\U0001F613 ')
    return
def enter1F629 ():
    textDisplay.insert(0,u'\U0001F629 ')
    return
def enter1F62B ():
    textDisplay.insert(0,u'\U0001F62B ')
    return
def enter1F971 ():
    textDisplay.insert(0,u'\U0001F971 ')
    return
def enter1F624 ():
    textDisplay.insert(0,u'\U0001F624 ')
    return
def enter1F621 ():
    textDisplay.insert(0,u'\U0001F621 ')
    return
def enter1F620 ():
    textDisplay.insert(0,u'\U0001F620 ')
    return
def enter1F92C ():
    textDisplay.insert(0,u'\U0001F92C ')
    return
def enter1F608 ():
    textDisplay.insert(0,u'\U0001F608 ')
    return
def enter1F47F ():
    textDisplay.insert(0,u'\U0001F47F ')
    return
def enter1F480 ():
    textDisplay.insert(0,u'\U0001F480 ')
    return
def enter1F62E ():
    textDisplay.insert(0,u'\U0001F62E ')
    return
def enter1F62F ():
    textDisplay.insert(0,u'\U0001F62F ')
    return
def enter1F632 ():
    textDisplay.insert(0,u'\U0001F632 ')
    return
def enter1F633 ():
    textDisplay.insert(0,u'\U0001F633 ')
    return
def enter1F97A ():
    textDisplay.insert(0,u'\U0001F97A ')
    return
def enter1F4A9 ():
    textDisplay.insert(0,u'\U0001F4A9 ')
    return
def enter1F921 ():
    textDisplay.insert(0,u'\U0001F921 ')
    return
def enter1F479 ():
    textDisplay.insert(0,u'\U0001F479 ')
    return
def enter1F47A ():
    textDisplay.insert(0,u'\U0001F47A ')
    return
def enter1F47B ():
    textDisplay.insert(0,u'\U0001F47B ')
    return
def enter1F47D ():
    textDisplay.insert(0,u'\U0001F47D ')
    return
def enter1F47E ():
    textDisplay.insert(0,u'\U0001F47E ')
    return
def enter1F916 ():
    textDisplay.insert(0,u'\U0001F916 ')
    return
def enter1F63A ():
    textDisplay.insert(0,u'\U0001F63A ')
    return
def enter1F638 ():
    textDisplay.insert(0,u'\U0001F638 ')
    return
def enter1F639 ():
    textDisplay.insert(0,u'\U0001F639 ')
    return
def enter1F63B ():
    textDisplay.insert(0,u'\U0001F63B ')
    return
def enter1F63C ():
    textDisplay.insert(0,u'\U0001F63C ')
    return
def enter1F63D ():
    textDisplay.insert(0,u'\U0001F63D ')
    return
def enter1F640 ():
    textDisplay.insert(0,u'\U0001F640 ')
    return
def enter1F63F ():
    textDisplay.insert(0,u'\U0001F63F ')
    return
def enter1F63E ():
    textDisplay.insert(0,u'\U0001F63E ')
    return
def enter1F648 ():
    textDisplay.insert(0,u'\U0001F648 ')
    return
def enter1F649 ():
    textDisplay.insert(0,u'\U0001F649 ')
    return
def enter1F64A ():
    textDisplay.insert(0,u'\U0001F64A ')
    return
def enter1F48C ():
    textDisplay.insert(0,u'\U0001F48C ')
    return
def enter1F498 ():
    textDisplay.insert(0,u'\U0001F498 ')
    return
def enter1F49D ():
    textDisplay.insert(0,u'\U0001F49D ')
    return
def enter1F496 ():
    textDisplay.insert(0,u'\U0001F496 ')
    return
def enter1F497 ():
    textDisplay.insert(0,u'\U0001F497 ')
    return
def enter1F493 ():
    textDisplay.insert(0,u'\U0001F493 ')
    return
def enter1F49E ():
    textDisplay.insert(0,u'\U0001F49E ')
    return
def enter1F495 ():
    textDisplay.insert(0,u'\U0001F495 ')
    return
def enter1F49F ():
    textDisplay.insert(0,u'\U0001F49F ')
    return
def enter1F9E1 ():
    textDisplay.insert(0,u'\U0001F9E1 ')
    return
def enter1F49B ():
    textDisplay.insert(0,u'\U0001F49B ')
    return
def enter1F49A ():
    textDisplay.insert(0,u'\U0001F49A ')
    return
def enter1F499 ():
    textDisplay.insert(0,u'\U0001F499 ')
    return
def enter1F48B ():
    textDisplay.insert(0,u'\U0001F48B ')
    return
def enter1F4AF ():
    textDisplay.insert(0,u'\U0001F4AF ')
    return
def enter1F4A2 ():
    textDisplay.insert(0,u'\U0001F4A2 ')
    return
def enter1F4A5 ():
    textDisplay.insert(0,u'\U0001F4A5 ')
    return
def enter1F4AB ():
    textDisplay.insert(0,u'\U0001F4AB ')
    return
def enter1F4A6 ():
    textDisplay.insert(0,u'\U0001F4A6 ')
    return
def enter1F4A8 ():
    textDisplay.insert(0,u'\U0001F4A8 ')
    return
def enter1F573 ():
    textDisplay.insert(0,u'\U0001F573 ')
    return
def enter1F4AC ():
    textDisplay.insert(0,u'\U0001F4AC ')
    return
def enter1F441 ():
    textDisplay.insert(0,u'\U0001F441 ')
    return
def enter1F5E8 ():
    textDisplay.insert(0,u'\U0001F5E8 ')
    return
def enter1F5E8 ():
    textDisplay.insert(0,u'\U0001F5E8 ')
    return
def enter1F5EF ():
    textDisplay.insert(0,u'\U0001F5EF ')
    return
def enter1F5EF ():
    textDisplay.insert(0,u'\U0001F5EF ')
    return
def enter1F4AD ():
    textDisplay.insert(0,u'\U0001F4AD ')
    return
def enter1F4A4 ():
    textDisplay.insert(0,u'\U0001F4A4 ')
    return
def enter1F44B ():
    textDisplay.insert(0,u'\U0001F44B ')
    return
def enter1F44B ():
    textDisplay.insert(0,u'\U0001F44B ')
    return
def enter1F44B ():
    textDisplay.insert(0,u'\U0001F44B ')
    return
def enter1F44B ():
    textDisplay.insert(0,u'\U0001F44B ')
    return
def enter1F44B ():
    textDisplay.insert(0,u'\U0001F44B ')
    return
def enter1F91A ():
    textDisplay.insert(0,u'\U0001F91A ')
    return
def enter1F91A ():
    textDisplay.insert(0,u'\U0001F91A ')
    return
def enter1F91A ():
    textDisplay.insert(0,u'\U0001F91A ')
    return
def enter1F91A ():
    textDisplay.insert(0,u'\U0001F91A ')
    return
def enter1F91A ():
    textDisplay.insert(0,u'\U0001F91A ')
    return
def enter1F590 ():
    textDisplay.insert(0,u'\U0001F590 ')
    return
def enter1F590 ():
    textDisplay.insert(0,u'\U0001F590 ')
    return
def enter1F590 ():
    textDisplay.insert(0,u'\U0001F590 ')
    return
def enter1F590 ():
    textDisplay.insert(0,u'\U0001F590 ')
    return
def enter1F590 ():
    textDisplay.insert(0,u'\U0001F590 ')
    return
def enter1F590 ():
    textDisplay.insert(0,u'\U0001F590 ')
    return
def enter1F91E ():
    textDisplay.insert(0,u'\U0001F91E ')
    return
def enter1F91E ():
    textDisplay.insert(0,u'\U0001F91E ')
    return
def enter1F91E ():
    textDisplay.insert(0,u'\U0001F91E ')
    return
def enter1F91E ():
    textDisplay.insert(0,u'\U0001F91E ')
    return
def enter1F91E ():
    textDisplay.insert(0,u'\U0001F91E ')
    return
def enter1F91F ():
    textDisplay.insert(0,u'\U0001F91F ')
    return
def enter1F91F ():
    textDisplay.insert(0,u'\U0001F91F ')
    return
def enter1F91F ():
    textDisplay.insert(0,u'\U0001F91F ')
    return
def enter1F91F ():
    textDisplay.insert(0,u'\U0001F91F ')
    return
def enter1F91F ():
    textDisplay.insert(0,u'\U0001F91F ')
    return
def enter1F918 ():
    textDisplay.insert(0,u'\U0001F918 ')
    return
def enter1F918 ():
    textDisplay.insert(0,u'\U0001F918 ')
    return
def enter1F918 ():
    textDisplay.insert(0,u'\U0001F918 ')
    return
def enter1F918 ():
    textDisplay.insert(0,u'\U0001F918 ')
    return
def enter1F918 ():
    textDisplay.insert(0,u'\U0001F918 ')
    return
def enter1F919 ():
    textDisplay.insert(0,u'\U0001F919 ')
    return
def enter1F919 ():
    textDisplay.insert(0,u'\U0001F919 ')
    return
def enter1F919 ():
    textDisplay.insert(0,u'\U0001F919 ')
    return
def enter1F919 ():
    textDisplay.insert(0,u'\U0001F919 ')
    return
def enter1F919 ():
    textDisplay.insert(0,u'\U0001F919 ')
    return
def enter1F44D ():
    textDisplay.insert(0,u'\U0001F44D ')
    return
def enter1F44D ():
    textDisplay.insert(0,u'\U0001F44D ')
    return
def enter1F44D ():
    textDisplay.insert(0,u'\U0001F44D ')
    return
def enter1F44D ():
    textDisplay.insert(0,u'\U0001F44D ')
    return
def enter1F44D ():
    textDisplay.insert(0,u'\U0001F44D ')
    return
def enter1F44E ():
    textDisplay.insert(0,u'\U0001F44E ')
    return
def enter1F44E ():
    textDisplay.insert(0,u'\U0001F44E ')
    return
def enter1F44E ():
    textDisplay.insert(0,u'\U0001F44E ')
    return
def enter1F44E ():
    textDisplay.insert(0,u'\U0001F44E ')
    return
def enter1F44E ():
    textDisplay.insert(0,u'\U0001F44E ')
    return
def enter1F44A ():
    textDisplay.insert(0,u'\U0001F44A ')
    return
def enter1F44A ():
    textDisplay.insert(0,u'\U0001F44A ')
    return
def enter1F44A ():
    textDisplay.insert(0,u'\U0001F44A ')
    return
def enter1F44A ():
    textDisplay.insert(0,u'\U0001F44A ')
    return
def enter1F91B ():
    textDisplay.insert(0,u'\U0001F91B ')
    return
def enter1F91B ():
    textDisplay.insert(0,u'\U0001F91B ')
    return
def enter1F91B ():
    textDisplay.insert(0,u'\U0001F91B ')
    return
def enter1F91B ():
    textDisplay.insert(0,u'\U0001F91B ')
    return
def enter1F91B ():
    textDisplay.insert(0,u'\U0001F91B ')
    return
def enter1F91C ():
    textDisplay.insert(0,u'\U0001F91C ')
    return
def enter1F91C ():
    textDisplay.insert(0,u'\U0001F91C ')
    return
def enter1F91C ():
    textDisplay.insert(0,u'\U0001F91C ')
    return
def enter1F91C ():
    textDisplay.insert(0,u'\U0001F91C ')
    return
def enter1F91C ():
    textDisplay.insert(0,u'\U0001F91C ')
    return
def enter1F44F ():
    textDisplay.insert(0,u'\U0001F44F ')
    return
def enter1F44F ():
    textDisplay.insert(0,u'\U0001F44F ')
    return
def enter1F44F ():
    textDisplay.insert(0,u'\U0001F44F ')
    return
def enter1F44F ():
    textDisplay.insert(0,u'\U0001F44F ')
    return
def enter1F91D ():
    textDisplay.insert(0,u'\U0001F91D ')
    return
def enter1F91D ():
    textDisplay.insert(0,u'\U0001F91D ')
    return
def enter1F91D ():
    textDisplay.insert(0,u'\U0001F91D ')
    return
def enter1F64F ():
    textDisplay.insert(0,u'\U0001F64F ')
    return
def enter1F64F ():
    textDisplay.insert(0,u'\U0001F64F ')
    return
def enter1F64F ():
    textDisplay.insert(0,u'\U0001F64F ')
    return
def enter1F4AA ():
    textDisplay.insert(0,u'\U0001F4AA ')
    return
def enter1F4AA ():
    textDisplay.insert(0,u'\U0001F4AA ')
    return
def enter1F4AA ():
    textDisplay.insert(0,u'\U0001F4AA ')
    return
def enter1F4AA ():
    textDisplay.insert(0,u'\U0001F4AA ')
    return
def enter1F4AA ():
    textDisplay.insert(0,u'\U0001F4AA ')
    return
def enter1F9BE ():
    textDisplay.insert(0,u'\U0001F9BE ')
    return
def enter1F9BF ():
    textDisplay.insert(0,u'\U0001F9BF ')
    return
def enter1F9B5 ():
    textDisplay.insert(0,u'\U0001F9B5 ')
    return
def enter1F9B5 ():
    textDisplay.insert(0,u'\U0001F9B5 ')
    return
def enter1F9B6 ():
    textDisplay.insert(0,u'\U0001F9B6 ')
    return
def enter1F9B6 ():
    textDisplay.insert(0,u'\U0001F9B6 ')
    return
def enter1F442 ():
    textDisplay.insert(0,u'\U0001F442 ')
    return
def enter1F442 ():
    textDisplay.insert(0,u'\U0001F442 ')
    return
def enter1F9BB ():
    textDisplay.insert(0,u'\U0001F9BB ')
    return
def enter1F9BB ():
    textDisplay.insert(0,u'\U0001F9BB ')
    return
def enter1F443 ():
    textDisplay.insert(0,u'\U0001F443 ')
    return
def enter1F443 ():
    textDisplay.insert(0,u'\U0001F443 ')
    return
def enter1F443 ():
    textDisplay.insert(0,u'\U0001F443 ')
    return
def enter1F9E0 ():
    textDisplay.insert(0,u'\U0001F9E0 ')
    return
def enter1F9B7 ():
    textDisplay.insert(0,u'\U0001F9B7 ')
    return
def enter1F9B4 ():
    textDisplay.insert(0,u'\U0001F9B4 ')
    return
def enter1F440 ():
    textDisplay.insert(0,u'\U0001F440 ')
    return
def enter1F441 ():
    textDisplay.insert(0,u'\U0001F441 ')
    return
def enter1F445 ():
    textDisplay.insert(0,u'\U0001F445 ')
    return
def enter1F444 ():
    textDisplay.insert(0,u'\U0001F444 ')
    return
def enter1F347 ():
    textDisplay.insert(0,u'\U0001F347 ')
    return
def enter1F348 ():
    textDisplay.insert(0,u'\U0001F348 ')
    return
def enter1F349 ():
    textDisplay.insert(0,u'\U0001F349 ')
    return
def enter1F34A ():
    textDisplay.insert(0,u'\U0001F34A ')
    return
def enter1F34B ():
    textDisplay.insert(0,u'\U0001F34B ')
    return
def enter1F34C ():
    textDisplay.insert(0,u'\U0001F34C ')
    return
def enter1F34D ():
    textDisplay.insert(0,u'\U0001F34D ')
    return
def enter1F96D ():
    textDisplay.insert(0,u'\U0001F96D ')
    return
def enter1F34E ():
    textDisplay.insert(0,u'\U0001F34E ')
    return
def enter1F34F ():
    textDisplay.insert(0,u'\U0001F34F ')
    return
def enter1F350 ():
    textDisplay.insert(0,u'\U0001F350 ')
    return
def enter1F351 ():
    textDisplay.insert(0,u'\U0001F351 ')
    return
def enter1F352 ():
    textDisplay.insert(0,u'\U0001F352 ')
    return
def enter1F353 ():
    textDisplay.insert(0,u'\U0001F353 ')
    return
def enter1F95D ():
    textDisplay.insert(0,u'\U0001F95D ')
    return
def enter1F345 ():
    textDisplay.insert(0,u'\U0001F345 ')
    return
def enter1F965 ():
    textDisplay.insert(0,u'\U0001F965 ')
    return
def enter1F951 ():
    textDisplay.insert(0,u'\U0001F951 ')
    return
def enter1F346 ():
    textDisplay.insert(0,u'\U0001F346 ')
    return
def enter1F954 ():
    textDisplay.insert(0,u'\U0001F954 ')
    return
def enter1F955 ():
    textDisplay.insert(0,u'\U0001F955 ')
    return
def enter1F33D ():
    textDisplay.insert(0,u'\U0001F33D ')
    return
def enter1F336 ():
    textDisplay.insert(0,u'\U0001F336 ')
    return
def enter1F336 ():
    textDisplay.insert(0,u'\U0001F336 ')
    return
def enter1F952 ():
    textDisplay.insert(0,u'\U0001F952 ')
    return
def enter1F96C ():
    textDisplay.insert(0,u'\U0001F96C ')
    return
def enter1F966 ():
    textDisplay.insert(0,u'\U0001F966 ')
    return
def enter1F9C4 ():
    textDisplay.insert(0,u'\U0001F9C4 ')
    return
def enter1F9C5 ():
    textDisplay.insert(0,u'\U0001F9C5 ')
    return
def enter1F95C ():
    textDisplay.insert(0,u'\U0001F95C ')
    return
def enter1FAD8 ():
    textDisplay.insert(0,u'\U0001FAD8 ')
    return
def enter1F330 ():
    textDisplay.insert(0,u'\U0001F330 ')
    return
def enter1F96F ():
    textDisplay.insert(0,u'\U0001F96F ')
    return
def enter1F95E ():
    textDisplay.insert(0,u'\U0001F95E ')
    return
def enter1F9C7 ():
    textDisplay.insert(0,u'\U0001F9C7 ')
    return
def enter1F9C0 ():
    textDisplay.insert(0,u'\U0001F9C0 ')
    return
def enter1F356 ():
    textDisplay.insert(0,u'\U0001F356 ')
    return
def enter1F357 ():
    textDisplay.insert(0,u'\U0001F357 ')
    return
def enter1F969 ():
    textDisplay.insert(0,u'\U0001F969 ')
    return
def enter1F953 ():
    textDisplay.insert(0,u'\U0001F953 ')
    return
def enter1F354 ():
    textDisplay.insert(0,u'\U0001F354 ')
    return
def enter1F35F ():
    textDisplay.insert(0,u'\U0001F35F ')
    return
def enter1F355 ():
    textDisplay.insert(0,u'\U0001F355 ')
    return
def enter1F32D ():
    textDisplay.insert(0,u'\U0001F32D ')
    return
def enter1F96A ():
    textDisplay.insert(0,u'\U0001F96A ')
    return
def enter1F32E ():
    textDisplay.insert(0,u'\U0001F32E ')
    return
def enter1F358 ():
    textDisplay.insert(0,u'\U0001F358 ')
    return
def enter1F359 ():
    textDisplay.insert(0,u'\U0001F359 ')
    return
def enter1F35A ():
    textDisplay.insert(0,u'\U0001F35A ')
    return
def enter1F35B ():
    textDisplay.insert(0,u'\U0001F35B ')
    return
def enter1F35C ():
    textDisplay.insert(0,u'\U0001F35C ')
    return
def enter1F35D ():
    textDisplay.insert(0,u'\U0001F35D ')
    return
def enter1F360 ():
    textDisplay.insert(0,u'\U0001F360 ')
    return
def enter1F362 ():
    textDisplay.insert(0,u'\U0001F362 ')
    return
def enter1F363 ():
    textDisplay.insert(0,u'\U0001F363 ')
    return
def enter1F364 ():
    textDisplay.insert(0,u'\U0001F364 ')
    return
def enter1F365 ():
    textDisplay.insert(0,u'\U0001F365 ')
    return
def enter1F96E ():
    textDisplay.insert(0,u'\U0001F96E ')
    return
def enter1F361 ():
    textDisplay.insert(0,u'\U0001F361 ')
    return
def enter1F95F ():
    textDisplay.insert(0,u'\U0001F95F ')
    return
def enter1F960 ():
    textDisplay.insert(0,u'\U0001F960 ')
    return
def enter1F961 ():
    textDisplay.insert(0,u'\U0001F961 ')
    return
def enter1F366 ():
    textDisplay.insert(0,u'\U0001F366 ')
    return
def enter1F367 ():
    textDisplay.insert(0,u'\U0001F367 ')
    return
def enter1F368 ():
    textDisplay.insert(0,u'\U0001F368 ')
    return
def enter1F369 ():
    textDisplay.insert(0,u'\U0001F369 ')
    return
def enter1F36A ():
    textDisplay.insert(0,u'\U0001F36A ')
    return
def enter1F382 ():
    textDisplay.insert(0,u'\U0001F382 ')
    return
def enter1F370 ():
    textDisplay.insert(0,u'\U0001F370 ')
    return
def enter1F9C1 ():
    textDisplay.insert(0,u'\U0001F9C1 ')
    return
def enter1F967 ():
    textDisplay.insert(0,u'\U0001F967 ')
    return
def enter1F36B ():
    textDisplay.insert(0,u'\U0001F36B ')
    return
def enter1F36C ():
    textDisplay.insert(0,u'\U0001F36C ')
    return
def enter1F36D ():
    textDisplay.insert(0,u'\U0001F36D ')
    return
def enter1F36E ():
    textDisplay.insert(0,u'\U0001F36E ')
    return
def enter1F3E0 ():
    textDisplay.insert(0,u'\U0001F3E0 ')
    return
def enter1F3E1 ():
    textDisplay.insert(0,u'\U0001F3E1 ')
    return
def enter1F3E2 ():
    textDisplay.insert(0,u'\U0001F3E2 ')
    return
def enter1F3E3 ():
    textDisplay.insert(0,u'\U0001F3E3 ')
    return
def enter1F3E4 ():
    textDisplay.insert(0,u'\U0001F3E4 ')
    return
def enter1F3E5 ():
    textDisplay.insert(0,u'\U0001F3E5 ')
    return
def enter1F3E6 ():
    textDisplay.insert(0,u'\U0001F3E6 ')
    return
def enter1F3E8 ():
    textDisplay.insert(0,u'\U0001F3E8 ')
    return
def enter1F3E9 ():
    textDisplay.insert(0,u'\U0001F3E9 ')
    return
def enter1F3EA ():
    textDisplay.insert(0,u'\U0001F3EA ')
    return
def enter1F3EB ():
    textDisplay.insert(0,u'\U0001F3EB ')
    return
def enter1F3EC ():
    textDisplay.insert(0,u'\U0001F3EC ')
    return
def enter1F3ED ():
    textDisplay.insert(0,u'\U0001F3ED ')
    return
def enter1F3EF ():
    textDisplay.insert(0,u'\U0001F3EF ')
    return
def enter1F3F0 ():
    textDisplay.insert(0,u'\U0001F3F0 ')
    return
def enter1F492 ():
    textDisplay.insert(0,u'\U0001F492 ')
    return
def enter1F691 ():
    textDisplay.insert(0,u'\U0001F691 ')
    return
def enter1F692 ():
    textDisplay.insert(0,u'\U0001F692 ')
    return
def enter1F693 ():
    textDisplay.insert(0,u'\U0001F693 ')
    return
def enter1F694 ():
    textDisplay.insert(0,u'\U0001F694 ')
    return
def enter1F695 ():
    textDisplay.insert(0,u'\U0001F695 ')
    return
def enter1F696 ():
    textDisplay.insert(0,u'\U0001F696 ')
    return
def enter1F697 ():
    textDisplay.insert(0,u'\U0001F697 ')
    return
def enter1F698 ():
    textDisplay.insert(0,u'\U0001F698 ')
    return
def enter1F699 ():
    textDisplay.insert(0,u'\U0001F699 ')
    return
def enter1F94E ():
    textDisplay.insert(0,u'\U0001F94E ')
    return
def enter1F3C0 ():
    textDisplay.insert(0,u'\U0001F3C0 ')
    return
def enter1F3D0 ():
    textDisplay.insert(0,u'\U0001F3D0 ')
    return
def enter1F3C8 ():
    textDisplay.insert(0,u'\U0001F3C8 ')
    return
def enter1F3C9 ():
    textDisplay.insert(0,u'\U0001F3C9 ')
    return
def enter1F3BE ():
    textDisplay.insert(0,u'\U0001F3BE ')
    return
def enter1F94F ():
    textDisplay.insert(0,u'\U0001F94F ')
    return
def enter1F3B3 ():
    textDisplay.insert(0,u'\U0001F3B3 ')
    return
def enter1F3CF ():
    textDisplay.insert(0,u'\U0001F3CF ')
    return
def enter1F3D1 ():
    textDisplay.insert(0,u'\U0001F3D1 ')
    return
def enter1F3D2 ():
    textDisplay.insert(0,u'\U0001F3D2 ')
    return
def enter1F94D ():
    textDisplay.insert(0,u'\U0001F94D ')
    return
def enter1F3D3 ():
    textDisplay.insert(0,u'\U0001F3D3 ')
    return
def enter1F3F8 ():
    textDisplay.insert(0,u'\U0001F3F8 ')
    return
def enter1F94A ():
    textDisplay.insert(0,u'\U0001F94A ')
    return
def enter1F94B ():
    textDisplay.insert(0,u'\U0001F94B ')
    return
def enter1F945 ():
    textDisplay.insert(0,u'\U0001F945 ')
    return
def enter1F3A3 ():
    textDisplay.insert(0,u'\U0001F3A3 ')
    return
def enter1F93F ():
    textDisplay.insert(0,u'\U0001F93F ')
    return
def enter1F3BD ():
    textDisplay.insert(0,u'\U0001F3BD ')
    return
def enter1F3BF ():
    textDisplay.insert(0,u'\U0001F3BF ')
    return
def enter1F6F7 ():
    textDisplay.insert(0,u'\U0001F6F7 ')
    return
def enter1F94C ():
    textDisplay.insert(0,u'\U0001F94C ')
    return
def enter1F3AF ():
    textDisplay.insert(0,u'\U0001F3AF ')
    return
def enter1FA80 ():
    textDisplay.insert(0,u'\U0001FA80 ')
    return
def enter1FA81 ():
    textDisplay.insert(0,u'\U0001FA81 ')
    return
def enter1F52B ():
    textDisplay.insert(0,u'\U0001F52B ')
    return
def enter1F3B1 ():
    textDisplay.insert(0,u'\U0001F3B1 ')
    return
def enter1F52E ():
    textDisplay.insert(0,u'\U0001F52E ')
    return
def enter1F3AE ():
    textDisplay.insert(0,u'\U0001F3AE ')
    return
def enter1F453 ():
    textDisplay.insert(0,u'\U0001F453 ')
    return
def enter1F576 ():
    textDisplay.insert(0,u'\U0001F576 ')
    return
def enter1F576 ():
    textDisplay.insert(0,u'\U0001F576 ')
    return
def enter1F97D ():
    textDisplay.insert(0,u'\U0001F97D ')
    return
def enter1F97C ():
    textDisplay.insert(0,u'\U0001F97C ')
    return
def enter1F9BA ():
    textDisplay.insert(0,u'\U0001F9BA ')
    return
def enter1F454 ():
    textDisplay.insert(0,u'\U0001F454 ')
    return
def enter1F455 ():
    textDisplay.insert(0,u'\U0001F455 ')
    return
def enter1F456 ():
    textDisplay.insert(0,u'\U0001F456 ')
    return
def enter1F9E3 ():
    textDisplay.insert(0,u'\U0001F9E3 ')
    return
def enter1F9E4 ():
    textDisplay.insert(0,u'\U0001F9E4 ')
    return
def enter1F9E5 ():
    textDisplay.insert(0,u'\U0001F9E5 ')
    return
def enter1F9E6 ():
    textDisplay.insert(0,u'\U0001F9E6 ')
    return
def enter1F457 ():
    textDisplay.insert(0,u'\U0001F457 ')
    return
def enter1F458 ():
    textDisplay.insert(0,u'\U0001F458 ')
    return
def enter1F97B ():
    textDisplay.insert(0,u'\U0001F97B ')
    return
def enter1FA71 ():
    textDisplay.insert(0,u'\U0001FA71 ')
    return
def enter1FA72 ():
    textDisplay.insert(0,u'\U0001FA72 ')
    return
def enter1FA73 ():
    textDisplay.insert(0,u'\U0001FA73 ')
    return
def enter1F459 ():
    textDisplay.insert(0,u'\U0001F459 ')
    return
def enter1F45A ():
    textDisplay.insert(0,u'\U0001F45A ')
    return
def enter1F4FF ():
    textDisplay.insert(0,u'\U0001F4FF ')
    return
def enter1F484 ():
    textDisplay.insert(0,u'\U0001F484 ')
    return
def enter1F48D ():
    textDisplay.insert(0,u'\U0001F48D ')
    return
def enter1F48E ():
    textDisplay.insert(0,u'\U0001F48E ')
    return
def enter1F451 ():
    textDisplay.insert(0,u'\U0001F451 ')
    return
def enter1F452 ():
    textDisplay.insert(0,u'\U0001F452 ')
    return
def enter1F3A9 ():
    textDisplay.insert(0,u'\U0001F3A9 ')
    return
def enter1F393 ():
    textDisplay.insert(0,u'\U0001F393 ')
    return
def enter1F9E2 ():
    textDisplay.insert(0,u'\U0001F9E2 ')
    return
def enter1F507 ():
    textDisplay.insert(0,u'\U0001F507 ')
    return
def enter1F508 ():
    textDisplay.insert(0,u'\U0001F508 ')
    return
def enter1F509 ():
    textDisplay.insert(0,u'\U0001F509 ')
    return
def enter1F50A ():
    textDisplay.insert(0,u'\U0001F50A ')
    return
def enter1F4E2 ():
    textDisplay.insert(0,u'\U0001F4E2 ')
    return
def enter1F4E3 ():
    textDisplay.insert(0,u'\U0001F4E3 ')
    return
def enter1F4EF ():
    textDisplay.insert(0,u'\U0001F4EF ')
    return
def enter1F514 ():
    textDisplay.insert(0,u'\U0001F514 ')
    return
def enter1F515 ():
    textDisplay.insert(0,u'\U0001F515 ')
    return
def enter1F3BC ():
    textDisplay.insert(0,u'\U0001F3BC ')
    return
def enter1F3B5 ():
    textDisplay.insert(0,u'\U0001F3B5 ')
    return
def enter1F3B6 ():
    textDisplay.insert(0,u'\U0001F3B6 ')
    return
def enter1F399 ():
    textDisplay.insert(0,u'\U0001F399 ')
    return
def enter1F399 ():
    textDisplay.insert(0,u'\U0001F399 ')
    return
def enter1F39A ():
    textDisplay.insert(0,u'\U0001F39A ')
    return
def enter1F39A ():
    textDisplay.insert(0,u'\U0001F39A ')
    return
def enter1F39B ():
    textDisplay.insert(0,u'\U0001F39B ')
    return
def enter1F39B ():
    textDisplay.insert(0,u'\U0001F39B ')
    return
def enter1F3A4 ():
    textDisplay.insert(0,u'\U0001F3A4 ')
    return
def enter1F3A7 ():
    textDisplay.insert(0,u'\U0001F3A7 ')
    return
def enter1F4FB ():
    textDisplay.insert(0,u'\U0001F4FB ')
    return
def enter1F4F1 ():
    textDisplay.insert(0,u'\U0001F4F1 ')
    return
def enter1F4F2 ():
    textDisplay.insert(0,u'\U0001F4F2 ')
    return
def enter1F4DE ():
    textDisplay.insert(0,u'\U0001F4DE ')
    return
def enter1F4DF ():
    textDisplay.insert(0,u'\U0001F4DF ')
    return
def enter1F4E0 ():
    textDisplay.insert(0,u'\U0001F4E0 ')
    return
def enter1F39E ():
    textDisplay.insert(0,u'\U0001F39E ')
    return
def enter1F39E ():
    textDisplay.insert(0,u'\U0001F39E ')
    return
def enter1F4FD ():
    textDisplay.insert(0,u'\U0001F4FD ')
    return
def enter1F4FD ():
    textDisplay.insert(0,u'\U0001F4FD ')
    return
def enter1F3AC ():
    textDisplay.insert(0,u'\U0001F3AC ')
    return
def enter1F4FA ():
    textDisplay.insert(0,u'\U0001F4FA ')
    return
def enter1F4F7 ():
    textDisplay.insert(0,u'\U0001F4F7 ')
    return
def enter1F4F8 ():
    textDisplay.insert(0,u'\U0001F4F8 ')
    return
def enter1F4F9 ():
    textDisplay.insert(0,u'\U0001F4F9 ')
    return
def enter1F4FC ():
    textDisplay.insert(0,u'\U0001F4FC ')
    return
def enter1F50D ():
    textDisplay.insert(0,u'\U0001F50D ')
    return
def enter1F50E ():
    textDisplay.insert(0,u'\U0001F50E ')
    return
def enter1F56F ():
    textDisplay.insert(0,u'\U0001F56F ')
    return
def enter1F56F ():
    textDisplay.insert(0,u'\U0001F56F ')
    return
def enter1F4A1 ():
    textDisplay.insert(0,u'\U0001F4A1 ')
    return
def enter1F526 ():
    textDisplay.insert(0,u'\U0001F526 ')
    return
def enter1F534 ():
    textDisplay.insert(0,u'\U0001F534 ')
    return
def enter1F7E0 ():
    textDisplay.insert(0,u'\U0001F7E0 ')
    return
def enter1F7E1 ():
    textDisplay.insert(0,u'\U0001F7E1 ')
    return
def enter1F7E2 ():
    textDisplay.insert(0,u'\U0001F7E2 ')
    return
def enter1F535 ():
    textDisplay.insert(0,u'\U0001F535 ')
    return
def enter1F7E3 ():
    textDisplay.insert(0,u'\U0001F7E3 ')
    return
def enter1F7E4 ():
    textDisplay.insert(0,u'\U0001F7E4 ')
    return
def enter1F7E5 ():
    textDisplay.insert(0,u'\U0001F7E5 ')
    return
def enter1F7E7 ():
    textDisplay.insert(0,u'\U0001F7E7 ')
    return
def enter1F7E8 ():
    textDisplay.insert(0,u'\U0001F7E8 ')
    return
def enter1F7E9 ():
    textDisplay.insert(0,u'\U0001F7E9 ')
    return
def enter1F7E6 ():
    textDisplay.insert(0,u'\U0001F7E6 ')
    return
def enter1F7EA ():
    textDisplay.insert(0,u'\U0001F7EA ')
    return
def enter1F7EB ():
    textDisplay.insert(0,u'\U0001F7EB ')
    return
def enter1F1E9 ():
    textDisplay.insert(0,u'\U0001F1E9 ')
    return
# function to pass into next emojis page keyboard
def nextFun():
    global lastIndex
    if (lastIndex != 384):
        btn1['command']=eval(listOfFunctions[lastIndex+1])
        btn1['text']=listOfEmojis[lastIndex+1]      
        btn2['command']=eval(listOfFunctions[lastIndex+2])
        btn2['text']=listOfEmojis[lastIndex+2]      
        btn3['command']=eval(listOfFunctions[lastIndex+3])
        btn3['text']=listOfEmojis[lastIndex+3]      
        btn4['command']=eval(listOfFunctions[lastIndex+4])
        btn4['text']=listOfEmojis[lastIndex+4]      
        btn5['command']=eval(listOfFunctions[lastIndex+5])
        btn5['text']=listOfEmojis[lastIndex+5]      
        btn6['command']=eval(listOfFunctions[lastIndex+6])
        btn6['text']=listOfEmojis[lastIndex+6]      
        btn7['command']=eval(listOfFunctions[lastIndex+7])
        btn7['text']=listOfEmojis[lastIndex+7]
        btn8['command']=eval(listOfFunctions[lastIndex+8])
        btn8['text']=listOfEmojis[lastIndex+8]
        btn9['command']=eval(listOfFunctions[lastIndex+9])
        btn9['text']=listOfEmojis[lastIndex+9]
        btn10['command']=eval(listOfFunctions[lastIndex+10])
        btn10['text']=listOfEmojis[lastIndex+10]
        btn11['command']=eval(listOfFunctions[lastIndex+11])
        btn11['text']=listOfEmojis[lastIndex+11]
        btn12['command']=eval(listOfFunctions[lastIndex+12])
        btn12['text']=listOfEmojis[lastIndex+12]
        btn13['command']=eval(listOfFunctions[lastIndex+13])
        btn13['text']=listOfEmojis[lastIndex+13]
        btn14['command']=eval(listOfFunctions[lastIndex+14])
        btn14['text']=listOfEmojis[lastIndex+14]
        btn15['command']=eval(listOfFunctions[lastIndex+15])
        btn15['text']=listOfEmojis[lastIndex+15]
        btn16['command']=eval(listOfFunctions[lastIndex+16])
        btn16['text']=listOfEmojis[lastIndex+16]
        btn17['command']=eval(listOfFunctions[lastIndex+17])
        btn17['text']=listOfEmojis[lastIndex+17]
        btn18['command']=eval(listOfFunctions[lastIndex+18])
        btn18['text']=listOfEmojis[lastIndex+18]
        btn19['command']=eval(listOfFunctions[lastIndex+19])
        btn19['text']=listOfEmojis[lastIndex+19]
        btn20['command']=eval(listOfFunctions[lastIndex+20])
        btn20['text']=listOfEmojis[lastIndex+20]
        btn21['command']=eval(listOfFunctions[lastIndex+21])
        btn21['text']=listOfEmojis[lastIndex+21]
        btn22['command']=eval(listOfFunctions[lastIndex+22])
        btn22['text']=listOfEmojis[lastIndex+22]
        btn23['command']=eval(listOfFunctions[lastIndex+23])
        btn23['text']=listOfEmojis[lastIndex+23]
        btn24['command']=eval(listOfFunctions[lastIndex+24])
        btn24['text']=listOfEmojis[lastIndex+24]
        lastIndex = lastIndex + 24
# function to return into next emojis page keyboard
def prevFun():
    global lastIndex
    if ((lastIndex - 24)!= 0):
        btn1['command']=eval(listOfFunctions[lastIndex-1])
        btn1['text']=listOfEmojis[lastIndex-1]
        btn2['command']=eval(listOfFunctions[lastIndex-2])
        btn2['text']=listOfEmojis[lastIndex-2]
        btn3['command']=eval(listOfFunctions[lastIndex-3])
        btn3['text']=listOfEmojis[lastIndex-3]
        btn4['command']=eval(listOfFunctions[lastIndex-4])
        btn4['text']=listOfEmojis[lastIndex-4]
        btn5['command']=eval(listOfFunctions[lastIndex-5])
        btn5['text']=listOfEmojis[lastIndex-5]
        btn6['command']=eval(listOfFunctions[lastIndex-6])
        btn6['text']=listOfEmojis[lastIndex-6]
        btn7['command']=eval(listOfFunctions[lastIndex-7])
        btn7['text']=listOfEmojis[lastIndex-7]
        btn8['command']=eval(listOfFunctions[lastIndex-8])
        btn8['text']=listOfEmojis[lastIndex-8]
        btn9['command']=eval(listOfFunctions[lastIndex-9])
        btn9['text']=listOfEmojis[lastIndex-9]
        btn10['command']=eval(listOfFunctions[lastIndex-10])
        btn10['text']=listOfEmojis[lastIndex-10]
        btn11['command']=eval(listOfFunctions[lastIndex-11])
        btn11['text']=listOfEmojis[lastIndex-11]
        btn12['command']=eval(listOfFunctions[lastIndex-12])
        btn12['text']=listOfEmojis[lastIndex-12]
        btn13['command']=eval(listOfFunctions[lastIndex-13])
        btn13['text']=listOfEmojis[lastIndex-13]
        btn14['command']=eval(listOfFunctions[lastIndex-14])
        btn14['text']=listOfEmojis[lastIndex-14]
        btn15['command']=eval(listOfFunctions[lastIndex-15])
        btn15['text']=listOfEmojis[lastIndex-15]
        btn16['command']=eval(listOfFunctions[lastIndex-16])
        btn16['text']=listOfEmojis[lastIndex-16]
        btn17['command']=eval(listOfFunctions[lastIndex-17])
        btn17['text']=listOfEmojis[lastIndex-17]
        btn18['command']=eval(listOfFunctions[lastIndex-18])
        btn18['text']=listOfEmojis[lastIndex-18]
        btn19['command']=eval(listOfFunctions[lastIndex-19])
        btn19['text']=listOfEmojis[lastIndex-19]
        btn20['command']=eval(listOfFunctions[lastIndex-20])
        btn20['text']=listOfEmojis[lastIndex-20]
        btn21['command']=eval(listOfFunctions[lastIndex-21])
        btn21['text']=listOfEmojis[lastIndex-21]
        btn22['command']=eval(listOfFunctions[lastIndex-22])
        btn22['text']=listOfEmojis[lastIndex-22]
        btn23['command']=eval(listOfFunctions[lastIndex-23])
        btn23['text']=listOfEmojis[lastIndex-23]
        btn24['command']=eval(listOfFunctions[lastIndex-24])
        btn24['text']=listOfEmojis[lastIndex-24]
        lastIndex = lastIndex - 24
# define the necessary buttons
btnChangeToNextEMOJISlist=Button(root,text=' Next ',command=nextFun ,width=5,font=("Arial", 10) , bg="#a9dce3")
btnChangeToPreviousEMOJISlist=Button(root,text=' Previous ',command=prevFun ,width=5,font=("Arial", 10) , bg="#a9dce3")
btnChangeToPreviousEMOJISlist.place(x=229,y=210)
btnChangeToNextEMOJISlist.place(x=285,y=210)
# launch our application
root.mainloop()