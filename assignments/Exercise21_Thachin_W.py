from tkinter import *
import math

def calcBMI(event):
    try:
        weight = float(entryWeight.get())
        height = float(entryHeight.get()) / 100
        bmi = round(weight / math.pow(height, 2),2)
        text = "~",bmi
        labelResult.configure(text = text)
        getMeaning(bmi)
    except:
        labelResult.configure(text = "Wrong input!")

def getMeaning(bmi):
    if bmi >= 30:
        text = "อ้วนมาก"
    elif bmi >= 25:
        text = "อ้วน"
    elif bmi >= 23:
        text = "น้ำหนักเกิน"
    elif bmi >= 18.6:
        text = "น้ำหนักปกติ เหมาะสม"
    else:
        text = "ผอมเกินไป"
    labelMeaning.configure(text = text)

mainWindow = Tk()

labelHeight = Label(mainWindow, text = "Height (cm.) : ").grid(row = 0, column = 0)
entryHeight = Entry(mainWindow)
entryHeight.grid(row = 0, column = 1)

labelWeight = Label(mainWindow, text = "Weight (kg.) : ").grid(row = 1, column = 0)
entryWeight = Entry(mainWindow)
entryWeight.grid(row = 1, column = 1)

labelBMI = Label(mainWindow, text = "BMI").grid(row = 2, column = 0)

labelResult = Label(mainWindow, text = "-")
labelResult.grid(row = 2, column = 1)

labelMeaning = Label(mainWindow, text = "")
labelMeaning.grid(row = 3, column = 1)

btnCalc = Button(mainWindow, text = "Calculate BMI")
btnCalc.grid(row = 4, column = 1)
btnCalc.bind('<Button-1>',calcBMI)

mainWindow.mainloop()
