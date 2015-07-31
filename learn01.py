#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *

# általános mozgató eljárás
def mozog(gd, hb):
    global x1, y1
    x1, y1 = x1 +gd, y1 +hb
    can1.coords(oval1, x1, y1, x1+30, y1+30)


def mozog2(gd, hb):
    global z1, v1
    z1, v1 = z1 +gd, v1 +hb
    can1.coords(oval2, z1, v1 ,z1+50, v1+50)

# eseménykezelők
def mozdit_balra():
    mozog(-10, 0)

def mozdit_jobbra():
    mozog (10, 0)

def mozdit_fel():
    mozog (0, -10)

def mozdit_le():
    mozog (0, 10)

def mozdit_balra2():
    mozog2(-10, 0)

def mozdit_jobbra2():
    mozog2 (10, 0)

def mozdit_fel2():
    mozog2 (0, -10)

def mozdit_le2():
    mozog2 (0, 10)

# Főprogram

# a következő változók globálisak,
x1, y1 = 10, 10 #kiindulási kordináták
z1, v1 = 50, 50

# A fő ("master") widget létrehozása
abl1 = Tk()
abl1.title("Animációs gyakorlat TKinter-rel")

# "slave" widget-ek létrhezoása

can1 = Canvas(abl1,bg='dark grey', height=300, width=300)
oval1 = can1.create_oval(x1,y1,x1+30,y1+30,width=2,fill='red')
oval2 = can1.create_oval(z1,v1,z1+50,v1+50,width=2,fill='blue')
can1.pack(side=LEFT)
Button(abl1,text='Kilép', command=abl1.quit).pack(side=BOTTOM)
Button(abl1,text='Balra', command=mozdit_balra).pack()
Button(abl1,text='Jobbra', command=mozdit_jobbra).pack()
Button(abl1,text='Föl', command=mozdit_fel).pack()
Button(abl1,text='Le', command=mozdit_le).pack()

Button(abl1,text='Balra', command=mozdit_balra2).pack()
Button(abl1,text='Jobbra', command=mozdit_jobbra2).pack()
Button(abl1,text='Föl', command=mozdit_fel2).pack()
Button(abl1,text='Le', command=mozdit_le2).pack()
Tavolsag=Label(abl1,text="Távolság:").pack(side=LEFT)


#eseményfigyelő (főhurok) indítás
abl1.mainloop()