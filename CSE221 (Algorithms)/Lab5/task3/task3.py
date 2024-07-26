i = open("D:\CSE221\Lab5\input3_2.txt",'r')
o = open("D:\CSE221\Lab5\output3.txt",'w')

node_connect = i.readline().split()
node = int(node_connect[0])
connect = int(node_connect[1])

adj = {}
dfs_stack = []
for p in range(node+1):
    if p != 0:
        adj[p] = []
    
for j in i.readlines():
    j = j.split()
    adj[int(j[0])].append(int(j[1]))
    adj[int(j[1])].append(int(j[0]))

start_node = list(adj.keys())[1]
def dfs(visited, graph, node): 
    if node not in visited:
        o.write(str(node)+' ')
        visited.append(node)
        for i in graph[node]:
            dfs(visited, graph, i)

dfs(dfs_stack, adj, start_node)