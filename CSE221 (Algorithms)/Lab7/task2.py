i = open("D:\CSE221\Lab7\input2.txt",'r')
o = open("D:\CSE221\Lab7\output2.txt",'w')

itr_list = i.readline().split()
itr_num = int(itr_list[0])
person = int(itr_list[1])

list1 = []
for k in i.readlines():
    k = k.split()
    list1.append((int(k[0]),int(k[1])))

def set2(ele):
  return ele[1]
list1 = sorted(list1,key=set2)

final_list = []

end = [-1] * person
for p in range(itr_num):
    if p == 0:
        final_list.append(list1[p])
        end[0] = list1[p][1]
    else:
        for j in range(person):
            if list1[p][0] >= end[j]:
                final_list.append(list1[p])
                end[j] = list1[p][1]
                break

o.write(str(len(final_list)))