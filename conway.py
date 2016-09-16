#! /usr/bin/env python
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import tools

def display_cells(arr, ax):
    nrows, ncols = arr.shape
    for i in xrange(nrows):
        for j in xrange(ncols):
            if arr[i, j]:
                ax.add_patch(patches.Rectangle((j, i), 1, 1, facecolor='black'))
    ax.grid(True)
    ax.set_aspect('equal')
    ax.set_xlim(0, ncols)
    ax.set_ylim(0, nrows)
    ax.set_xticks(np.arange(0, 100))
    ax.set_yticks(np.arange(0, 100))
    ax.set_xticklabels([])
    ax.set_yticklabels([])

def show(arr, ax, pause=.2):
    display_cells(arr, ax)
    plt.show(block=False)
    plt.pause(pause)
    plt.close()

def main():
    arr = np.zeros((100, 100))
    print tools.glider(90, 10)
    print tools.blinker(40, 80)
    arr[tools.glider(90, 10)] = 1
    arr[tools.blinker(40, 80)] = 1
    plt.rc('grid', linestyle="-", color='grey')
    while True:
        fig, ax = plt.subplots(facecolor='white')
        show(arr, ax)
        arr = tools.step(arr)

if __name__ == '__main__':
    main()
