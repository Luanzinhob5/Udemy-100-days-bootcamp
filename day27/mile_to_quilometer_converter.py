from tkinter import *

def calculate():
    mile = input.get()
    calc = float(mile) * 1.609
    label_2.config(text=calc)


#Window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300,height=100)


#Label
label = Label(text="", font=("Arial", 18, "normal"))
label.grid(column=0,row=0)

label_1 = Label(text="is equal to", font=("Arial", 16, "normal"))
label_1.grid(column=0,row=1)

label_2 = Label(text="0",font=("Arial", 16, "normal"))
label_2.grid(column=1,row=1)

label_3 = Label(text="Km",font=("Arial", 16, "normal"))
label_3.grid(column=2,row=1)

label_4 = Label(text="Miles",font=("Arial", 16, "normal"))
label_4.grid(column=2,row=0)

#Button
button = Button(text="Calculate",command=calculate)
button.grid(column=1,row=2)

#input
input = Entry(width=10)
input.grid(column=1,row=0)



window.mainloop()