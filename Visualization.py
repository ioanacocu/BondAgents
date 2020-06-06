
import random

from datetime import datetime

from tkinter import *

import numpy as np;
from scipy.stats import truncnorm



tk=Tk();
width=1000;
height=500;
nAgents=50;
canvas=Canvas(tk, width=width, height=height)
tk.title("Bouncy Agents")
t=canvas.create_text(100,10,fill="darkblue",font="Times 20 italic bold",
                        text="Click the bubbles that are multiples of two.")
canvas.pack()
r=15;



