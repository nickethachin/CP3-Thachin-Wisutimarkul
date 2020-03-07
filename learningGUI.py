from tkinter import *

userLogin = False
userId = "root"
userPassword = "1234"

def login(event):
    userInputID = entryUsername.get()
    print(userInputID)
    userInputPassword = entryPassword.get()
    print(userInputPassword)


mainWindow = Tk()
labelUsername = Label(mainWindow, text = "User : ").grid(row = 0, column = 0)
entryUsername = Entry(mainWindow)
entryUsername.grid(row = 0, column = 1)
labelPassword = Label(mainWindow, text = "Pass : ").grid(row = 1, column = 0)
entryPassword = Entry(mainWindow,show = "*")
entryPassword.grid(row = 1, column = 1)
btnLogin = Button(mainWindow, text = "Login")
btnLogin.grid(row = 2, column = 1)
btnLogin.bind('<Button-1>',login)
mainWindow.mainloop()
