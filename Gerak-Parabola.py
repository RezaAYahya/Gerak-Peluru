import math
import matplotlib.pyplot as plt
import numpy as np

#Konstanta
g = 9.806
t = 0
delta_t = 0.01
m = 0.15
vo = 50
teta = 35

#Tanpa Hambatan Udara
ax = 0
ay = -g
i = 0
k = 0
  # Numerik
x = np.zeros((600))
y = np.zeros((600))
vx = vo * math.cos(math.radians(teta))
vy = vo * math.sin(math.radians(teta))
  # Analitik
xA = np.zeros((600))
yA = np.zeros((600))
vxA = vo * math.cos(math.radians(teta))
vyA = vo * math.sin(math.radians(teta))

#Hambatan Udara
d = 0.0013
vxH = vo * math.cos(math.radians(teta))
vyH = vo * math.sin(math.radians(teta))
v = ((vx**2) + (vy**2))**0.5
axH = -(d/m)*(v*vx)
ayH = -g -(d/m)*(v*vy)
j = 0
xH = np.zeros((600))
yH = np.zeros((600))

# Menyiapkan data posisi tanpa hambatan udara (Numerik)
while x[i] >= 0 and y[i] >= 0:
  #Posisi x
  vx = vx + (ax * delta_t)
  x[i+1] = x[i] + (vx * delta_t)
  #Posisi y
  vy = vy + (ay * delta_t)
  y[i+1] = y[i] + (vy * delta_t)
  #increment
  i+= 1

# Menyiapkan data posisi dengan hambatan udara (Numerik)
while xH[j] >= 0 and yH[j] >= 0:
  #Posisi x
  vxH = vxH + (axH * delta_t)
  xH[j+1] = xH[j] + (vxH * delta_t)
  #Posisi y
  vyH = vyH + (ayH * delta_t)
  yH[j+1] = yH[j] + (vyH * delta_t)
  #increment
  j+= 1

# Menyiapkan data posisi tanpa hambatan udara (Analitik)
while True:
  # Posisi x
  xA[k] = xA[0] + (vxA * t) + (0.5 * ax * t**2)
  # Posisi y
  yA[k] = yA[0] + (vyA * t) + (0.5 * ay * t**2)
  # Increment
  k+=1
  t += delta_t
  # Stop Kondisi
  if yA[k-1] < 0:
    break


# Plotting
# Soal 1
plt.figure(1)
plt.plot(x,y,'r',label="Tanpa Hambatan Udara")
plt.plot(xH,yH,'b',label="Dengan Hambatan Udara")
plt.title("Grafik Gerak Parabola")
plt.xlabel("Jarak Tempuh Horizontal (m)")
plt.ylabel("Tinggi (m)")
plt.legend(bbox_to_anchor=(1.0, 1.0))

# Soal 2
plt.figure(2)
plt.plot(x, y, 'r', label="Numerik")
plt.plot(xA, yA, 'b', label="Analitik")
plt.title("Grafik Gerak Parabola")
plt.xlabel("Jarak Tempuh Horizontal (m)")
plt.ylabel("Tinggi (m)")
plt.legend(bbox_to_anchor=(1.0, 1.0))

# Menampilkan plot
plt.show()
