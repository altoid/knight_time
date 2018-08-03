#!/usr/bin/env python

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
NSQUARES = 5
all_moves = {}
path_count = 0

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


def find_path(current_path, move):
    global path_count

    # figure out every path to the 'e' square from here.  return a list of paths (list of list of (r, c)
    if state[move[0]][move[1]] == 'e':
        path_count += 1
        current_path.append(move)
        print current_path
        current_path.pop()
        return

    current_path.append(move)
    for m in next_moves(move):
        if state[m[0]][m[1]] == 'e':
            find_path(current_path, m)
            break

        if state[m[0]][m[1]] != 0:
            continue

        state[m[0]][m[1]] = 'v'

        find_path(current_path, m)

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
    find_path([], from_loc)
    print "done, found %s paths" % path_count
