from logging import root
from tkinter import *
from turtle import left
import emoji
from emojiLib import *

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
btn1=Button(root,text='\U0001F600 ',command=lambda:enter1F600(textDisplay),width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn1.place(x=5,y=70)
btn2=Button(root,text='\U0001F603 ',command=lambda:enter1F603(textDisplay),width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn2.place(x=74,y=70)
btn3=Button(root,text='\U0001F604 ',command=lambda:enter1F604(textDisplay),width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn3.place(x=144,y=70)
btn4=Button(root,text='\U0001F601 ',command=lambda:enter1F601(textDisplay),width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn4.place(x=215,y=70)
btn5=Button(root,text='\U0001F606 ',command=lambda:enter1F606(textDisplay),width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn5.place(x=285,y=70)
btn6=Button(root,text='\U0001F605 ',command=lambda:enter1F605(textDisplay),width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn6.place(x=354,y=70)
btn7=Button(root,text='\U0001F923 ',command=lambda:enter1F923(textDisplay),width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn7.place(x=424,y=70)
btn8=Button(root,text='\U0001F602 ',command=lambda:enter1F602(textDisplay) ,width=4,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn8.place(x=492,y=70)
btn9=Button(root,text='\U0001F642 ',command=lambda:enter1F642(textDisplay),width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn9.place(x=5,y=115)
btn10=Button(root,text='\U0001F643 ',command=lambda:enter1F643(textDisplay),width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn10.place(x=74,y=115)
btn11=Button(root,text='\U0001F609 ',command=lambda:enter1F609(textDisplay),width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn11.place(x=144,y=115)
btn12=Button(root,text='\U0001F60A ',command=lambda:enter1F60A(textDisplay),width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn12.place(x=215,y=115)
btn13=Button(root,text='\U0001F607 ',command=lambda:enter1F607(textDisplay),width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn13.place(x=285,y=115)
btn14=Button(root,text='\U0001F92A ',command=lambda:enter1F92A(textDisplay) ,width=4,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn14.place(x=492,y=160)
btn15=Button(root,text='\U0001F970 ',command=lambda:enter1F970(textDisplay),width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn15.place(x=354,y=115)
btn16=Button(root,text='\U0001F60D ',command=lambda:enter1F60D(textDisplay),width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn16.place(x=424,y=115)
btn17=Button(root,text='\U0001F929 ',command=lambda:enter1F929(textDisplay) ,width=4,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn17.place(x=492,y=115)
btn18=Button(root,text='\U0001F618 ',command=lambda:enter1F618(textDisplay),width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn18.place(x=5,y=160)
btn19=Button(root,text='\U0001F617 ',command=lambda:enter1F617(textDisplay),width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn19.place(x=74,y=160)
btn20=Button(root,text='\U0001F61A ',command=lambda:enter1F61A(textDisplay),width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn20.place(x=144,y=160)
btn21=Button(root,text='\U0001F619 ',command=lambda:enter1F619(textDisplay),width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn21.place(x=215,y=160)
btn22=Button(root,text='\U0001F61C ',command=lambda:enter1F61C(textDisplay),width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn22.place(x=424,y=160)
btn23=Button(root,text='\U0001F60B ',command=lambda:enter1F60B(textDisplay),width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn23.place(x=285,y=160)
btn24=Button(root,text='\U0001F61B ',command=lambda:enter1F61B(textDisplay),width=5,font=("Arial", 15), cursor="hand2" , bg="#a9dce3")
btn24.place(x=354,y=160)
# other functions for others emojis thats are not showed on first open of application
# i make them on library
# function to pass into next emojis page keyboard
def nextFun():
    global lastIndex
    if (lastIndex != 384):
        btn1['command']=eval("lambda:"+listOfFunctions[lastIndex+1]+"(textDisplay)")
        btn1['text']=listOfEmojis[lastIndex+1]      
        btn2['command']=eval("lambda:"+listOfFunctions[lastIndex+2]+"(textDisplay)")
        btn2['text']=listOfEmojis[lastIndex+2]      
        btn3['command']=eval("lambda:"+listOfFunctions[lastIndex+3]+"(textDisplay)")
        btn3['text']=listOfEmojis[lastIndex+3]      
        btn4['command']=eval("lambda:"+listOfFunctions[lastIndex+4]+"(textDisplay)")
        btn4['text']=listOfEmojis[lastIndex+4]      
        btn5['command']=eval("lambda:"+listOfFunctions[lastIndex+5]+"(textDisplay)")
        btn5['text']=listOfEmojis[lastIndex+5]      
        btn6['command']=eval("lambda:"+listOfFunctions[lastIndex+6]+"(textDisplay)")
        btn6['text']=listOfEmojis[lastIndex+6]      
        btn7['command']=eval("lambda:"+listOfFunctions[lastIndex+7]+"(textDisplay)")
        btn7['text']=listOfEmojis[lastIndex+7]
        btn8['command']=eval("lambda:"+listOfFunctions[lastIndex+8]+"(textDisplay)")
        btn8['text']=listOfEmojis[lastIndex+8]
        btn9['command']=eval("lambda:"+listOfFunctions[lastIndex+9]+"(textDisplay)")
        btn9['text']=listOfEmojis[lastIndex+9]
        btn10['command']=eval("lambda:"+listOfFunctions[lastIndex+10]+"(textDisplay)")
        btn10['text']=listOfEmojis[lastIndex+10]
        btn11['command']=eval("lambda:"+listOfFunctions[lastIndex+11]+"(textDisplay)")
        btn11['text']=listOfEmojis[lastIndex+11]
        btn12['command']=eval("lambda:"+listOfFunctions[lastIndex+12]+"(textDisplay)")
        btn12['text']=listOfEmojis[lastIndex+12]
        btn13['command']=eval("lambda:"+listOfFunctions[lastIndex+13]+"(textDisplay)")
        btn13['text']=listOfEmojis[lastIndex+13]
        btn14['command']=eval("lambda:"+listOfFunctions[lastIndex+14]+"(textDisplay)")
        btn14['text']=listOfEmojis[lastIndex+14]
        btn15['command']=eval("lambda:"+listOfFunctions[lastIndex+15]+"(textDisplay)")
        btn15['text']=listOfEmojis[lastIndex+15]
        btn16['command']=eval("lambda:"+listOfFunctions[lastIndex+16]+"(textDisplay)")
        btn16['text']=listOfEmojis[lastIndex+16]
        btn17['command']=eval("lambda:"+listOfFunctions[lastIndex+17]+"(textDisplay)")
        btn17['text']=listOfEmojis[lastIndex+17]
        btn18['command']=eval("lambda:"+listOfFunctions[lastIndex+18]+"(textDisplay)")
        btn18['text']=listOfEmojis[lastIndex+18]
        btn19['command']=eval("lambda:"+listOfFunctions[lastIndex+19]+"(textDisplay)")
        btn19['text']=listOfEmojis[lastIndex+19]
        btn20['command']=eval("lambda:"+listOfFunctions[lastIndex+20]+"(textDisplay)")
        btn20['text']=listOfEmojis[lastIndex+20]
        btn21['command']=eval("lambda:"+listOfFunctions[lastIndex+21]+"(textDisplay)")
        btn21['text']=listOfEmojis[lastIndex+21]
        btn22['command']=eval("lambda:"+listOfFunctions[lastIndex+22]+"(textDisplay)")
        btn22['text']=listOfEmojis[lastIndex+22]
        btn23['command']=eval("lambda:"+listOfFunctions[lastIndex+23]+"(textDisplay)")
        btn23['text']=listOfEmojis[lastIndex+23]
        btn24['command']=eval("lambda:"+listOfFunctions[lastIndex+24]+"(textDisplay)")
        btn24['text']=listOfEmojis[lastIndex+24]
        lastIndex = lastIndex + 24
# function to return into next emojis page keyboard
def prevFun():
    global lastIndex
    if ((lastIndex - 24)!= 0):
        btn1['command']=eval("lambda:"+listOfFunctions[lastIndex-1]+"(textDisplay)")
        btn1['text']=listOfEmojis[lastIndex-1]
        btn2['command']=eval("lambda:"+listOfFunctions[lastIndex-2]+"(textDisplay)")
        btn2['text']=listOfEmojis[lastIndex-2]
        btn3['command']=eval("lambda:"+listOfFunctions[lastIndex-3]+"(textDisplay)")
        btn3['text']=listOfEmojis[lastIndex-3]
        btn4['command']=eval("lambda:"+listOfFunctions[lastIndex-4]+"(textDisplay)")
        btn4['text']=listOfEmojis[lastIndex-4]
        btn5['command']=eval("lambda:"+listOfFunctions[lastIndex-5]+"(textDisplay)")
        btn5['text']=listOfEmojis[lastIndex-5]
        btn6['command']=eval("lambda:"+listOfFunctions[lastIndex-6]+"(textDisplay)")
        btn6['text']=listOfEmojis[lastIndex-6]
        btn7['command']=eval("lambda:"+listOfFunctions[lastIndex-7]+"(textDisplay)")
        btn7['text']=listOfEmojis[lastIndex-7]
        btn8['command']=eval("lambda:"+listOfFunctions[lastIndex-8]+"(textDisplay)")
        btn8['text']=listOfEmojis[lastIndex-8]
        btn9['command']=eval("lambda:"+listOfFunctions[lastIndex-9]+"(textDisplay)")
        btn9['text']=listOfEmojis[lastIndex-9]
        btn10['command']=eval("lambda:"+listOfFunctions[lastIndex-10]+"(textDisplay)")
        btn10['text']=listOfEmojis[lastIndex-10]
        btn11['command']=eval("lambda:"+listOfFunctions[lastIndex-11]+"(textDisplay)")
        btn11['text']=listOfEmojis[lastIndex-11]
        btn12['command']=eval("lambda:"+listOfFunctions[lastIndex-12]+"(textDisplay)")
        btn12['text']=listOfEmojis[lastIndex-12]
        btn13['command']=eval("lambda:"+listOfFunctions[lastIndex-13]+"(textDisplay)")
        btn13['text']=listOfEmojis[lastIndex-13]
        btn14['command']=eval("lambda:"+listOfFunctions[lastIndex-14]+"(textDisplay)")
        btn14['text']=listOfEmojis[lastIndex-14]
        btn15['command']=eval("lambda:"+listOfFunctions[lastIndex-15]+"(textDisplay)")
        btn15['text']=listOfEmojis[lastIndex-15]
        btn16['command']=eval("lambda:"+listOfFunctions[lastIndex-16]+"(textDisplay)")
        btn16['text']=listOfEmojis[lastIndex-16]
        btn17['command']=eval("lambda:"+listOfFunctions[lastIndex-17]+"(textDisplay)")
        btn17['text']=listOfEmojis[lastIndex-17]
        btn18['command']=eval("lambda:"+listOfFunctions[lastIndex-18]+"(textDisplay)")
        btn18['text']=listOfEmojis[lastIndex-18]
        btn19['command']=eval("lambda:"+listOfFunctions[lastIndex-19]+"(textDisplay)")
        btn19['text']=listOfEmojis[lastIndex-19]
        btn20['command']=eval("lambda:"+listOfFunctions[lastIndex-20]+"(textDisplay)")
        btn20['text']=listOfEmojis[lastIndex-20]
        btn21['command']=eval("lambda:"+listOfFunctions[lastIndex-21]+"(textDisplay)")
        btn21['text']=listOfEmojis[lastIndex-21]
        btn22['command']=eval("lambda:"+listOfFunctions[lastIndex-22]+"(textDisplay)")
        btn22['text']=listOfEmojis[lastIndex-22]
        btn23['command']=eval("lambda:"+listOfFunctions[lastIndex-23]+"(textDisplay)")
        btn23['text']=listOfEmojis[lastIndex-23]
        btn24['command']=eval("lambda:"+listOfFunctions[lastIndex-24]+"(textDisplay)")
        btn24['text']=listOfEmojis[lastIndex-24]
        lastIndex = lastIndex - 24
# define the necessary buttons
btnChangeToNextEMOJISlist=Button(root,text=' Next ',command=nextFun ,width=5,font=("Arial", 10) , bg="#a9dce3")
btnChangeToPreviousEMOJISlist=Button(root,text=' Previous ',command=prevFun ,width=5,font=("Arial", 10) , bg="#a9dce3")
btnChangeToPreviousEMOJISlist.place(x=229,y=210)
btnChangeToNextEMOJISlist.place(x=285,y=210)
# launch our application
root.mainloop()