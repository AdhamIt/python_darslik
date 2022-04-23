import tkinter as tk

# Label
# Button
# Input -> Entry

win = tk.Tk()
win.geometry("300x300+450+200")
# win.resizable(width=300, height=300)
win.minsize(width=300, height=300)
win.maxsize(width=300, height=300)
win.title("Birinchi loyiha")
rasm=tk.PhotoImage(file='icon.png')
win.iconphoto(False, rasm)
win.config(bg="red")


button1 = tk.Button(win, text="Button1", bg="yellow", fg="violet")
label = tk.Label(win, text="Label", bg="yellow")
entr = tk.Entry()
chekbox = tk.Checkbutton(win, text="Chekbox")
radio = tk.Radiobutton(win, text="bu radio button")
# pack 
# place
# grid
button1.pack()
label.pack()
entr.pack()
chekbox.pack()
radio.pack()
# button1.place(x=10, y=50)
# label.place(x=60, y=100)
# label.grid(row=0, column=1)
# button1.grid(row=1, column=200)








win.mainloop()