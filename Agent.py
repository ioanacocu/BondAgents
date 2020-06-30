import math
import time

from InitializeValues import *
from numpy.random import choice

class ball:
    def __init__(self,x1,y1,x2,y2, color, speedx, speedy, boxX, boxY):
        self.ballId=canvas.create_oval(x1,y1,x2,y2, fill=color);
        self.xspeed=speedx;
        self.yspeed=speedy;
        self.color=color;
        self.boxX=boxX;
        self.boxY=boxY;
def moveBalls(canvas, balls, options, probabilitiesChange):
    x=0
    stillrunning=True
    interactions = 0;
    differentInteractions=0;
    changed=0;
    while stillrunning:
        x=x+1;
        stillrunning=False;
        # effect calculations
        i=0;
        while i < len(balls)-1:
            j=i+1
            ball1=balls[i];
            if ball1.color=="black":
                stillrunning=True;
            pos1 = canvas.coords(ball1.ballId)
            xc1=(pos1[1]+pos1[3])/2
            yc1=(pos1[0]+pos1[2])/2
            #neighbourBalls=[ball for ball in balls if ball.boxX==ball1.boxX and ball.boxY==ball1.boxY
                            #and not(ball.ballId==ball1.ballId)]
            while j<len(balls):
                ball2=balls[j];
                if ball2.boxX==ball1.boxX and ball2.boxY==ball1.boxY:
                    pos2 = canvas.coords(ball2.ballId)
                    xc2 = (pos2[1] + pos2[3]) / 2
                    yc2 = (pos2[0] + pos2[2]) / 2
                    if math.sqrt(math.pow((xc1-xc2),2)+math.pow((yc1-yc2),2)) < r:
                        interactions=interactions+1
                        if ball1.color!=ball2.color:
                            differentInteractions=differentInteractions+1;
                            if ball1.color=="white":
                                ball2.color="black" if choice(options, p=probabilitiesChange) == 0 else "white"
                                if ball2.color=="white":
                                    changed=changed+1;
                                    canvas.itemconfig(ball2.ballId, fill=ball2.color)

                            else:
                                ball1.color = "black" if choice(options, p=probabilitiesChange) == 0 else "white"
                                if ball1.color=="white":
                                    changed = changed + 1;
                                    canvas.itemconfig(ball1.ballId, fill=ball1.color)

                j=j+1;
            i=i+1;
        # movement
        if balls[len(balls)-1].color=="black":
            stillrunning=True;
        for ball in balls:
            canvas.move(ball.ballId, ball.xspeed, ball.yspeed)
            pos = canvas.coords(ball.ballId)
            if pos[3] >= (ball.boxY+1)*height/vlocations or pos[1] <= ball.boxY*height/vlocations:
                ball.yspeed = -ball.yspeed
            if pos[2] >= (ball.boxX+1)*width/hlocations or pos[0] <= (ball.boxX)*width/hlocations:
                    ball.xspeed = -ball.xspeed

        canvas.itemconfigure(t, text="Changed agents: "+str(changed)+" Steps: "+str(x)+ " \n Interactions: "+str(interactions)+ " Meaninglul interactions: "+str(differentInteractions))
        tk.update();

        time.sleep(0.01)

def goDemo(mimicry):
    pChange = mimicry;
    print(mimicry)
    options = [0, 1]
    probabilitiesChange = [1 - pChange, pChange]
    i = 0;

    while i < nAgents:
        boxX=random.randint(0,hlocations-1)
        boxY=random.randint(0,vlocations-1)
        #x1=((2*boxX+1)*width/hlocations)/2
        #y1 = ((2 * boxY + 1) * height / vlocations) / 2
        x1 = random.randint(math.ceil(boxX*width/hlocations)+2*r, math.ceil((boxX+1)*width/hlocations - 2*r));
        y1 = random.randint(math.ceil(2*r+boxY*height/vlocations), math.ceil((boxY+1)*height/vlocations - 2*r));
        direction = random.randint(0, 2);
        try:
            vx = coef * math.pow(i, lam) + perturbation[i][0]  # math.log(math.fabs(math.log(i)));
        except:
            vx = 0;
        # vx=math.log(1+i);
        print(vx)
        vx = (vx if direction == 1 else -vx);
        direction = random.randint(0, 2);
        # vy=(vs[i][1] if direction==1 else -vs[i][1]);
        try:
            vy = coef * math.pow(i, lam) + perturbation[i][1]  # math.log(math.fabs(math.log(i)));
        except:
            vy = 0;
        vy = (vy if direction == 1 else -vy);
        balls.append(
            ball(x1, y1, x1 + r, y1 + r, "white" if choice(options, p=probabilitiesColor) == 0 else "black", vx, vy, boxX, boxY));
        i = i + 1;
    moveBalls(canvas, balls, options,probabilitiesChange)