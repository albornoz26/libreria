import matplotlib.pyplot as plt
import numpy as np
##fig, ax =plt.subplots()
##ax.scatter(x=[1,2,3],y=[3,2,1])
##plt.savefig('diagrama')
##plt.show()
###---------------------------------------------------------------------------
##xi = [0,1,2,3,4,5,6]
##yi = [0,1,4,9,16,25,36]
##
##plt.plot(xi,yi)
##plt.show()
###---------------------------------------------------------------------------
##fig, ax = plt.subplots()
##ax.boxplot([1, 2, 1, 2, 3, 4, 3, 3, 5, 7])
##plt.show()
###---------------------------------------------------------------------------
##fig, ax = plt.subplots()
##ax.pie([5, 4, 3, 2, 1])
##plt.show()
###---------------------------------------------------------------------------
##fig, ax = plt.subplots()
##x = np.linspace(-3.0, 3.0, 100)
##y = np.linspace(-3.0, 3.0, 100)
##x, y = np.meshgrid(x, y)
##z = np.sqrt(x**2 + 2*y**2)
##ax.contourf(x, y, z)
##plt.show()
#####----------------------------------------------------------------------------
##fig, ax = plt.subplots()
##x = np.random.random((16, 16))
##ax.imshow(x)
##plt.show()
###----------------------------------------------------------------------------
##fig, ax = plt.subplots()
##x, y = np.random.multivariate_normal(mean=[0.0, 0.0], cov=[[1.0, 0.4], [0.4, 0.5]], size=1000).T
##ax.hist2d(x, y)
##plt.show()
###----------------------------------------------------------------------------
fig, ax = plt.subplots()
dias = ['L', 'M', 'MI', 'J', 'V', 'S', 'D']
temperaturas = {'Cali':[28.5, 30.5, 31, 30, 28, 27.5, 30.5], 'Bogota':[24.5, 25.5, 26.5, 25, 26.5, 24.5, 25]}
ax.plot(dias, temperaturas['Cali'], label='Cali')
ax.plot(dias, temperaturas['Bogota'],label='Bogota')
ax.legend(loc = 'upper right')
ax.set_xlabel("Días", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
ax.set_ylabel("Temperatura ºC", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:purple'})
ax.set_title('Evolución de la temperatura diaria', loc = "left", fontdict = {'fontsize':20, 'fontweight':'bold', 'color':'tab:blue'})
plt.savefig('diagrama')
plt.show()
