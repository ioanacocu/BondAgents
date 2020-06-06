
from Agent import *
from scipy.stats import expon


vs=np.random.lognormal(mean=1, sigma=1, size=[nAgents,2])
vs=np.random.exponential(scale=7, size=[nAgents,2])
balls=[];
pColor=0.1;
probabilitiesColor=[pColor,1-pColor]

lam=-1;
coef=10;
mu, sigma = 127, 30 # mean and standard deviation for colors
#cs=truncnorm(a=0., b=254/30, loc=127, scale=30).rvs(size=nAgents)
#mu, sigma = 20, 5 # mean and standard deviation for coefs
#cs = np.random.normal(mu, sigma, nAgents)


i=0;
while i <nAgents:
    x1=random.randint(r,width-r+1);
    y1=random.randint(r,height-r+1);
    direction = random.randint(0, 2);
    try:
        vx = coef*math.pow(i,lam)*(1-direction/100)#math.log(math.fabs(math.log(i)));
    except:
        vx=0;
    #vx=math.log(1+i);
    print(vx)
    vx=(vx if direction==1 else -vx);
    direction = random.randint(0, 2);
    #vy=(vs[i][1] if direction==1 else -vs[i][1]);
    try:
        vy =  coef*math.pow(i,lam)*(1-direction/100) #math.log(math.fabs(math.log(i)));
    except:
        vy=0;
    vy = (vy if direction == 1 else -vy);
    balls.append(ball(x1, y1, x1+r, y1+r, "white" if choice(options, p=probabilitiesColor)==0 else "black", vx, vy));
    i=i+1;
moveBalls(canvas, balls)
tk.mainloop()


