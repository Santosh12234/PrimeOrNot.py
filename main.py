from tkinter import *

root = Tk()
root.config(bg="Pink")

root.resizable(False, False)


def checknum():
    n = int(Entry1.get())
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        label2.config(text=str(n) + " is a prime number")
    else:
        label2.config(text=str(n) + " is not a prime number")


Entry1 = Entry(root, bg="white", fg="black", width=14, font=("Candra", 18))
Entry1.place(x=155, y=300)
root.geometry("500x500")

button1 = Button(root, bg="red", fg="black", width=10, height=1, text="Exit", font=("Candra", 10),
                 command=lambda: exit(0))
button1.place(x=155, y=350)

button2 = Button(root, bg="green", fg="black", width=10, height=1, text="Check", font=("Candra", 10),
                 command=lambda: checknum())
button2.place(x=250, y=350)

label1 = Label(root, bg="light yellow", fg="black", width=29, height=1, text="PRIME  OR  NOT", font=("candra", 20))
label1.place(x=13, y=13)

label2 = Label(root, bg="pink", fg="black", width=29, height=1, font=("candra", 20))
label2.place(x=13, y=200)

root.mainloop()