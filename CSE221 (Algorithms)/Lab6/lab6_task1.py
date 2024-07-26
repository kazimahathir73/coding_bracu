i = open("D:\CSE221\lab6_input1.txt",'r')
o = open("D:\CSE221\lab6_output1.txt",'w')

import heapq

node_connect = i.readline().split()
node = int(node_connect[0])
connect = int(node_connect[1])

adj = []
for p in range(node+1):
    adj.append([])

count = 1   
for j in i.readlines():
    if count <= connect:
        j = j.split()
        adj[int(j[0])].append((int(j[1]),int(j[2])))
        count+=1
    else:
        start_node = int(j)

def dijkstra(adj_list, start):
    n = len(adj_list)
    dist = [float('inf')] * n
    dist[start] = 0
    visited = [False] * n
    pq = [(0, start)]
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        if visited[curr_node]:
            continue
        visited[curr_node] = True
        for j in adj_list[curr_node]:
            neighbor = j[0]
            weight = j[1]
            if not visited[neighbor] and curr_dist + weight < dist[neighbor]:
                dist[neighbor] = curr_dist + weight
                heapq.heappush(pq, (dist[neighbor], neighbor))
    return dist

dijkstra_dist = dijkstra(adj, start_node)
for k in range(node+1):
    if k != 0:
        if dijkstra_dist[k] != float('inf'):
            o.write(str(dijkstra_dist[k])+'  ')
        else:
            o.write('-1'+'  ')