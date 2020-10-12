import asyncio


async def another_func():
    print("another_func: sleeping...")
    await asyncio.sleep(5)


async def extra_func():
    print("extra_func: sleeping...")
    await asyncio.sleep(10)


async def main():
    # another_func will not block the execution until it is completed
    task1 = event_loop.create_task(another_func())
    task2 = event_loop.create_task(extra_func())
    # Insted of await for every single task;
    # use asyncio.wait([...])
    asyncio.wait([task1, task2])
    print("main: sleeping...")

if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())
    print("After running async function")
