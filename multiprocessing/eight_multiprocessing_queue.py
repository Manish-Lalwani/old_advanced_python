import time
from multiprocessing import Process, Queue
"""
SAME AS PIPE BUT,
MULTIPLE PROCESS CAN READ WRITE DATA TO THE QUEUE BUT DATA ONCE WRITE IS DELETED FROM QUEUE SO OTHER PROCESS CANNOT THE SAME STATEMENT 
"""
q =Queue()

def m1(process_name):
    print(f"Process {process_name} started:")
    for i in range(5):
        q.put(f"Value {i} ")
    print(f"Process {process_name} executed successfully")

def m2(process_name):
    print(f"Process {process_name} started:")
    while True:
        print(f"Process {process_name} ==== {q.get()}")
    print(f"Process {process_name} executed successfully")


p1 = Process(target=m1,args=(1,))
p2 = Process(target=m2,args=(2,))
p3 = Process(target=m2,args=(3,))
p4 = Process(target=m1,args=(1,))
p1.start()
p2.start()
p3.start()
p4.start()