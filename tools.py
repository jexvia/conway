import numpy as np

def cell_alive(threebythree):
    cellval = threebythree[1, 1]
    if cellval: # cell is currently alive
        neighbors = np.sum(threebythree) - 1 #don't include current cell
        return neighbors == 2 or neighbors == 3
    else:
        neighbors = np.sum(threebythree)
        return neighbors == 3

def step(arr):
    next_step = np.zeros_like(arr)
    nrows, ncols = arr.shape
    for row in xrange(1, nrows-1):
        for col in xrange(1, ncols-1):
            threebythree = arr[row-1:row+2, col-1:col+2]
            if cell_alive(threebythree):
                next_step[row, col] = 1
    return next_step

def glider(row, col):
    return np.array([[row+1, col], [row, col+1], [row, col+2], [row+1, col+2], [row+2, col+2]]).T

def blinker(row, col):
    return np.array([[r, c] for r in xrange(row, row+2) for c in xrange(col, col+2)] + [[r, c] for r in xrange(row+2, row+4) for c in xrange(col+2, col+4)]).T
