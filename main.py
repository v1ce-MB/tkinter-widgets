from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox

window=Tk()

def msg():
   # messagebox.showwarning("Warning!!", "you have clicked the button")
   #messagebox.showerror("error!", "you have clicked too many times!")
   #messagebox.showinfo("info", "it is 4;50 pm!")
   #messagebox.askokcancel("askok", "Do you want to continue?")
   messagebox.askretrycancel("question", "Do you want to close?")

upload= Image.open("ars img.png")
Arsenal=ImageTk.PhotoImage(upload)
image= Label(window, image=Arsenal )
image.pack()

button=Button(window, text="click!", command=msg)
button.pack()



window.mainloop()