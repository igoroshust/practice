# Считывание нескольких URL
import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = [
        'https://httpbin.org/delay/1', # Задержка 1с
        'https://httpbin.org/delay/2', # Задержка 2с
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        for result in results:
            print(result[:100])

asyncio.run(main())