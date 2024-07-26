def findk(arr, low, high, k):

	if (k > 0 and k <= high - low + 1):

		pi = partition(arr, low, high)
		if (pi - low == k - 1):
			return arr[pi]
		if (pi - low > k - 1):
			return findk(arr, low, pi - 1, k)
		return findk(arr, pi + 1, high, k - pi + low - 1)


def partition(arr, low, high):
	pivot = arr[high]
	i = low
	for j in range(low, high):
		if (arr[j] <= pivot):
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
	arr[i], arr[high] = arr[high], arr[i]
	return i

i = open('D:\CSE221\Lab3\input1b.txt','r')
o = open('D:\CSE221\Lab3\output1b.txt','w')
array = [int(k) for k in i.readline().split()]
for i in i.readlines():
    k = int(i)
    ans = findk(array, 0, len(array)-1, k)
    print(ans)
    o.write(str(ans)+' ')
    
