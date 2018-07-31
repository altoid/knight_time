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


def next_moves(loc):
    # loc is a 2-ple giving (row, column).
    deltas = [(-2, -1), (-2, 1),
              (-1, -2), (-1, 2),
              (1, -2), (1, 2),
              (2, -1), (2, 1)]

    moves = map(lambda d: tuple([sum(x) for x in zip(loc, d)]), deltas)
    moves = filter(lambda x: 0 <= x[0] < NSQUARES and 0 <= x[1] < NSQUARES, moves)
    for m in moves:
        yield m


def find_path(path, move):
    if state[move[0]][move[1]] == 'e':
        return path.append(move)

    if state[move[0]][move[1]] != 0:
        return

    results = []
    for m in next_moves(move):
        state[move[0]][move[1]] = 'v'
        path_copy = list(path)
        path_copy = path_copy.append(move)
        result = find_path(path_copy, m)
        if result:
            results.append(result)


def show_state(state):
    for r in xrange(NSQUARES):
        print "+---" * NSQUARES + "+"
        print "| %s |" % ' | '.join(map(str, state[NSQUARES - 1 - r]))
    print "+---" * NSQUARES + "+"


def shortest_path(from_loc, to_loc):
    # from_loc and to_loc are 2-ples
    for i in xrange(NSQUARES):
        state.append([0] * NSQUARES)
    state[from_loc[0]][from_loc[1]] = 's'
    state[to_loc[0]][to_loc[1]] = 'e'
    show_state(state)
    for m in next_moves(from_loc):
        find_path([from_loc], m)
