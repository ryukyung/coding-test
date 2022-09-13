# [4358] 생태학
from collections import defaultdict
import sys
trees = defaultdict(int)
count = 0
while True:
    treeName = sys.stdin.readline().rstrip()
    if not treeName:
        break
    trees[treeName] += 1
    count += 1
    
treeList = list(trees.keys())
treeList.sort()
for tree in treeList:
    result = trees[tree]/count*100
    print('%s %.4f' %(tree, result))
