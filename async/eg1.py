import asyncio
import time


async def f1():
	y=1
	for x in range(30,40):
		print("f1:",x)
		y *= x
		await asyncio.sleep(1) #pauses the functions execution and passes the control to event_loop which decides which function/co-routine will be executed next
	return y


async def f2():
	y=1
	for x in range(50,60):
		print("f2",x)
		y *= x
		await asyncio.sleep(1)
	return y

async def f3():
	y=1
	for x in range(50,60):
		print("f3",x)
		y *= x
		res = await f1() #waits for xomplete execution of f1 in each iteration
		print("value returned from f1 is",res)
	return y


if __name__ == "__main__":
	start_time = time.time()
	event_loop = asyncio.get_event_loop()
	gather = asyncio.gather(f1(),f2(),f3())
	res = event_loop.run_until_complete(gather)
	print("Gathered result is:",res)
	duration = time.time() - start_time


# print("*********************")
# await f1()
# # await f2()
