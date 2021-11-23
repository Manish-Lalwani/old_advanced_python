import time
import multiprocessing

start_time = time.time()
def f1(p_name):
    time.sleep(1)
    print(f'PROCESS NAME {p_name}')

process_list = []

#create and start process
for i in range(10):
    p = multiprocessing.Process(target=f1,args=[i])
    p.start()
    process_list.append(p)

#wait for processes to get complete before going executing next line in main process
for x in process_list:
    x.join()

end_time = time.time()
print(f"TIME TAKEN IS {end_time - start_time}")