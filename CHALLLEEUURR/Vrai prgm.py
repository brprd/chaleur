import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy.integrate import odeint
n=10
m=1000
T=np.zeros((n,m))
for t in range(1,m):
    T[0][t]=1

for i in range(1,n-1):
    for j in range(1,m-1):
        T[i][j+1]=1/2*(T[i+1][j]+T[i-1][j])
Y=np.linspace(0,1,num=1000)
X=np.linspace(0,1,num=10)
X0=X
print(X)
print(Y)

ax = Axes3D(plt.figure())
X, Y = np.meshgrid(X, Y , indexing = 'ij')
ax.plot_surface(X, Y, T)
plt.show()
Y0=np.zeros(10)
t=43
for i in range(0,10):
    Y0[i]=T[i][t]

"""plt.plot(X0,Y0)
plt.show()"""
def T(x,t):
    return 
    

def Euler(F,x0,T):
    n=len(T)
    X=[x0]
    for i in range(n-1):
        y=X[-1]+T[i+1]-T[i]*F(X[-1],T[i])
        X.append(y)
    return np.array(X)
    
    
    
    