#!/usr/bin/env python

import random

# find the shortest path between two squares on a chess board, with
# moves to be executed by a night.
#
#     +--+--+--+--+--+--+--+--+
#  7  |  |  |  |  |  |  |  |  |
#     +--+--+--+--+--+--+--+--+
#  6  |  |  |  |  |  |  |  |  |
#     +--+--+--+--+--+--+--+--+
#  5  |  |  |  |  |E |  |  |  |
#     +--+--+--+--+--+--+--+--+
#  4  |  |  |  |  |  |  |  |  |
#     +--+--+--+--+--+--+--+--+
#  3  |  |  |  |  |V |  |  |  |
#     +--+--+--+--+--+--+--+--+
#  2  |  |  |  |  |  |  |  |  |
#     +--+--+--+--+--+--+--+--+
#  1  |  |  |  |S |  |  |  |  |
#     +--+--+--+--+--+--+--+--+
#  0  |  |  |  |  |  |  |  |  |
#     +--+--+--+--+--+--+--+--+
#      0  1  2  3  4  5  6  7

# each time we make a move we mark a square visited.  
# if any of our moves is to 'E' then we win.  
# if all of our moves goes to a 'V' square then the path is no good.

state = []
NSQUARES = 8
all_moves = {}
path_count = 0
min_path_len = NSQUARES * NSQUARES + 1
shortest_path = None


def show_state(state):
    for r in xrange(NSQUARES):
        print "+---" * NSQUARES + "+"
        print "| %s |" % ' | '.join(map(str, state[NSQUARES - 1 - r]))
    print "+---" * NSQUARES + "+"


def next_moves(loc):
    # loc is a 2-ple giving (row, column).
    deltas = [(-2, -1), (-2, 1),
              (-1, -2), (-1, 2),
              (1, -2), (1, 2),
              (2, -1), (2, 1)]

    if loc not in all_moves:
        moves = map(lambda d: tuple([sum(x) for x in zip(loc, d)]), deltas)
        all_moves[loc] = filter(lambda x: 0 <= x[0] < NSQUARES and 0 <= x[1] < NSQUARES, moves)
    return all_moves[loc]


def find_path(current_path, move, level):
    global path_count
    global min_path_len
    global shortest_path

    if level > min_path_len:
        return

    # figure out every path to the 'e' square from here.  return a list of paths (list of list of (r, c)
    if state[move[0]][move[1]] == 'e':
        path_count += 1
        current_path.append(move)
        if level < min_path_len:
            min_path_len = level
            shortest_path = list(current_path)
        current_path.pop()
        return

    current_path.append(move)
    for m in next_moves(move):
        if state[m[0]][m[1]] == 'e':
            find_path(current_path, m, level + 1)
            break

        if state[m[0]][m[1]] != 0:
            continue

        state[m[0]][m[1]] = 'v'

        find_path(current_path, m, level + 1)

        state[m[0]][m[1]] = 0
    current_path.pop()


def shortest_path(from_loc, to_loc):
    global path_count
    
    # from_loc and to_loc are 2-ples
    for i in xrange(NSQUARES):
        state.append([0] * NSQUARES)
    state[from_loc[0]][from_loc[1]] = 's'
    state[to_loc[0]][to_loc[1]] = 'e'
    show_state(state)
    find_path([], from_loc, 0)
    print "%s ==> %s" % (from_loc, to_loc)
    print shortest_path
    print "done"


if __name__ == '__main__':
    from_loc = (random.randint(0, NSQUARES - 1), random.randint(0, NSQUARES - 1))
    to_loc = (random.randint(0, NSQUARES - 1), random.randint(0, NSQUARES - 1))
    shortest_path(from_loc, to_loc)
    