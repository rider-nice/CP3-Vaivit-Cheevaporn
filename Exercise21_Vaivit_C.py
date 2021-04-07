from tkinter import *

def Calculator():
    H = float(TextH.get())
    W = float(TextW.get())
    BMI = W/((H/100)**2)
    Result = ""
    if BMI >= 30:
        Result = "อ้วนมาก"
    elif BMI >= 25:
        Result = "อ้วน"
    elif BMI >= 23:
        Result = "น้ำหนักเกิน"
    elif BMI >= 18.6:
        Result = "น้ำหนักปกติ เหมาะสม"
    elif BMI < 18.6:
        Result = "ผอมเกินไป"
    LabelR.configure(text = Result)

MainWindow = Tk()

LabelH = Label(MainWindow,
               text = "Height"
               ).grid(row = 0, column = 0)

TextH = Entry(MainWindow)
TextH.grid(row = 0, column = 1)

LabelHcm = Label(MainWindow,
                 text = "cm.",
                 ).grid(row = 0, column = 2)

LabelW = Label(MainWindow,
               text = "Weight"
               ).grid(row = 1, column = 0)

TextW = Entry(MainWindow)
TextW.grid(row = 1, column = 1)

LabelWkg = Label(MainWindow,
                 text = "kg.",
                 ).grid(row = 1, column = 2)

CalculateBut = Button(MainWindow,
                      text = "Calculate",
                      command = Calculator
                      ).grid(row = 2, column = 1)

LabelR = Label(MainWindow,
               text = "Result"
               )
LabelR.grid(row = 3, column = 1)

MainWindow.mainloop()