import asyncio

async def get_after(delay, what):
    await asyncio.sleep(delay)
    return what

async def main():
    print(f"started at {time.strftime('%X')}")

    task1 = asyncio.create_task(get_after(1, 'hello'))
    task2 = asyncio.create_task(get_after(2, 'world'))

    t2 = await task2
    t1 = await task1

    print(t1, t2)

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())