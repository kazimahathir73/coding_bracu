def count_alien(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, count_left = count_alien(arr[:mid])
    right, count_right = count_alien(arr[mid:])
    merged, inv_merge = merge(left, right)

    return merged, count_left + count_right + inv_merge

def merge(left, right):
    i = j = 0
    num = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            num += len(left) - i
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, num


i = open('D:\CSE221\Lab4\input3.txt','r')
o = open('D:\CSE221\Lab4\output3.txt','w')
size = i.readline()
array = [int(k) for k in i.readline().split()]
count = count_alien(array)[1]
o.write(str(count))