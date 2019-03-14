from tkinter import *
from tkinter import filedialog
import os
import soc_server
import soc_client

def chooseFile():
    filePath = filedialog.askopenfilename() #!filetypes=(("All files", "*.*")) Why this is not working?
    entry1.insert(0, filePath)
    print(filePath)

def chooseRadio():
    if(var.get() == "Send"):
        entry1.config(state=NORMAL)
        btn1.config(state=NORMAL)
    else:
        entry1.config(state=DISABLED)
        btn1.config(state=DISABLED)

def startShare():
    if (var.get() == "Send"):
        soc_server.startServer(entry1.get())
    else:
        soc_client.startClient()
    
def checkFileValidity():
    print("Checking file validity..")
    if os.path.isfile(entry1.get()):
        entry1.config(fg="green")
    else:
        entry1.config(fg="red")
    window.after(2000, checkFileValidity)

window = Tk()
window.title("Jalex-p2p")
window.geometry("600x500+150+50")

frame1 = Frame(window)
lbl1 = Label(frame1,text="Please choose an option",font = ("Arial",18))
lbl1.pack(side = LEFT)
frame1.pack(fill="x", padx=10, pady=10)

frame2 = Frame(window)
var = StringVar()
radio1 = Radiobutton(frame2, text="Send a file", variable=var, value="Send", font=("arial", 12), anchor="w", justify="left", command=chooseRadio)
radio1.pack(fill="x")
radio2 = Radiobutton(frame2, text="Recieve a file", variable=var, value="Recieve", font=("Arial",12), anchor="w", justify="left", command=chooseRadio)
radio2.pack(fill="x")
var.set("Send")
frame2.pack(fill="x",pady=10)

frame3 = Frame(window)
lbl2 = Label(frame3, text="Specify the file path here: ", font=("Arial",12))
lbl2.pack(fill="both", padx=10, pady=10, side=LEFT)
frame3.pack(fill="both")

frame4 = Frame(window)
entry1 = Entry(frame4, bd=1, font=("Arial",12), width=35)
entry1.pack(side=LEFT, anchor="n", padx=10, pady=10)
filePath = ""
btn1 = Button(frame4, text="Browse", font=("Arial",12), command=chooseFile)
btn1.pack(pady=10, side=LEFT)
print(filePath) #TODO:Fix cann't access variable after using global filePath in function chooseFile
frame4.pack(fill="both")

frame5 = Frame(window)
btn2 = Button(window, text="Start sharing", font=("Arial",12), command=startShare)
btn2.pack()
frame5.pack(fill="both", pady=10)

window.after(2000, checkFileValidity)
window.mainloop()