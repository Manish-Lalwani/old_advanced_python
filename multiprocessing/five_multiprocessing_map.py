import time
import concurrent.futures

start_time = time.perf_counter()

def m1(p_name):
    print(f'PROCESS NAME {p_name} started')
    for i in range(5):
        print(f'PNAME {p_name}Count :{i}' )
        time.sleep(2)
    return f'PROCESS NAME {p_name} finished'




#case1
with concurrent.futures.ProcessPoolExecutor() as executor:
    range1 = [0,1,2,3,4,5]
    results = executor.map(m1,range1)
    print(f'Type of result: {type(results)} ===== Result is:{results}')

    for x in results:
        print(x)

"""
OUTPUT WITH MAP: #it prints the result in order the process were started
PROCESS NAME 0 finished
PROCESS NAME 1 finished
PROCESS NAME 2 finished
PROCESS NAME 3 finished
PROCESS NAME 4 finished
PROCESS NAME 5 finished

"""
#case2
# future_obj_list = []
# with concurrent.futures.ProcessPoolExecutor() as executor:
#     for i in range(6):
#         future_obj = executor.submit(m1,i)
#         future_obj_list.append(future_obj)
#
#     for x in concurrent.futures.as_completed(future_obj_list):
#         print(x.result())


"""
OUTPUT WITH AS COMPLETED: # it prints the results as completed and not in the order of execution    

PROCESS NAME 2 finished
PROCESS NAME 1 finished
PROCESS NAME 4 finished
PROCESS NAME 0 finished
PROCESS NAME 5 finished
PROCESS NAME 3 finished

"""