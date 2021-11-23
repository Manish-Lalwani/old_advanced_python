import threading
from threading import Lock
import time
demo_obj_lock = Lock()

class demo:
    def __init__(self):
        self.obj =1





demo_obj = demo().obj
print("1111111111",demo_obj)

def read1():
    print("read started")
    global demo_obj
    while True:
        demo_obj_lock.acquire()
        print(f"value of demo_obj is {demo_obj}")
        demo_obj_lock.release()
        time.sleep(1)


def write1():
    print("write started")
    global demo_obj
    while True:
        demo_obj_lock.acquire()
        demo_obj +=1
        demo_obj_lock.release()
        print(f"after write {demo_obj}")
        time.sleep(1)




if __name__ == "__main__":
    # read1()
    # write1()
    # read1()

    t1 = threading.Thread(target=write1)
    t2 = threading.Thread(target=read1)

    t1.start()
    t2.start()
