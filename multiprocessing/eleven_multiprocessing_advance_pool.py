from concurrent.futures import ProcessPoolExecutor
import time
def m1(val):
    print("M1 executing")
    time.sleep(1)
    return val*val


if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=4) as executor:
        # results = executor.map(m1,range(10))
        # print(f'Type of result: {type(results)} ===== Result is:{results}')
        # for x in results:
        #     print(x)
        results =

