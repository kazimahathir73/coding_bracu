i = open("D:\CSE221\Lab7\input1.txt",'r')
o = open("D:\CSE221\Lab7\output1.txt",'w')

itr_num = int(i.readline())

list1 = []
for k in i.readlines():
    k = k.split()
    list1.append((int(k[0]),int(k[1])))

def set2(ele):
  return ele[1]
list1 = sorted(list1,key=set2)

final_list = []

end = -1
for p in range(itr_num):
    if p == 0:
        final_list.append(list1[p])
        end = list1[p][1]
    else:
        if list1[p][0] >= end:
            final_list.append(list1[p])
            end = list1[p][1]
            
o.write(str(len(final_list))+'\n')
for j in final_list:
    o.write(str(j[0])+' '+str(j[1])+'\n')