import time
import concurrent.futures

def m1(p_name):
    print(f'PROCESS NAME {p_name} started')
    for i in range(10):
        print(f'PNAME {p_name}Count :{i}' )
        time.sleep(2)
    return f'PROCESS NAME {p_name} finished'

# starts first 8 process as the laptop is having 4cores(8threads) after finishing full 8 processes starts 9th and 10th #process will be executed in any order
with concurrent.futures.ProcessPoolExecutor() as executor: #using context manager auto joins all process so it waits for all process to complete and then the context manager is exited
    future_obj = executor.submit(m1,"p1") # functions returns future object
    print(f'PRINTING RESULT FIRST PROCESS {future_obj.result()}') # if future_obj.result called it will wait for the process to complete and then will go to next line
    future_obj1 = executor.submit(m1,"p2")
    future_obj2 = executor.submit(m1, "p3")
    future_obj3 = executor.submit(m1, "p4")
    future_obj5 = executor.submit(m1, "p5")
    future_obj6 = executor.submit(m1, "p6")
    future_obj7 = executor.submit(m1, "p7")
    future_obj8 = executor.submit(m1, "p8")
    future_obj9 = executor.submit(m1, "p9")
    future_obj10 = executor.submit(m1, "p10")


