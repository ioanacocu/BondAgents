def loguniform(low ,high, size, base):
    return np.power(base, np.random.uniform(low, high, size))

import matplotlib.pyplot as plt
from scipy import stats
vars=np.random.lognormal(mean=3, sigma=1, size=1000)
#vars=loguniform(0 ,100, 100, 2)
from numpy import random
#vars= random.exponential(scale=0.01, size=1000)
vars.sort();
vs=[]
sum=0;
for v in vars:
    vs.append(float(v))
    sum=sum+float(v)
#vars.sort();
count, bins, ignored = plt.hist(vars, 100, density=True, align='mid')
x = np.linspace(min(bins), max(bins), 100)
pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))
       / (x * sigma * np.sqrt(2 * np.pi)))
plt.plot(x, count, linewidth=2, color='r')
plt.axis('tight')
#plt.show()
print(sum/1000)
print(np.log(sum/1000))
print(vs)
print(count)
print(bins)
print(ignored)
#plt.plot(vs)
#plt.ylabel('some numbers')
plt.show()


#tk.mainloop()

red = random.randint(0,254);
    green = random.randint(0,254);
    blue = random.randint(0,254);
    coef=cs[i]#random.randint(0,1000);
    color = "#"
    cr = str(hex(red));
    cr= cr[2:len(cr)]
    while len(cr) < 2:
        cr = '0' + cr;
    cg = str(hex(green));
    cg= cg[2:len(cg)]
    while len(cg) < 2:
        cg = '0' + cg;
    cb = str(hex(blue));
    cb= cg[2:len(cb)];
    while len(cb) < 2:
        cb = '0' + cb;
    color=color+cr+cg+cb;