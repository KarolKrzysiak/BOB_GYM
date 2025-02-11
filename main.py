from tkinter import *
import tkinter as tk

root = Tk()
frm = tk.Frame(root)
frm.grid()
tk.Label(frm, text="BOB GYM").grid(column=0,row=0)
#tk.Button(frm, text="Quit", command=root.destroy).grid(column=1,row=1)

tk.Button(frm, text="Analytics").grid(column=1,row=1)
tk.Button(frm, text="Charts").grid(column=2,row=1)
tk.Button(frm, text="Workout").grid(column=3,row=1)



root.mainloop()
