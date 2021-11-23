import time

#type hints
def th_add(num1:int, num2:int) -> str:
    print("Adding 2 numbers")
    return f' ADDITION OF 2 NUMBERS {num1+num2}'

#normal
def add(num1, num2):
    print("Adding 2 numbers")
    return f' ADDITION OF 2 NUMBERS {num1+num2}'



if __name__ == "__main__":
    start_time = time.perf_counter()
    print(th_add(5,7))
    end_time = time.perf_counter()
    print(f'TIME TAKEN FOR RUNNING STATIC TYPE HINT FUNCTION IS:{end_time-start_time}')

    start_time = time.perf_counter()
    print(add(5, 7))
    end_time = time.perf_counter()
    print(f'TIME TAKEN FOR RUNNING STATIC TYPE HINT FUNCTION IS:{end_time - start_time}')
