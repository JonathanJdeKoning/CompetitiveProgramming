import sys
input = sys.stdin.readline
from collections import defaultdict
total = 0
trees= defaultdict(int)
while True:
    tree = input().strip()
    if not tree: break
    trees[tree] += 1
    total += 1
trees = sorted(trees.items())
for tree, num in trees:
    print(tree, 100*(num/total))