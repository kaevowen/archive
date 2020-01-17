from tkinter import *
import tkinter

top = tkinter.Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar0 = IntVar()

C0 = Checkbutton(top, text = "Check All", variable = CheckVar0,
	onvalue = 1, offvalue = 0, height = 1, width = 20, justify = 'right')
C1 = Checkbutton(top, text = "Music", variable = CheckVar1,
	onvalue = 1, offvalue = 0, height=1,width = 20, justify = 'right')
C2 = Checkbutton(top, text = "Video", variable = CheckVar2,
	onvalue = 1, offvalue = 0, height=1,width = 20, justify = 'right')

C0.pack()
C1.pack()
C2.pack()

top.mainloop()