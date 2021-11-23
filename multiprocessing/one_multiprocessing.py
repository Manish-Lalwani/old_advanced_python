from multiprocessing import Process
import os
import time

def cube():
	print("Process 1 CUBE PID IS:", os.getpid())
	my_numbers = [x for x in range(100)]
	for x in my_numbers:
		print('%s cube is %s' % (x, x**3))
		time.sleep(1)

def square():
	print("Process 2 SQUARE PID IS:", os.getpid())
	my_numbers = [x for x in range(100)]
	for x in my_numbers:
		print('%s square is %s' % (x, x**2))
		time.sleep(1)



if __name__ == '__main__':
	print("Main PID id", os.getpid())
	p1 = Process(target=cube)
	p2 = Process(target=square)
	p1.start()
	p2.start()
	p1.join
	p2.join
	print ("Done")