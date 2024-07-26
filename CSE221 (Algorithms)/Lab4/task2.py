max_value = 0
def max_element(arr):
	global max_value
	if len(arr) > 1:
		mid = len(arr)//2
		L = arr[:mid]
		R = arr[mid:]
		max_element(L)
		max_element(R)
		i = j = k = 0
		while i < len(L) and j < len(R):
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
				if R[j] > max_value:
					max_value = R[j]
			else:
				arr[k] = R[j]
				j += 1
				if L[i] > max_value:
					max_value = L[i]
			k += 1

		while i < len(L):
			if L[i] > max_value:
				max_value = L[i]
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			if R[j] > max_value:
				max_value = R[j]
			arr[k] = R[j]
			j += 1
			k += 1

i = open('D:\CSE221\Lab4\input2.txt','r')
o = open('D:\CSE221\Lab4\output2.txt','w')
size = i.readline()
array = [int(k) for k in i.readline().split()]

max_element(array)
o.write(str(max_value))
