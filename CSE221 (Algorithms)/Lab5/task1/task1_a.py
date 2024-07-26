import numpy as np

i = open("D:\CSE221\Lab5\input1a_1.txt",'r')
o = open("D:\CSE221\Lab5\output1a.txt",'w')
ve_list = i.readline().split()
v = int(ve_list[0])
e = int(ve_list[1])

arr = np.zeros([v+1,v+1])
for j in i.readlines():
    j = j.split()
    arr[int(j[0])][int(j[1])] = int(j[2])
    
o.write(str(arr))