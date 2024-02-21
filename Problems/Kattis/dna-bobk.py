#!/usr/bin/python3

BASES = "ATGC"

dnaString = input()

nQueries = int(input())

current = [0, 0, 0, 0]

counts = [current.copy()]

for i in range(len(dnaString)):
    letter = dnaString[i:i+1]
    current[BASES.find(letter)] += 1
#    if letter == 'A':
#        current[0] += 1
#    if letter == 'T':
#        current[1] += 1
#    if letter == 'G':
#        current[2] += 1
#    if letter == 'C':
#        current[3] += 1

    counts.append(current.copy())

diff = [0, 0, 0, 0]

for i in range(nQueries):
    (start, end) = map(int, input().split(' '))

    order = [0, 1, 2, 3]

    for j in range(4):
        diff[j] = counts[end][j] - counts[start-1][j]

    if diff[order[0]] < diff[order[1]] or (diff[order[0]] == diff[order[1]] and order[1] < order[0]):
        (order[0], order[1]) = (order[1], order[0])
    if diff[order[2]] < diff[order[3]] or (diff[order[2]] == diff[order[3]] and order[3] < order[2]):
        (order[2], order[3]) = (order[3], order[2])
    if diff[order[0]] < diff[order[2]] or (diff[order[0]] == diff[order[2]] and order[2] < order[0]):
        (order[0], order[2]) = (order[2], order[0])
    if diff[order[1]] < diff[order[3]] or (diff[order[1]] == diff[order[3]] and order[3] < order[1]):
        (order[1], order[3]) = (order[3], order[1])
    if diff[order[1]] < diff[order[2]] or (diff[order[1]] == diff[order[2]] and order[2] < order[1]):
        (order[1], order[2]) = (order[2], order[1])

    print(BASES[order[0]:order[0] + 1], end='')
    print(BASES[order[1]:order[1] + 1], end='')
    print(BASES[order[2]:order[2] + 1], end='')
    print(BASES[order[3]:order[3] + 1])
