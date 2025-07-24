# coroutines

"""
Coroutines in Python are special functions defined with async def.
They allow asynchronous programming using await, async for, and async with.
These constructs enable non-blocking I/O and concurrent operations.
"""

import asyncio

# ---------------------------------------------
# Coroutine function definition
# ---------------------------------------------

async def greet_later():
    await asyncio.sleep(1)
    return "Hello after 1 second"

async def run_greet():
    message = await greet_later()
    print(message)

# asyncio.run(run_greet())

# ---------------------------------------------
# The async for statement
# ---------------------------------------------

class AsyncCounter:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.counter >= self.limit:
            raise StopAsyncIteration
        await asyncio.sleep(0.1)
        self.counter += 1
        return self.counter

async def iterate_async():
    async for number in AsyncCounter(3):
        print("Count:", number)

# asyncio.run(iterate_async())

# ---------------------------------------------
# The async with statement
# ---------------------------------------------

class AsyncFile:
    def __init__(self, path):
        self.path = path
        self.file = None

    async def __aenter__(self):
        self.file = open(self.path, "w")
        return self.file

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return False

async def write_file():
    async with AsyncFile("test.txt") as f:
        f.write("Async content written.")

# asyncio.run(write_file())
