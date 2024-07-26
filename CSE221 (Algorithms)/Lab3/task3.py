import sorting as st
import time
import math
import matplotlib.pyplot as plt
import numpy as np

n = 13
x = [i for i in range(n)]
y = []
z = []

#using bubble sort
class doctor_serial_bubble:
    def __init__(self):
        pass
    def bubble_call(self,arr):
        self.last_list = []
        for k in arr:
            k = k.split()
            start = time.time()
            if k[0] != 'see' and k[1] != 'doctor':
                self.enqueue((int(k[1]),k[0]))
                st.bubble(self.last_list)
            else:
                self.seeDoctor()
            y.append(time.time()-start)

    def enqueue(self,element):
        self.last_list.append(element)
    def seeDoctor(self):
        if len(self.last_list) != 0:
            self.last_list.pop(0)
        else:
            return 'Empty'
    def printQueue(self):
        print_list = []
        for i in self.last_list:
            print_list.append(i[1])
        print(print_list)
        #o.write(str(print_list))
        
#using heap sort
class doctor_serial_heap:
    def __init__(self):
        pass
    def heap_call(self,arr):
        self.last_list = []
        for k in arr:
            k = k.split()
            start = time.time()
            if k[0] != 'see' and k[1] != 'doctor':
                self.enqueue((int(k[1]),k[0]))
                st.minheap(self.last_list)
            else:
                self.seeDoctor()
            z.append(time.time()-start)
              
    def enqueue(self,element):
        self.last_list.append(element)
    def seeDoctor(self):
        if len(self.last_list) != 0:
            self.last_list.pop(0)
        else:
            return 'Empty'
    def printQueue(self):
        print_list = []
        for i in self.last_list:
            print_list.append(i[1])
        print(print_list)
        o.write(str(print_list))
        
i = open('D:\CSE221\Lab3\input3.txt','r')
o = open('D:\CSE221\Lab3\output3.txt','w')
list_d = i.readlines()

obj_bubble = doctor_serial_bubble()
obj_bubble.bubble_call(list_d)
obj_bubble.printQueue()
obj_heap = doctor_serial_heap()
obj_heap.heap_call(list_d)
obj_heap.printQueue()

for i in range(1,len(y)):
  y[i] = y[i] + y[i-1]
  z[i] = z[i] + z[i-1]

x_interval = math.ceil(n/10)
plt.plot(x, y, 'r')
plt.plot(x, z, 'b')
plt.xticks(np.arange(min(x), max(x)+1, x_interval))
plt.xlabel('n-th position')
plt.ylabel('time')
plt.title('Comparing Time Complexity!')
plt.show()

i.close()
o.close()