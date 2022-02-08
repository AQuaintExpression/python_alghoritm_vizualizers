from turtle import colormode
from rich import print as rprint
import time

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def bubble_sort_one_step(our_list, i=0, j=0, sorted=False):
    # We go through the list as many times as there are elements
    for i in range(len(our_list)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(our_list) - 1):
            if our_list[j] > our_list[j+1]:
                # Swap
                our_list[j], our_list[j+1] = our_list[j+1], our_list[j]
                return sorted, i, j
    sorted = True
    return sorted, i, j


our_list = [19, 13, 6, 2, 18, 8]
sorted = False

while not sorted:
    sorted, i, j = bubble_sort_one_step(our_list)

    plt.plot([x for x in range(len(our_list))], our_list)
    colored_list = [str(x) for x in our_list]
    colored_list = [x if index not in [j, j+1] else '[bold red]' + x + '[/]' for index, x in enumerate(colored_list)]

    rprint(', '.join(colored_list))
    time.sleep(0.2)

plt.show()