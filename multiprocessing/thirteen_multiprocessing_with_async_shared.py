"""
EXECUTING 3 PROCESS
P1 - SYNCHRONOUS PROCESS [[UPDATES SHARED DICTIONARY]]
P2 - ASYNCHRONOUS PROCESS (CALLS 2 ASYNC PROCESS)
   A1 - ASYNCIO_F1 [UPDATES SHARED DICTIONARY]
   A2 - ASYNCIO_F2 [UPDATES SHARED DICTIONARY]
P3 - SYNCHRONOUS PROCESS [DISPLAYING SHARED DICTIONARY DATA]

DICT1 - SHARED DICTIONARY BETWEEN ALL 3 PROCESSES

"""
from multiprocessing import Process, Manager, Value, Lock
import time
import asyncio

all_process_complete_lock = Lock()
dict1_lock =Lock()
async def asyncio_f1():
    print("asyncio_f1 started")
    for _ in range(10):
        print("---This is async f1")
        dict1_lock.acquire()
        dict1["count"] += 1
        dict1["process"] +='a1-'
        dict1_lock.release()
        await asyncio.sleep(1)


async def asyncio_f2():
    print("asyncio_f1 started")
    for _ in range(10):
        print("---This is async_f2")
        dict1_lock.acquire()
        dict1["count"] += 1
        dict1["process"] += 'a2-'
        dict1_lock.release()
        await asyncio.sleep(1)

#sync p1
def m1(process_name):
    for _ in range(10):
        print(f"Process:{process_name} This is synchronous func")
        dict1_lock.acquire()
        dict1["count"] += 1
        dict1["process"] += 'p1-'
        dict1_lock.release()
        time.sleep(1)

#async p2
def m2(process_name):
    print(f"Process:{process_name} This is async main func")
    dict1_lock.acquire()
    dict1["count"] += 1
    dict1["process"] += 'p2-'
    dict1_lock.release()
    event_loop = asyncio.get_event_loop()
    gather = asyncio.gather(asyncio_f1(),asyncio_f2())
    event_loop.run_until_complete(gather)

#sync p3
def m3(process_name): #display_dict_value
    while all_process_complete_flag.value:
        print(f"Process:{process_name} Values are: {dict1.values()}")
        time.sleep(1)


with Manager() as manager: #manager is i think only provides shared dictionary here
    all_process_complete_flag = Value('i',1) #shared variable
    dict1 = manager.dict() #shared dictionary
    dict1_lock.acquire() #acquiring lock for shared dictionary
    dict1["count"] = 1
    dict1["process"] = 'main-'
    dict1_lock.release() #release lock after updating dictionary

    #creating 3 processes 2nd process calls async function or co-routine
    p1 =Process(target=m1,args=(1,))
    p2 = Process(target=m2,args=(2,))
    p3 = Process(target=m3,args=(3,))

    #starting processes
    p1.start()
    p2.start()
    p3.start()

    #joining process so that the main thread waits for them to complete
    p1.join()
    p2.join()
    if (p1.is_alive() == False) and (p2.is_alive() == False): #if p1 and p2 completed sets flag to false so that p3 process can be terminated
        all_process_complete_flag.value = 0
    p3.join() # have joined p3 afterwards as if joined before the if statement will never be executed and it will run on infinity




