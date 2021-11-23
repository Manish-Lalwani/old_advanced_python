from multiprocessing import Process, Manager, Lock, Value
import time
"""
USING MANAGER ALLOW US TO USE THE ADBANCED PYTHON TYPE LIST DICTIONARY ETC AS SHARED 
BUT WITHOUT ETERNAL LOG VALUES ARE INCONSISTENT SO APPLIED EXTERNAL LOCK
"""

lock = Lock()

def m1(process_name):
    print(f"Process {process_name} started:")
    for i in range(0,10):
        print(f'Process {process_name}: Arr value before write{arr}')
        time.sleep(1)
        lock.acquire()
        arr[i] = arr[i]+1
        lock.release()
    print(f'Process {process_name}: Arr value after write{arr}')
    print(f"Process {process_name} executed successfully")

def m2(process_name):
    print(f"Process {process_name} started:")
    for i in range(0,10):
        print(f'Process {process_name}: Arr value before write{arr}')
        time.sleep(1)
        lock.acquire()
        arr[i] = arr[i]+1
        lock.release()
    print(f'Process {process_name}: Arr value after write{arr}')
    print(f"Process {process_name} executed successfully")


def m3(process_name):
    print(f"Process {process_name} started:")
    for i in range(0,10):
        print(f'Process {process_name}: Arr value before write{arr}')
        time.sleep(1)
        lock.acquire()
        arr[i] = arr[i]+1
        lock.release()
    print(f'Process {process_name}: Arr value after write{arr}')
    print(f"Process {process_name} executed successfully")


def m4(process_name):
    print(f"Process {process_name} started:")
    while all_process_completed_flag.value: #print while all 3 processes are not terminated
        print(f'Inside Process {process_name} all_process_completed_flag type {type(all_process_completed_flag)} value {all_process_completed_flag.value}')
        time.sleep(1)
        print(f'Process {process_name}: Arr value after write{arr}')
    print(f"Process {process_name} executed successfully")


if __name__ == "__main__":
    with Manager() as manager:
        arr = manager.list(range(10))
        all_process_completed_flag = Value('i',0)
        all_process_completed_flag.value = 1
        print(f'all_process_completed_flag type {type(all_process_completed_flag)} value {all_process_completed_flag.value}')
        print(arr)
        p1 = Process(target=m1,args=(1,))
        p2 = Process(target=m2,args=(2,))
        p3 = Process(target=m3,args=(3,))
        p4 = Process(target=m4,args=(4,))
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p1.join()
        p2.join()
        p3.join()
        if (p1.is_alive() == 0) and (p2.is_alive()== 0) and (p3.is_alive()== 0): # if all 3 process have terminated
            all_process_completed_flag.value = 0
        p4.join() # joined p4 later as if joined earlier the next statement will not be executed till the p4 process is not terminated