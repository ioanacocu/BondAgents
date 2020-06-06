import math
import time
import Visualization
from Visualization import *
from numpy.random import choice
pChange=0.8;
options = [0, 1]
probabilitiesChange = [pChange, 1-pChange]
class ball:
    def __init__(self,x1,y1,x2,y2, color, speedx, speedy):
        self.ballId=canvas.create_oval(x1,y1,x2,y2, fill=color);
        self.xspeed=speedx;
        self.yspeed=speedy;
        self.color=color;
def moveBalls(canvas, balls):
    x=0
    while True:
        x=x+1;
        # effect calculations
        i=0;
        j=0;
        while i < len(balls)-1:
            j=i+1;
            ball1=balls[i];
            pos1 = canvas.coords(ball1.ballId)
            xc1=(pos1[1]+pos1[3])/2
            yc1=(pos1[0]+pos1[2])/2
            while j<len(balls):
                ball2=balls[j];
                pos2 = canvas.coords(ball2.ballId)
                xc2 = (pos2[1] + pos2[3]) / 2
                yc2 = (pos2[0] + pos2[2]) / 2
                if math.sqrt(math.pow((xc1-xc2),2)+math.pow((yc1-yc2),2)) < r:
                    if ball1.color!=ball2.color:
                        a=1;
                        if (ball1.color=="white"):
                            ball2.color="black" if choice(options, p=probabilitiesChange) == 0 else "white"
                            canvas.itemconfig(ball2.ballId, fill=ball2.color)
                        else:
                            ball1.color = "black" if choice(options, p=probabilitiesChange) == 0 else "white"
                            canvas.itemconfig(ball1.ballId, fill=ball1.color)

                j=j+1;
            i=i+1;
        # movement
        for ball in balls:
            canvas.move(ball.ballId, ball.xspeed, ball.yspeed)
            pos = canvas.coords(ball.ballId)
            if pos[3] >= height or pos[1] <= 0:
                ball.yspeed = -ball.yspeed
            if pos[2] >= width or pos[0] <= 0:
                    ball.xspeed = -ball.xspeed

        canvas.itemconfigure(t, text=x)
        tk.update();

        time.sleep(0.01)