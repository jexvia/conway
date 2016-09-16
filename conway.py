#! /usr/bin/env python
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import tools

def display_cells(arr, ax):
    ax.imshow(arr, cmap='Greys', interpolation='None')

def setup_ax(ax, nrows, ncols):
    ax.grid(True)
    ax.set_aspect('equal')
    ax.set_xlim(0, ncols)
    ax.set_ylim(0, nrows)
    ax.set_xticks(np.arange(0, 100))
    ax.set_yticks(np.arange(0, 100))
    ax.set_xticklabels([])
    ax.set_yticklabels([])

def show(arr, ax, pause=.2):
    setup_ax(ax, *arr.shape)
    display_cells(arr, ax)
    plt.show(block=False)
    plt.pause(pause)
    plt.cla()

def main():
    arr = np.zeros((100, 100))
    arr[tools.glider(90, 10)] = 1
    arr[tools.blinker(40, 80)] = 1
    plt.rc('grid', linestyle="-", color='grey')
    fig, ax = plt.subplots(facecolor='white')
    while True:
        show(arr, ax)
        arr = tools.step(arr)

if __name__ == '__main__':
    main()
