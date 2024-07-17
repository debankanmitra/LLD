import asyncio

# when we put async it works as a coroutine 
# await keyword in Python is used within an async function to pause the execution of the coroutine until the awaited asynchronous operation is complete. 
# await is non-blocking, meaning they do not hold up the execution of other tasks while they wait for some operation (like I/O) to complete.
async def main():
    print("Debankan")
    asyncio.create_task(finish()) # ideally when this function is waiting for something to happen, we should execute "print("Mitra")" without blocking it, here we use someting called "task"
    print("Mitra")

async def finish():
    print("finished")
    await asyncio.sleep(4) # sleep also creates a coroutine so it should be awaited
    print("closed")

# asyncio creates a event loop and add the coroutine into it
asyncio.run(main())