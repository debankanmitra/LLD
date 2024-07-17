import asyncio

async def fetchdata():
    print("start fetching")
    await asyncio.sleep(2)
    print("finish fetching")
    return {"key": "value"}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.75)

async def main():
    task1 = asyncio.create_task(fetchdata()) # when we create a tsk any coroutine which returns something this creates a future, future is like a promise in JS
    task2 = asyncio.create_task(print_numbers())
    value = await task1 # the reason there is printing value is because we are waiting for the task to finish, we waited for 2 seconds, so in that 2 seconds window other task is still running
    print(value)
    # await task2 # to get the full output we should wait for the second task to finish

asyncio.run(main())

"""
https://youtu.be/t5Bo1Je9EmE?si=qH_w85vDqmQ8bdJI

"""