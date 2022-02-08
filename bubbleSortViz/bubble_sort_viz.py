import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

######### GLOBALS #########
iteration = 0
i = 0
j = 0



def bubble_sort_gen(our_list):
    # We go through the list as many times as there are elements
    global i
    global j
    for i in range(len(our_list)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        if len(our_list) == 1:
            return
        for j in range(len(our_list) - 1):
            if our_list[j] > our_list[j+1]:
                our_list[j], our_list[j+1] = our_list[j+1], our_list[j]
                yield our_list


our_list = [19, 13, 6, 2, 18, 8, 20, 14, 7, 3, 19, 9, 29, 23, 16, 12, 28, 18, 30, 24, 17, 13, 29, 19]
random.seed(time.time())
random.shuffle(our_list)
N = len(our_list)
generator = bubble_sort_gen(our_list)

#setting up plot
fig, ax = plt.subplots()
ax.set_title('Bubble sort')
ax.set_xlim(0, len(our_list))
ax.set_ylim(0, max(our_list) + 2)
text = ax.text(0.02, 0.95, "0", transform=ax.transAxes)

#creating rectangle list
bar_rects = ax.bar(range(len(our_list)), our_list, align="edge")


def update_fig(our_list, rects):
    global iteration
    for index, (rect, val) in enumerate(zip(rects, our_list)):
        rect.set_height(val)
        if index == j or index == j + 1:
            rect.set_color('red')
        else:
            rect.set_color('blue')
    iteration += 1
    text.set_text("# of operations: {}".format(iteration))

anim = FuncAnimation(
    fig, 
    func=update_fig,
    fargs=(bar_rects,), 
    frames=generator, 
    interval=200,
    repeat=False
    )
plt.show()






