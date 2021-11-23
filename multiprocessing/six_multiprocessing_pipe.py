import time
from multiprocessing import Process, Pipe


parent_con, child_con =Pipe() #returns 2 pipe object
def m1(p_name,parent_con):
    """Writes 10 statements to Pipe and exits the process"""
    print(f'PROCESS NAME {p_name} started')
    for i in range(10):
        parent_con.send("Hi THis is parent process P1")
    print("Process 1 executed fully")

def m2(p_name,child_con):
    """READS STATEMENTS FROM PIPE IN INTERVAL OF 1 SECOND (will keep on reading continuously in interval of 1 second)"""
    print(f"Process ID:{p_name} Child Process started")
    while True:
        print(f"Process ID:{p_name} {child_con.recv()}")
        time.sleep(1)

# #case1
# with concurrent.futures.ProcessPoolExecutor() as executor:
#     for i in range(5):
#         future_obj = executor.submit(m1,i)
#         print(future_obj.result()) # waits for every process to complete then moves to next iteration
#

# #case2
# future_obj_list = []
# with concurrent.futures.ProcessPoolExecutor() as executor:
#     for i in range(5):
#         future_obj = executor.submit(m1,i)
#         future_obj_list.append(future_obj)
#
#     print("@@@@@@@@@@@@@@@@@")
#     for f in concurrent.futures.as_completed(future_obj_list):
#         print(f.result())

p1 = Process(target=m1,args=(1,parent_con))
p2 = Process(target=m2,args=(2,child_con))
#p3 = Process(target=m2,args=(3,child_con)) #error when passing the pipe to third process
p1.start()
p2.start()
#p3.start()
