from tkinter import *

root = Tk()
root.title('Menu')
root.configure(background='#FFFF99')
root.geometry("335x600")


def clean():
    global pizzas
    w.destroy()
    root.deiconify()
    for i in range(len(pizzas)):
        pizzas[i - 1].set(False)


def order():
    global pizzas, labels, w,logo00,label400,lbl300
    labels = [lbl3, lbl4, lbl5, lbl6, lbl8, lbl7, lbl9, lbl11,lbl12,lbl13,lbl14,lbl15,lbl16]
    w = Tk()
    w.configure(background='#FFFF99')
    w.geometry("335x600")
    root.withdraw()
    w.title("Order")
    lbl10 = Label(w, text="That's your order", font=('Arial', 25),bg='#FFFF99')
    lbl10.pack()

    class Order():

        def __init__(self, text):
            self.text = text

        def print(self):
            h = Label(w, text=self.text, font=('Arial', 17),bg='#FFFF99')
            h.pack()

    for i in range(len(labels)):
        if pizzas[i - 1].get() == True:
            orderr = Order(labels[i - 1].cget("text"))
            orderr.print()

    btn2 = Button(w, text='OK', command=clean, font=('Arial', 13),bg='#FFFF99')
    btn2.pack()
    logo00 = PhotoImage(file="pizza (1).png")
    lbl300 = Label(w, image=logo00, bg='#FFFF99')
    lbl300.pack()
    lbl400 = Label(w, text="Developed by Kalampas", font=('Arial', 24), bg='#FFFF99')
    lbl400.pack(side=BOTTOM)


def menu():
    global lbl, lbl2, lbl3, lbl4, lbl5, lbl6, lbl7, lbl8, lbl9, lbl11,lbl12,lbl13,lbl14,lbl15,lbl16,logo,lbl100,logo0,lbl200
    lbl = Label(root, text='Italian Menu', font=('Italiana', 30),bg='#FFFF99')
    lbl.grid(row=0, column=0, columnspan=4)
    lbl2 = Label(root, text='Pizza', font=('Tahoma', 20),bg='#FFFF99')
    lbl2.grid(row=1, column=0, columnspan=2)
    lbl3 = Label(root, text='Chicago 8$', font=('Tahoma', 13),bg='#FFFF99')
    lbl3.grid(row=2, column=0)
    lbl4 = Label(root, text='Greek 7$', font=('Tahoma', 13),bg='#FFFF99')
    lbl4.grid(row=3, column=0)
    lbl5 = Label(root, text='California 9$', font=('Tahoma', 13),bg='#FFFF99')
    lbl5.grid(row=4, column=0)
    lbl6 = Label(root, text='Detroit 10$', font=('Tahoma', 13),bg='#FFFF99')
    lbl6.grid(row=5, column=0)
    lbl8 = Label(root, text='Neapolitan 6$', font=('Tahoma', 13),bg='#FFFF99')
    lbl8.grid(row=6, column=0)
    lbl7 = Label(root, text='St.Louis 7$', font=('Tahoma', 13),bg='#FFFF99')
    lbl7.grid(row=7, column=0)
    lbl9 = Label(root, text='Margarita 8$', font=('Tahoma', 13),bg='#FFFF99')
    lbl9.grid(row=8, column=0)
    lbl11 = Label(root, text='Philadelphia 6$', font=('Tahoma', 13),bg='#FFFF99')
    lbl11.grid(row=9, column=0)

    chk = Checkbutton(root, var=chkp1, font=("Tahoma", 15),bg='#FFFF99')
    chk.grid(row=2, column=1)
    chk2 = Checkbutton(root, var=chkp2, font=("Tahoma", 15),bg='#FFFF99')
    chk2.grid(row=3, column=1)
    chk3 = Checkbutton(root, var=chkp3, font=("Tahoma", 15),bg='#FFFF99')
    chk3.grid(row=4, column=1)
    chk4 = Checkbutton(root, var=chkp4, font=("Tahoma", 15),bg='#FFFF99')
    chk4.grid(row=5, column=1)
    chk5 = Checkbutton(root, var=chkp5, font=("Tahoma", 15),bg='#FFFF99')
    chk5.grid(row=6, column=1)
    chk6 = Checkbutton(root, var=chkp6, font=("Tahoma", 15),bg='#FFFF99')
    chk6.grid(row=7, column=1)
    chk7 = Checkbutton(root, var=chkp7, font=("Tahoma", 15),bg='#FFFF99')
    chk7.grid(row=8, column=1)
    chk8 = Checkbutton(root, var=chkp8, font=("Tahoma", 15),bg='#FFFF99')
    chk8.grid(row=9, column=1)

    lbl12 = Label(root, text='Spaghetti', font=('Tahoma', 20),bg='#FFFF99')
    lbl12.grid(row=1, column=2, columnspan=2)
    lbl13 = Label(root, text='Mafaldine 10$', font=('Tahoma', 13),bg='#FFFF99')
    lbl13.grid(row=2, column=2,rowspan=2)
    lbl14 = Label(root, text='Pappardelle 9$', font=('Tahoma', 13),bg='#FFFF99')
    lbl14.grid(row=4, column=2,rowspan=2)
    lbl15 = Label(root, text='Stringozzi 12$', font=('Tahoma', 13),bg='#FFFF99')
    lbl15.grid(row=6, column=2,rowspan=2)
    lbl16 = Label(root, text='Bucatini 8$', font=('Tahoma', 13),bg='#FFFF99')
    lbl16.grid(row=8, column=2,rowspan=2)

    chk11 = Checkbutton(root, var=chkp11, font=("Tahoma", 15),bg='#FFFF99')
    chk11.grid(row=2, column=3,rowspan=2)
    chk12 = Checkbutton(root, var=chkp12, font=("Tahoma", 15),bg='#FFFF99')
    chk12.grid(row=4, column=3,rowspan=2)
    chk13 = Checkbutton(root, var=chkp13, font=("Tahoma", 15),bg='#FFFF99')
    chk13.grid(row=6, column=3,rowspan=2)
    chk14 = Checkbutton(root, var=chkp14, font=("Tahoma", 15),bg='#FFFF99')
    chk14.grid(row=8, column=3,rowspan=2)

    btn = Button(root, text='Finish order', command=order, font=("Tahoma", 12),bg='#FFFF99')
    btn.grid(row=10, column=0, columnspan=4)

    logo = PhotoImage(file="R0aef0559f630f1ab3f85838f3e85e4c0.png")
    lbl100 = Label(root, image=logo,bg='#FFFF99')
    lbl100.grid(row=11, column=2, columnspan=2)
    logo0 = PhotoImage(file="R0aef0559f630f1ab3f85838f3e85e4c0222.png")
    lbl200 = Label(root, image=logo0,bg='#FFFF99')
    lbl200.grid(row=11, column=0, columnspan=2)


chkp1 = BooleanVar()
chkp2 = BooleanVar()
chkp3 = BooleanVar()
chkp4 = BooleanVar()
chkp5 = BooleanVar()
chkp6 = BooleanVar()
chkp7 = BooleanVar()
chkp8 = BooleanVar()
chkp11 = BooleanVar()
chkp12 = BooleanVar()
chkp13 = BooleanVar()
chkp14 = BooleanVar()

pizzas = [chkp1, chkp2, chkp3, chkp4, chkp5, chkp6, chkp7, chkp8, chkp11, chkp12, chkp13, chkp14]

menu()

root.mainloop()
