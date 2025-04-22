#digital clock
import tkinter as tk
from time import strftime


"""
`strftime` stands for **String Format Time**, and it allows 
you to customize the way date and time are displayed.
The statement `from time import strftime` is 
used to import the `strftime` function from Python's 
built-in `time` module. The `strftime` function is typically 
used for formatting date and time objects into string
 representations based on a format string.

"""
root = tk.Tk()
#tk se ek root window banate hai
c
def time():
    string = strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000,time) #time and date ko har second change karta hai

#root window ke anadar dalega and font size clr ayega
label=tk.Label(root,font=('calibri',50,"bold"),background="black",foreground="white")
label.pack(anchor="center")
time()
root.mainloop()