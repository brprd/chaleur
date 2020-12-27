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
ax.plot_surface(x, t, T)


ax.set_xlabel('$x$', fontsize=20)
ax.set_ylabel('$t$', fontsize=20)
ax.set_zlabel('$T$', fontsize=20)
ax.view_init(azim=30)

plt.show()