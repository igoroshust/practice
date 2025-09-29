# I/O-bound - чтение файлов асинхронно
import asyncio
import aiofiles

async def read_file(filename):
    async with aiofiles.open(filename, 'r') as f:
        content = await f.read()
    return content

async def main():
    files = ['file1.txt', 'file2.txt']
    tasks = [read_file(f) for f in files]
    contents = await asyncio.gather(*tasks) # Читаем файлы параллельно
    for content in contents:
        print(content[:50])

asyncio.run(main())