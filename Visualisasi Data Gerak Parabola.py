#Model grafik parabola sejak titik awal hingga titik terjauh
#(sumbu Y awal dan akhir adalah 0 m ) dengan selisi waktunya sejak titik awal
#hingga akhir adalah 0,1 s. dengan kecepatan awal benda  1,4×10^−3  m/s.

import numpy as np
import matplotlib.pyplot as plt

alpha = np.radians(45)
g = 9.8
v0 = 1.4*10**3

v0x = v0*np.cos(alpha)
v0y = v0*np.sin(alpha)

X = ((v0**2)*np.sin(2*alpha))/(g)
Y = ((v0**2)*(np.sin(alpha)**2))/(2*g)
T = (2*v0*np.sin(alpha))/g

t = np.arange(0.0, T, 0.01)
y = v0y*t - 0.5*g*t**2
x = v0x*t

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set(xlabel='x (m)', ylabel= 'y (m)', title='Grafik Gerak Parabola')
ax.grid()
plt.show()
