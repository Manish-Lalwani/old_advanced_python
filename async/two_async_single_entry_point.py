import asyncio
import time



async def f1():
	print("Starting F1 Function")
	print("f1 going for sleep")
	await asyncio.sleep(3)
	print("f1 awake")

async def f2():
	print("Starting F2 Function")
	print("f2 going for sleep")
	await asyncio.sleep(3)
	print("f2 awake")


# HERE MAIN IS THE FUNCTION WHICH CALL OTHER ASYNC FUNCTION SO WE USE MAIN FUNCTION TO RUN THE PROGRAM
async def main():
	print("Starting Main Function")
	await f1() #will execute full f1 including its sleep and then only will go to next line
	print("======================== ========================")
	await f2()



if __name__ == "__main__":
	event_loop = asyncio.get_event_loop()
	event_loop.run_until_complete(main())
	event_loop.close()