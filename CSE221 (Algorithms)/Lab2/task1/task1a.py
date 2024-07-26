i = open("D:\CSE221\Lab2\input1a.txt",'r')
o = open("D:\CSE221\Lab2\output1a.txt", 'w')

idx_list = i.readline().split()
end = int(idx_list[0])
num = int(idx_list[1])

list1 = i.readline().split()


#Time complexity = O(n^2)
flag = True
for i in range(end):
    for k in range(i+1,end):
        sum1 = int(list1[i]) + int(list1[k])
        if sum1 == num:
            o.write(str(i+1)+' ')
            o.write(str(k+1))
            flag = False
            break
        
if flag:
    o.write('Impossible')
