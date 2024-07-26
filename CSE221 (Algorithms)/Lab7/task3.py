i = open("D:\CSE221\Lab7\input3_1.txt",'r')
o = open("D:\CSE221\Lab7\output3.txt",'w')

itr_list = i.readline().split()
list_size = int(itr_list[0])
itr_num = int(itr_list[1])

size_list = []
parent_list = []
group_list= []

for j in range(list_size+1):
    parent_list.append(j)
    size_list.append(1)
   
for k in i.readlines():
    k = k.split()
    parent = int(k[0])
    child = int(k[1])
    if parent_list[child] != parent_list[parent]:
        parent_list[child] = parent_list[parent]
        if parent_list[parent] not in group_list:
            group_list.append(parent_list[parent])
        size_list[parent_list[parent]] += size_list[child]
       
    print(str(size_list[parent_list[parent]]))
    o.write(str(size_list[parent_list[parent]])+'\n')
    
print(group_list)