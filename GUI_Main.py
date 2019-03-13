from tkinter import *

window = Tk()
window.title("Jalex-p2p")
window.geometry("600x500+150+50")

frame1 = Frame(window)
lbl1 = Label(frame1,text="Please choose an option",font = ("Arial",18))
lbl1.pack(side = LEFT)
frame1.pack(fill="x", padx=10, pady=10)

frame2 = Frame(window)
var = StringVar()
radio1 = Radiobutton(frame2, text="Send a file", variable=var, value="Send", font=("arial", 12), anchor="w", justify="left")
radio1.pack(fill="x")
radio2 = Radiobutton(frame2, text="Recieve a file", variable=var, value="Recieve", font=("Arial",12), anchor="w", justify="left")
radio2.pack(fill="x")
var.set("Send")
frame2.pack(fill="x",pady=10)

frame3 = Frame(window)
lbl2 = Label(frame3, text="Specify the file path here: ", font=("Arial",12))
lbl2.pack(fill="both", padx=10, pady=10, side=LEFT)
frame3.pack(fill="both")

frame4 = Frame(window)
entry1 = Entry(frame4, bd=1, font=("Arial",12))
entry1.pack(side=LEFT, anchor="n", padx=10, pady=10)
frame4.pack(fill="both")

window.mainloop()