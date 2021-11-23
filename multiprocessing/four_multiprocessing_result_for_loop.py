import time
import concurrent.futures

def m1(p_name):
    print(f'PROCESS NAME:{p_name} --- started')
    for i in range(5):
        print(f'PNAME:{p_name} Count :{i}' )
        time.sleep(2)
    return f'PROCESS NAME:{p_name} --- finished'

start_time = time.perf_counter()
future_obj_list = []

with concurrent.futures.ProcessPoolExecutor() as executor:
    for i in range(5):
        future_obj = executor.submit(m1,i)
        future_obj_list.append(future_obj)

print("\n**************")
#printing return statements of print objects waits for all object to complete and then this loop is executed
for f in concurrent.futures.as_completed(future_obj_list):
    print(f'Type of future_obj {type(future_obj_list[0])}============Type of result {type(f)}===============Result is: {f.result()}')

end_time = time.perf_counter()

print(f'Time Taken is {end_time - start_time} seconds')