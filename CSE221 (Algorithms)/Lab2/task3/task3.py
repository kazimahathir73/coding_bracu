def merge(a, b):
    end_list1 = len(a)
    list1 = a
    end_list2 = len(b)
    list2 = b

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
        
    return new_list
        
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergeSort(arr[:mid])
        a2 = mergeSort(arr[mid:])
        return merge(a1, a2)
    
i = open("D:\CSE221\Lab2\input3.txt",'r')
o = open("D:\CSE221\Lab2\output3.txt", 'w')
end = int(i.readline())
final_list = i.readline().split()
o.write(str(mergeSort(final_list)))