i = open("D:\CSE221\Lab2\input2b.txt",'r')
o = open("D:\CSE221\Lab2\output2b.txt", 'w')

end_list1 = i.readline()
list1 = i.readline().split()
end_list2 = i.readline()
list2 = i.readline().split()

#Time complexity = O(n)
new_list = []

if end_list1 < end_list2:
    min1 = end_list1
else:
    min1 = end_list2

i = 0
j = 0
while(i < int(min1) and j < int(min1)):
    if int(list1[i]) <= int(list2[j]):
        new_list.append(list1[i])
        i+=1
    else:
        new_list.append(list2[j])
        j+=1
      
if i == int(min1):
    new_list = new_list + list2[j:]
if j == int(min1):
    new_list = new_list + list1[i:]
    
o.write(str(new_list))
        
    