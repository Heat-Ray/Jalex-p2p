from tkinter import *

window = Tk()
window.title("Jalex-p2p")
window.geometry("600x500+150+50")

frame1 = Frame(window)
lbl1 = Label(frame1,text="Please choose an option",font = ("Arial",18))
lbl1.pack(side = LEFT)
frame1.pack(fill="x")

frame2 = Frame(window)
var = StringVar()
radio1 = Radiobutton(frame2, text="Send a file", variable=var, value="Send", font=("Arial",12), anchor="w", justify="left")
radio1.pack(fill="x")
frame2.pack(fill="both")

window.mainloop()