from collections import deque
i = open("D:\CSE221\Lab5\input7_1.txt",'r')
o = open("D:\CSE221\Lab5\output7.txt",'w')

total_node = int(i.readline())

tree = {}
for p in range(total_node+1):
    if p != 0:
        tree[p] = []

for j in i.readlines():
    j = j.split()
    tree[int(j[0])].append(int(j[1]))
print(tree)    

def bfs(graph, start):
    visited = [False] * (len(graph)+1)
    visited[start] = True
    queue = deque([start])
    level = -1  
    last = None  
    while queue:
        size = len(queue)
        level += 1
        for i in range(size):
            node = queue.popleft()
            last = node
            for k in graph[node]:
                if not visited[k]:
                    visited[k] = True
                    queue.append(k)
    return last, level


x, dist_x = bfs(tree, 1) 
y, dist_y = bfs(tree, x)

o.write(str(x)+' ')
o.write(str(y))
