import time
common = {
	'x': 10 
}


def global_variable_usage():

	for i in range(1000000):
		a =common['x']


def local_variable_usage():
	x =10
	for i in range(1000000):
		a =x




if __name__ == '__main__':
	start_time = time.time()
	global_variable_usage()
	end_time = time.time()
	print("total time taken is",end_time - start_time)

	start_time = time.time()
	local_variable_usage()
	end_time = time.time()
	print("total time taken is",end_time - start_time)