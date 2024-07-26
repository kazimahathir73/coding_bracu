i = open("D:\CSE221\Lab5\input5_1.txt",'r')
o = open("D:\CSE221\Lab5\output5.txt",'w')

node_connect = i.readline().split()
node = int(node_connect[0])
connect = int(node_connect[1])
end_node = int(node_connect[2])

adj = {}
queue = []
visited = []
for p in range(node+1):
    if p != 0:
        adj[p] = []
    
for j in i.readlines():
    j = j.split()
    adj[int(j[0])].append(int(j[1]))
    adj[int(j[1])].append(int(j[0]))

start_node = list(adj.keys())[1]
def shortest_path(graph, start, end):
    queue.append(start)
    visited.append(start)
    parent = {start: None}            #parent dict for every vartex
    while queue:                      #normal bfs
        current = queue.pop(0)
        for i in graph[current]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
                parent[i] = current       #key -> vartex || value -> imd parent

    if end not in visited:        #start and end are disconnected
        return []

    path = [end]                     #list for path
    
    #started the back craking from end to start
    
    while path[-1] != start:                #find every edge parent untill start is found
        path.append(parent[path[-1]])       #finding parent of edge's imd parent and append to path
    path.reverse()                          #reverse the path for start to end
    
    return path

sht_path = shortest_path(adj,start_node,end_node)
o.write('Time: '+str(len(sht_path)-1)+'\n')
for k in range(len(sht_path)):
    if k == 0:
        o.write('Shortest Path: '+str(sht_path[k])+' ')
    else:
        o.write(str(sht_path[k])+' ')

