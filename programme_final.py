import numpy as np
import scipy.integrate as si
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

Text=300
T0=1000


#### Méthode FCTS

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

nx=10
nt=1000
dx=1/nx
dt=1/nt
T=np.zeros(shape=(nx,nt))

#conditions initiales
Text=300
T0=1000


for i in range(nt):
    T[0][i]=Text
    T[nx-1][i]=Text
for i in range(nx):
    T[i][0]=T0


for i in range(nt-1):
    for j in range(1,nx-1):
        T[j][i+1]=(T[j+1][i]+T[j-1][i]-2*T[j][i])*dt/(dx*dx) + T[j][i]


ax = Axes3D(plt.figure())
x = np.linspace(0,1,nx)
t = np.linspace(0,1,nt)
x, t = np.meshgrid(x, t, indexing = 'ij')
ax.plot_surface(x, t, T, cmap='plasma')


ax.set_xlabel('$x$', fontsize=20)
ax.set_ylabel('$t$', fontsize=20)
ax.set_zlabel('$T$', fontsize=20)
ax.view_init(azim=30)

plt.show()
T1=T


#### Méthode EDO
def equation_de_chaleur(u,t):
    dudt = np.zeros(X.shape)
    for i in range(1, N-1):
        dudt[i] = (((u[i + 1] - 2*u[i] + u[i - 1]) / dx**2))

    return dudt

N = 10
M=1000
L = 1.0
X=np.linspace(0,L,num=N)

dx= L / (N - 1)

t=np.linspace(0.0, L, M)
# conditions initiales 1D
T=T0*np.ones(len(X))             # la température initiale
T[0]=Text                        # température au bord
T[-1]=Text                       # température au bord

def Euler(F,x0,T):
    n = len(T)
    X = [x0]
    for i in range(n-1):
        y = X[-1] + (T[i+1]-T[i])*F(X[-1],T[i])
        X.append(y)
    return np.array(X)


#solT=Euler(equation_de_chaleur,T,t)
solT = si.odeint(equation_de_chaleur, T, t)

ax = Axes3D(plt.figure())
t,X = np.meshgrid(t, X , indexing = 'ij')
ax.plot_surface(t,X, np.array(solT), cmap='plasma')
plt.show()
T2=solT.T

#### comparaison

ax = Axes3D(plt.figure())
x = np.linspace(0,1,nx)
t = np.linspace(0,1,nt)
x, t = np.meshgrid(x, t, indexing = 'ij')
ax.plot_surface(x, t, T1-T2, cmap='plasma')
plt.show()