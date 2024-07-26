i = open("D:\CSE221\Lab2\input1b.txt",'r')
o = open("D:\CSE221\Lab2\output1b.txt", 'w')

idx_list = i.readline().split()
end = int(idx_list[0])
num = int(idx_list[1])

list1 = i.readline().split()

#time complexity = O(n)
flag = True
for i in list1:
    remainer = num - int(i)
    if str(remainer) in list1:
        o.write(str(list1.index(i)+1)+' ')
        o.write(str(list1.index(str(remainer))+1))
        flag = False
        break
        
if flag:
    print('Impossible')