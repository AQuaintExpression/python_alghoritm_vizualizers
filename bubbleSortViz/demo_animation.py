from matplotlib import animation
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


x_data = []
y_data = []

fig, ax = plt.subplots()
ax.set_xlim(0, 105)
ax.set_ylim(0, 12)
line, = ax.plot(0, 0)

def animation_frame(i, rand_list):
    print(rand_list) #for testing how arguments are passed

    x_data = [x for x in range(len(rand_list))]

    line.set_xdata(x_data)
    line.set_ydata(rand_list)
    for index, elem in enumerate(rand_list):
        rand_list[index] = rand_list[index] + 1

    return line, 


animation = FuncAnimation(
    fig,
    func=animation_frame,
    frames=np.arange(0, 10, 0.01),
    interval=500,
    fargs=([1, 2, 3],)
)

plt.show()