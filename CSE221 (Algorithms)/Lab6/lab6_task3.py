i = open("D:\CSE221\lab6_input3.txt",'r')
o = open("D:\CSE221\lab6_output3.txt",'w')

node_connect = i.readline().split()
node = int(node_connect[0])
connect = int(node_connect[1])

adj = []
for p in range(node+1):
    adj.append([])
  
for j in i.readlines():
    j = j.split()
    adj[int(j[0])].append((int(j[1]),int(j[2])))


def dfs_all_paths(graph, start, start_weight, end, path=[], paths=[]):
    if start_weight != 0:
        path = path + [(start_weight, start)]
    if start == end:
        paths.append(path)
    for node,weight in graph[start]:
        if node not in path:
            dfs_all_paths(graph, node, weight, end, path, paths)
    return paths

possilbe_path_weight = dfs_all_paths(adj,1,0,node) 
max_path = []
for k in possilbe_path_weight:
    max_path.append(max(k)[0])
o.write(str(min(max_path)))