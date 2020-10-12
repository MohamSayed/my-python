"""
    aysnc - await mechanims in python
"""
import asyncio
import random


async def simple_function(id):
    rand_time = random.randint(1, 5)
    await asyncio.sleep(rand_time)
    print("completed: {} - seconds: {}".format(id, rand_time))


async def main():
    tasks = []
    for i in range(10):
        tasks.append(asyncio.ensure_future(simple_function(i)))
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
