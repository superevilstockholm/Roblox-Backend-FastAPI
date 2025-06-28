import asyncio
import aiohttp

from time import perf_counter

async def fetch(session: aiohttp.ClientSession, url: str):
    async with session.get(url) as response:
        return response.headers
    
async def main():
    start = perf_counter()
    tasks: list[asyncio.Task] = []
    async with aiohttp.ClientSession() as session:
        for _ in range(100):
            tasks.append(asyncio.create_task(fetch(session, "http://127.0.0.1:23237/api/test/async/3")))
        await asyncio.gather(*tasks)
    print(f"Time: {perf_counter() - start}")

asyncio.run(main())