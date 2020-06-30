
import random
from scipy.stats import expon
import numpy as np;
from tkinter import *

width=1000;
height=500;
nAgents=50;
vlocations=3;
hlocations=3

tk=Tk();

mimicry=0.1;
canvas=Canvas(tk, width=width, height=height)
i=1;
while i<=hlocations-1:
    canvas.create_line(i*width/hlocations,0, i*width/hlocations,height)
    i=i+1
i=0
while i<=vlocations-1:
    canvas.create_line(0,i*height/vlocations, width, i*height/vlocations)
    i=i+1

tk.title("Bouncy Agents")
t=canvas.create_text(200,50,fill="darkblue",font="Times 20 italic bold",
                        text="")
canvas.pack()

vs=np.random.lognormal(mean=1, sigma=1, size=[nAgents,2])
vs=np.random.exponential(scale=7, size=[nAgents,2])
balls=[];
pColor=0.2;
r=15;
probabilitiesColor=[pColor,1-pColor]


lam=-1;
coef=10;
mu, sigma = 0, 1 # mean and standard deviation for colors
#cs=truncnorm(a=0., b=254/30, loc=127, scale=30).rvs(size=nAgents)
#mu, sigma = 20, 5 # mean and standard deviation for coefs
perturbation = np.random.normal(mu, sigma, [nAgents,2])
print(perturbation)





