import asyncio
import time

async def main():
    print(1)
    task = asyncio.create_task(foo('text'))
    

    print(3)

async def foo(text):
    print(text)


asyncio.run(main())  