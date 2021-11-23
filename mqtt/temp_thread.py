import threading
import time



def display_thread():
    while True:
        time.sleep(1)
        print("Display thread")

def display_normal():
    while True:
        time.sleep(1)
        print("Display normal")




if __name__ == "__main__":
    x = threading.Thread(target= display_thread)
    x.start()
    print("control has been passed after executing thread")
    display_normal()
    print("control has been passed after executing normal")