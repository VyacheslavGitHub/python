from tkinter import *
root = Tk()

# Frame (рамка)
fra1 = Frame(root, width=500, height=100, bg='darkred')
fra2 = Frame(root, width=300, height=200, bg='green', bd=20)
fra3 = Frame(root, width=500, height=150, bg='darkblue')

ent1 = Entry(fra2, width=20)
ent1.pack()
fra1.pack()
fra2.pack()
fra3.pack()

# шкала (Scale)

sca1 = Scale(fra3, orient=HORIZONTAL, length=300,
            from_=0, to=100, tickinterval=10, resolution=5)

# length - длина в пикселях
# from_, to - цифры на шкале
# tickinterval - цена деления
# resolution - шаг ходьбы
#sca1.pack()

#шкала прокрутки (Scrollbar)
#
#tx = Text(root, width=40, height=10, font='14')
#scr = Scrollbar(root, command=tx.yview)
#tx.configure(yscrollcommand=scr.set)
#
#tx.grid(row=0, column=1)
#scr.grid(row=0, column=1)

# окно верхнего уровня
win = Toplevel(root, relief=SUNKEN, bd=10, bg='blue')
win.title('дочернее окно')
win.minsize(width=400, height=200)
win.maxsize(width=4000, height=2000)

root.mainloop()
