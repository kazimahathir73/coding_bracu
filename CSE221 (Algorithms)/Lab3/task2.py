import heapq as hp

class heap():
    def __init__(self):
        self.heap_array = []
    def build(self,arr):
        for i in arr:
            hp.heappush(self.heap_array,i)
        print(self.heap_array)
        o.write(str(self.heap_array))
    def add(self,element):
        hp.heappush(self.heap_array,element)
        print(self.heap_array)
        o.write(str(self.heap_array))
    def delete(self):
        hp.heappop(self.heap_array)
        print(self.heap_array)
        o.write(str(self.heap_array))
    def heapify(self,h_array):
        hp.heapify(h_array)
        self.heap_array = h_array
        print(self.heap_array)
        o.write(str(self.heap_array))
    def heapSort(self,unsorted_array):
        new_array=[]
        for i in unsorted_array:
            hp.heappush(new_array,i)
        last_array = [hp.heappop(new_array) for i in range(len(new_array))]
        self.heap_array = last_array
        print(self.heap_array)
        o.write(str(self.heap_array))
    def sink(self,h_arr):
        hp._heapify_max(h_arr)
        self.heap_array = h_arr
        print(self.heap_array)
        o.write(str(self.heap_array))

i = open('D:\CSE221\Lab3\input2.txt','r')
o = open('D:\CSE221\Lab3\output2.txt','w')
array = [int(k) for k in i.readline().split()]
obj1 = heap()
obj1.build(array)
value = str(input('Enter the string: '))
if value == 'A':
    new_elm = int(input('Enter new number: '))
    obj1.add(new_elm)
if value == 'B':
    obj1.delete()
if value == 'S':
    obj1.heapSort(array)
    
i.close()
o.close()

