i = open("D:\CSE221\Lab5\input4_5.txt",'r')
o = open("D:\CSE221\Lab5\output4.txt",'w')

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
    
def has_cycle(graph):
    visited = {v: False for v in graph}
    color = {v: 'white' for v in graph}     #white -> Not visited
                                            #gray -> Visited but adjecents are not visted
                                            #black -> Fully visited    
    def dfs(node):
        visited[node] = True                #every node is true
        color[node] = 'gray'                #mark as gray as it is visited
        for i in graph[node]:
            if color[i] == 'white':         #condito(i)       #if white the run dfs 
                if dfs(i):                  #if dfs of any node returns 'Yes' the return 'Yes'
                    return 'Yes'
            elif color[i] == 'gray':        #condito(ii)      #cycle if any ajcent node of that current node is gray then that is cycle
                return 'Yes'
        color[node] = 'black'               #make nodes as black as all the adjecent are traversed
        return 'No'                         #else return 'No'
    
    for k in graph:                        #any node hasn't traversed or disconnected nodes dfs
        if not visited[k]:
            if dfs(k):
                return 'Yes'
    return 'No'

o.write(str(has_cycle(adj)))