import math
import time
import Visualization
from Visualization import *
from numpy.random import choice
pChange=0.99;
options = [0, 1]
probabilitiesChange = [pChange, 1-pChange]
class ball:
    def __init__(self,x1,y1,x2,y2, color, speedx, speedy):
        self.ballId=canvas.create_oval(x1,y1,x2,y2, fill=color);
        self.xspeed=speedx;
        self.yspeed=speedy;
        self.color=color;
        self.coef=r;

def getColor(coef1, coef2, color1, color2):
    coefSum=coef1+coef2;
    c1 = (int(color2[0:2], 16)*coef1 + int(color1[0:2], 16)*coef2) / coefSum;
    c2 = (int(color2[2:4], 16)*coef1 + int(color1[2:4], 16)*coef2) / coefSum;
    c3 = (int(color2[4:6], 16)*coef1 + int(color1[4:6], 16)*coef2)/ coefSum;
    cs = str(hex(math.floor(c1)));
    cs = cs[2:len(cs)]
    if len(cs) < 2:
        cs = '0' + cs;
    cb = '#' + cs;
    cs = str(hex(math.floor(c2)));
    cs = cs[2:len(cs)]
    while len(cs) < 2:
        cs = '0' + cs;
    cb = cb + cs;
    cs = str(hex(math.floor(c3)));
    cs = cs[2:len(cs)]
    while len(cs) < 2:
        cs = '0' + cs;
    cb = cb + cs;

    return cb;
def moveBalls(canvas, balls):
    x=0
    rectid = canvas.create_oval(200, 300, 300, 400);
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
            color1=ball1.color[1:len(ball1.color)];
            coef1=ball1.coef;
            while j<len(balls):
                ball2=balls[j];
                pos2 = canvas.coords(ball2.ballId)
                coef2=ball2.coef;
                coefSum=coef1+coef2;
                xc2 = (pos2[1] + pos2[3]) / 2
                yc2 = (pos2[0] + pos2[2]) / 2
                if math.sqrt(math.pow((xc1-xc2),2)+math.pow((yc1-yc2),2)) < math.sqrt(math.pow(coef1,2)+math.pow(coef2,2))/2:
                    if(False):
                        if ball2.xspeed!=ball1.xspeed:
                            ball2.xspeed= (ball2.xspeed*coef2 + ball1.xspeed*coef1)/coefSum;
                            ball1.xspeed = (ball2.xspeed*coef2 + ball1.xspeed*coef1)/coefSum;
                        if ball2.yspeed!=ball1.yspeed:
                            ball2.yspeed = (ball2.yspeed*coef2 + ball1.yspeed*coef1) / coefSum;
                            ball1.yspeed = (ball2.yspeed*coef2 + ball1.yspeed*coef1) / coefSum;
                    color2=ball2.color[1:len(ball2.color)]
                    if ball1.color!=ball2.color:
                        a=1;
                        if (ball1.color=="white"):
                            ball2.color="black" if choice(options, p=probabilitiesChange) == 0 else "white"
                            canvas.itemconfig(ball2.ballId, fill=ball2.color)
                        else:
                            ball1.color = "black" if choice(options, p=probabilitiesChange) == 0 else "white"
                            canvas.itemconfig(ball1.ballId, fill=ball1.color)
                        #ball2.color=getColor(coef1, coef2, color1, color2);
                        #ball1.color=getColor(coef2, coef1, color1, color2);
                        #canvas.itemconfig(ball2.ballId, fill=ball2.color);
                        #canvas.itemconfig(ball1.ballId, fill=ball1.color);
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
        #if(x%50==0):
            #canvas.delete(rectid);
        #if (x % 75 == 0):
            #ectid = canvas.create_oval(200, 300, 300, 400);
        canvas.itemconfigure(t, text=x)
        tk.update();

        time.sleep(0.01)