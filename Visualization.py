
from datetime import datetime

from tkinter import *
from Agent import *
from InitializeValues import *
from scipy.stats import truncnorm

root = Toplevel()
root.geometry("620x200")

label1 = Label(root, text="Legal obligation")
label1.pack(side=TOP)
var1=IntVar();
def selectedValue1():
    label1.configure(text='Legal obligation - ' + str(var1.get()))
    print(str(var1.get()))
R11=Radiobutton(root, text="Low",padx = 20, variable=var1, value=1, command=selectedValue1);
R11.pack(anchor=W)
R12=Radiobutton(root,text="Medium",padx = 20, variable=var1, value=2, command=selectedValue1);
R12.pack(anchor=W)
R13=Radiobutton(root,text="High",padx = 20, variable=var1, value=3, command=selectedValue1);
R13.pack(anchor=W)

label2 = Label(root, text="Client demand")
label2.pack(side=TOP)
var2=IntVar();
def selectedValue2():
    label2.configure(text='Client demand - ' + str(var2.get()))
    print(str(var2.get()))
R21=Radiobutton(root, text="Low",padx = 20, variable=var2, value=1, command=selectedValue2);
R21.pack(anchor=W)
R22=Radiobutton(root,text="Medium",padx = 20, variable=var2, value=2, command=selectedValue2);
R22.pack(anchor=W)
R23=Radiobutton(root,text="High",padx = 20, variable=var2, value=3, command=selectedValue2);
R23.pack(anchor=W)

label3 = Label(root, text="Mimicry value")
label3.pack(side=TOP)
var3=IntVar();
def selectedValue3():
    label3.configure(text='Mimicry value - ' + str(var3.get()))
    print(str(var3.get()))
R31=Radiobutton(root, text="Low", padx = 20, variable=var3, value=1, command=selectedValue3);
R31.pack(anchor=W)
R32=Radiobutton(root,text="Medium", padx = 20, variable=var3, value=2, command=selectedValue3);
R32.pack(anchor=W)
R33=Radiobutton(root,text="High", padx = 20, variable=var3, value=3, command=selectedValue3);
R33.pack(anchor=W)
def quit():
    root.destroy();
    root.update();
    m=mimicry+(var3.get() + var2.get() + var1.get()) * 0.05;
    goDemo(m)
Button(root, text ="Hello", command = quit).pack(anchor=W)

tk.mainloop()



