i = open("D:\CSE221\Lab5\input2_3.txt",'r')
o = open("D:\CSE221\Lab5\output2.txt",'w')

node_connect = i.readline().split()
node = int(node_connect[0])
connect = int(node_connect[1])

adj = {}
bfs = []
queue = []
for p in range(node+1):
    if p != 0:
        adj[p] = []
    
for j in i.readlines():
    j = j.split()
    adj[int(j[0])].append(int(j[1]))
    adj[int(j[1])].append(int(j[0]))


bfs.append(list(adj.keys())[1])
queue.append(list(adj.keys())[1])
while len(queue) != 0:
  bfs_val = queue.pop(0) 
  o.write(str(bfs_val)+" ") 

  for i in adj[bfs_val]:
    if i not in bfs:
      bfs.append(i)
      queue.append(i)
    
