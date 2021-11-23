"""
With lock the array can be shared to multiple process and it lock os acquired by other process it waits for other process to release the lock
with Multiprocessing Array Inbuilt lock the values were not correct
used external lock now the values are correct
Lock not working with Inbuilt list getting incorrect values
"""
from multiprocessing import Process, Array, Lock
import time
lock = Lock()

arr = Array(typecode_or_type='d',size_or_initializer=10)
#arr = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1] # lock not working with list getting incorrect values
print(f'Before starting the process values are {arr[:]}')
def m1(process_name):
    print(f"Process {process_name} started:")
    for i in range(0,10):
        print(f'Process {process_name}: Arr value before write{arr[:]}')
        time.sleep(1)
        lock.acquire()
        arr[i] = arr[i]+1
        lock.release()
    print(f'Process {process_name}: Arr value after write{arr[:]}')
    print(f"Process {process_name} executed successfully")

def m2(process_name):
    print(f"Process {process_name} started:")
    for i in range(0,10):
        print(f'Process {process_name}: Arr value before write{arr[:]}')
        time.sleep(1)
        lock.acquire()
        arr[i] = arr[i]+1
        lock.release()
    print(f'Process {process_name}: Arr value after write{arr[:]}')
    print(f"Process {process_name} executed successfully")


def m3(process_name):
    print(f"Process {process_name} started:")
    for i in range(0,10):
        print(f'Process {process_name}: Arr value before write{arr[:]}')
        time.sleep(1)
        lock.acquire()
        arr[i] = arr[i]+1
        lock.release()
    print(f'Process {process_name}: Arr value after write{arr[:]}')
    print(f"Process {process_name} executed successfully")


def m4(process_name):
    print(f"Process {process_name} started:")
    while True:
        time.sleep(1)
        print(f'Process {process_name}: Arr value after write{arr[:]}')
    print(f"Process {process_name} executed successfully")


p1 = Process(target=m1,args=(1,))
p2 = Process(target=m2,args=(2,))
p3 = Process(target=m3,args=(3,))
p4 = Process(target=m4,args=(4,))

p1.start()
p2.start()
p3.start()
p4.start()