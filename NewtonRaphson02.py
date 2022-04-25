import random
import math
import numpy as np
import matplotlib.pyplot as plt
random.seed(1)

x1 = []
x2 = []
prix1 = []
prix2 = []
n=1000000
eps = 10**-10
for i in range(n):
    x1.append(random.uniform(-1.0, 1.0))
    prix1.append(x1[i])
    x2.append(random.uniform(-1.0, 1.0))
    prix2.append(x2[i])



def f(x1, x2):
    return (x2**3)-(3.0*(x1**2)*x2)


def g(x1, x2):
    return (x1**3)-(3.0*x1*(x2**2))-5.0


def J00(x1, x2):
    return -6.0*x1*x2


def J01(x1, x2):
    return 3.0*(x2**2)-3.0*(x1**2)


def J10(x1, x2):
    return 3.0*(x1**2)-3.0*(x2**2)


def J11(x1, x2):
    return -6.0*x1*x2


def u1(x1, x2):
    det = J00(x1, x2)*J11(x1, x2)-J01(x1, x2)*J10(x1, x2)
    return -1.0/det*(J11(x1, x2)*f(x1, x2)-J01(x1, x2)*g(x1, x2))


def u2(x1, x2):
    det = J00(x1, x2)*J11(x1, x2)-J01(x1, x2)*J10(x1, x2)
    return 1.0/det*(J10(x1, x2)*f(x1, x2)-J00(x1, x2)*g(x1, x2))


repeat = []
for i in range(n):
    cnt = 0
    tmpx1 = 0
    tmpx2 = 0
    ux1 = 0
    ux2 = 0
    while True:
        if abs(f(x1[i], x2[i])) < eps and abs(g(x1[i], x2[i])) < eps:
            break
        cnt += 1
        tmpx1 = x1[i]
        tmpx2 = x2[i]
        ux1 = u1(x1[i], x2[i])
        ux2 = u2(x1[i], x2[i])
        x1[i] += ux1
        x2[i] += ux2
    repeat.append(cnt) 


z1=[]
z2=[]
index1=[]
tmp1=[]
#Blue
for i in range(n):
    if x1[i]>1.5:
        index1.append(i)
        z1.append(prix1[i])
        z2.append(prix2[i])
        tmp1.append(repeat[i])
      
v1=[]
v2=[]
index2=[]
tmp2=[]
#Green
for i in range(n):
    if x1[i]<0 and x2[i]>0:
        index2.append(i)
        v1.append(prix1[i])
        v2.append(prix2[i])
        tmp2.append(repeat[i])
     
u1=[]
u2=[]
index3=[]
tmp3=[]
#Red
for i in range(n):
    if x1[i]<0 and x2[i]<0:
        index3.append(i)
        u1.append(prix1[i])
        u2.append(prix2[i])
        tmp3.append(repeat[i])



#二次元
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(z1, z2, s=1, c='g')
ax.scatter(v1, v2, s=1, c='r')
ax.scatter(u1, u2, s=1, c='b')
plt.show()


"""
#二次元+繰り返し回数
fig = plt.figure()
ax = fig.add_subplot(111)
ax_cmap = ax.scatter(z1, z2, s=1, c=tmp1, cmap='inferno', alpha=0.1)
ax_cmap = ax.scatter(v1, v2, s=1, c=tmp2, cmap='inferno', alpha=0.1)
ax_cmap = ax.scatter(u1, u2, s=1, c=tmp3, cmap='inferno', alpha=0.1)
fig.colorbar(ax_cmap)
ax.set_xlabel('$x_1$', fontsize=10)
ax.set_ylabel('$x_2$', fontsize=10)
plt.show()
"""

"""
#三次元
a=np.array(u1)
b=np.array(u2)
c=np.array(tmp)
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(a, b, c, color='blue')
plt.show()
"""
