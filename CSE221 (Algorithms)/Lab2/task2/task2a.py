i = open("D:\CSE221\Lab2\input2a.txt",'r')
o = open("D:\CSE221\Lab2\output2a.txt", 'w')

end_list1 = i.readline()
list1 = i.readline().split()
end_list2 = i.readline()
list2 = i.readline().split()

final_list = list1+list2

#time complexity = O(nlogn)
def mergeSort(nlist):
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1

mergeSort(final_list)
o.write(str(final_list))




