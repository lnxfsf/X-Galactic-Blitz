
from turtle import *
from freegames import line
from random import choice, random
from turtle import *
import turtle
from tkinter import *

def start():
    def grid():
        "Draw tic-tac-toe grid."
        line(-67, 200, -67, -200)
        line(67, 200, 67, -200)
        line(-200, -67, 200, -67)
        line(-200, 67, 200, 67)

    def drawx(x, y):
        "Draw X player."
        line(x, y, x + 133, y + 133)
        line(x, y + 133, x + 133, y)



    def drawo(x, y):
        "Draw O player."
        up()
        goto(x + 67, y + 5)
        down()
        circle(62)


    def floor(value):
        "Round value down to grid with square size 133."
        return ((value + 200) // 133) * 133 - 200

    state = {'player': 0}
    players = [drawx, drawo]

    def tap(x, y):
        "Draw X or O in tapped square."
        x = floor(x)
        y = floor(y)
        player = state['player']
        draw = players[player]
        draw(x, y)
        update()
        state['player'] = not player

    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    grid()
    update()
    onscreenclick(tap)
    done()

#ovo sam ispod sve dodao

root=Tk()
root.geometry("400x200")
root.title('TIC TAC TOE')

def about(): #funkcija za dugme about
    new_window1 = Toplevel() #otvaranje novog prozoroa
    new_window1.title('About') #ime prozora
    labela = Label(new_window1, text='Iks-oks je igra za dva igrača koja se \n'
                   'igra na papiru na polju 3x3 kvadrata. \n'
                   'Igrači naizmenično postavljaju svoje \n'
                   'znakove (jedan koristi ikseve, drugi kružiće) \n'
                   'u slobodna polja. Cilj igre je spojiti tri znaka \n'
                   'vodoravno, uspravno ili dijagonalno.',
                   font=('Arial', 10))
    labela.grid(row=2, column=0)

label1=Label(text='')
label2=Label(text='TIC TAC TOE', font=('Arial',25,'bold'), fg='blue') #naslov

button1=Button(text='Start', command=start) #samo ubacio onaj prvi program u funkcija da se pali na start
button2=Button(text='About', command=about)
button3=Button(text='Exit', command=root.destroy)

label1.pack()
label2.pack()

button1.pack()
button2.pack()
button3.pack()

mainloop()
