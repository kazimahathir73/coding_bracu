i = open("D:\CSE221\lab8_input1.txt",'r')
o = open("D:\CSE221\lab8_output1.txt",'w')

node_connect = i.readline().split()
node = int(node_connect[0])
connect = int(node_connect[1])

edges = []
  
for j in i.readlines():
    a, b, c = map(int, j.split())
    edges.append([a,b,c])

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def minimum_cost(n, edges):
    parent = list(range(n + 1))
    rank = [0] * (n + 1)

    # Sort the edges in non-decreasing order of their weights
    edges.sort(key=lambda x: x[2])

    mst = []
    total_cost = 0

    for u, v, w in edges:
        # Check if there is a path from u to v in the current MST
        if find(parent, u) == find(parent, v):
            continue

        # Add the edge to the MST and update the total cost
        mst.append((u, v))
        total_cost += w

        # Merge the two sets
        union(parent, rank, u, v)

    return total_cost

o.write(str(minimum_cost(node, edges)))
