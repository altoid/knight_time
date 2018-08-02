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


def find_path(move):
    # figure out every path to the 'e' square from here.  return a list of paths (list of list of (r, c)
    if state[move[0]][move[1]] == 'e':
        return [[move]]

    results = []
    for m in next_moves(move):
        if state[m[0]][m[1]] == 'e':
            result = find_path(m)
            results = results + result
            break

        if state[m[0]][m[1]] != 0:
            continue

        state[m[0]][m[1]] = 'v'

        result = find_path(m)
        if result:
            results = result + results

        state[m[0]][m[1]] = 0

    # now stick <move> onto the front of each list we got back from the recursive calls
    final = []
    for r in results:
        f = [(move)] + r
        final.append(f)

    return final


def shortest_path(from_loc, to_loc):
    # from_loc and to_loc are 2-ples
    for i in xrange(NSQUARES):
        state.append([0] * NSQUARES)
    state[from_loc[0]][from_loc[1]] = 's'
    state[to_loc[0]][to_loc[1]] = 'e'
    show_state(state)
    results = find_path(from_loc)
    print min(results, key = lambda x: len(x))
    print "found %s paths" % len(results)
