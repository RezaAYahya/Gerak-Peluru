import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

x_data = [0]
y_data = [0]
g = 9.806
t = 0
delta_t = 0.01
m = 0.15
vo = 50
teta = 35
vx = vo * math.cos(math.radians(teta))
vy = vo * math.sin(math.radians(teta))
ay = -g

fig, ax = plt.subplots()
ax.set_xlim(0, 250)
ax.set_ylim(0, 45)
line, = ax.plot(0, 0)


def animation_frame(t):
	x_data.append(vx*t)
	y_data.append(vy*t+(0.5*ay*t**2))

	line.set_xdata(x_data)
	line.set_ydata(y_data)
	return line,


ani = animation.FuncAnimation(fig, func=animation_frame,frames=np.arange(0, 587, 0.1), interval=10)
											
plt.title("Grafik Gerak Parabola tanpa Hambatan Udara (Analitik)")
plt.xlabel("Jarak Tempuh Horizontal (m)")
plt.ylabel("Tinggi (m)")
plt.grid()
plt.show()
