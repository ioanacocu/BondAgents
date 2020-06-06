
from Agent import *


vs=np.random.lognormal(mean=1, sigma=1, size=[nAgents,2])

mu, sigma = 127, 30 # mean and standard deviation for colors
cs=truncnorm(a=0., b=254/30, loc=127, scale=30).rvs(size=nAgents)
mu, sigma = 20, 5 # mean and standard deviation for coefs
cs = np.random.normal(mu, sigma, nAgents)
balls=[];


pColor=0.1;
probabilitiesColor=[pColor,1-pColor]

i=0;
while i <nAgents:
    x1=random.randint(r,width-r+1);
    y1=random.randint(r,height-r+1);
    direction = random.randint(0, 2);
    vx=(vs[i][0] if direction==1 else -vs[i][0]);
    direction = random.randint(0, 2);
    vy=(vs[i][1] if direction==1 else -vs[i][1]);
    balls.append(ball(x1, y1, x1+r, y1+r, "white" if choice(options, p=probabilitiesColor)==0 else "black", vx, vy));
    i=i+1;
moveBalls(canvas, balls)
tk.mainloop()


