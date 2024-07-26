i = open("D:\CSE221\Lab5\input1b_1.txt",'r')
o = open("D:\CSE221\Lab5\output1b.txt",'w')

ve_list = i.readline().split()
v = int(ve_list[0])
e = int(ve_list[1])
list_final = []

for j in range(v+1):
    if j != 0:
        list_final.append([])

for k in i.readlines():
    k = k.split()
    list_final[int(k[0])].append((int(k[1]),int(k[2])))
    
for l in range(len(list_final)):
    if len(list_final[l]) != 0:
        add = ''
        for m in range(len(list_final[l])):
            if m != len(list_final[l])-1:
                add += str(list_final[l][m])+','
            else:
                add += str(list_final[l][m])
        o.write(str(l)+' : '+ add+'\n')
    else:
        o.write(str(l)+' : '+'\n')
