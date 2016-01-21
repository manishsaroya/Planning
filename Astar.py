# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 21:46:45 2016

@author: manish
"""

# ----------
# Instructions:
#
# Defining a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, the function output is
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, function returns the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

from operator import add

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1


delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def search(grid, init, goal, cost):
    # To store the positon vectors which are explored.
    explored = []
    explored.append(init)
    # stores the explored position in [row, col,optimal path length] manner.
    explored_path_length = []
    # this avoid over writing of the list "explored"
    init2 = init[:]
    init2.append(0)
    explored_path_length.append(init2)
    while 1:
        for i in explored_path_length:
            # extracting the row and column
            explore = i[:2]
            for j in xrange(len(delta)):
                # stores new neighbours
                new_nei = map(add, explore, delta[j])
                # avoid the rows to go out of range
                if new_nei[0] >= 0 and new_nei[0] < len(grid):
                    # avoid the columns to go out of range
                    if new_nei[1] >= 0 and new_nei[1] < len(grid[0]):
                        # Make sure the neighbouring space is Navigable.
                        if grid[new_nei[0]][new_nei[1]] == 0:
                            # store the position if not previously visited
                            if new_nei not in explored:
                                explored.append(new_nei)
                                # avoid over writing of the list "explored"
                                new_nei2 = new_nei[:]
                                # incrementing the optimal path length
                                new_nei2.append(i[2]+1)
                                explored_path_length.append(new_nei2)
                                # check if goal has achieved or not
                                if new_nei == [4, 5]:
                                    # return [row, col,optimal path length].
                                    return new_nei2[2:] + new_nei2[:2]
        # if there is no path possible return the string "fail"
        return 'fail'

# calling the search function
a = search(grid, init, goal, cost)
print a
