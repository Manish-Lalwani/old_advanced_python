"""
EXECUTING ASYNC AND SYNC FUNCTION TOGETHER

IN THIS PROGRAM THERE ARE 2 PROCESSES
FIRST PROCESS RUN 2 ASYNC FUNCTION ASYNCHRONOUSLY
SECOND FUNCTION RUNS SINGLE FUNCTION SYNCHRONOUSLY
"""

from multiprocessing import Process
import asyncio
import time

async def async_f1():
    for _ in range(10):
        print("This is async_f1")
        await asyncio.sleep(1)

async def async_f2():
    for _ in range(10):
        print("This is async_f2")
        await asyncio.sleep(1)

def m2():
    event_loop = asyncio.get_event_loop()
    gather = asyncio.gather(async_f1(),async_f2())
    res = event_loop.run_until_complete(gather)

def m1():
    for _ in range(10):
        print("This is synchronously function")
        time.sleep(1)



p1 = Process(target=m2)
p2 = Process(target=m1)

p1.start()
p2.start()
p1.join()
p2.join()



