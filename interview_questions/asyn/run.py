"""Асинхронный код (неблокирующий)"""
# import asyncio
# import time
#
# async def async_sleep(seconds):
#     print(f'Начинаю спать на {seconds} сек...')
#     await asyncio.sleep(seconds) # Не блокирует! Переключается на другие задачи!
#     print(f'Проснулся после {seconds} сек...')
#
# # Запуск
# async def main(): # async def - делает функцию корутиной
#     start = time.time()
#     # gather запускает обе корутины параллельно
#     await asyncio.gather( # await - подожди, не блокируй, дай другим поработать
#         async_sleep(2),
#         async_sleep(1)
#     )
#     print(f'Общее время: {time.time() - start:.2f} сек.')
#
# # Запуск event loop (цикл событий)
# asyncio.run(main()) # ~2 сек. (максимум из задач)


"""Синхронный код (блокирующий)"""
# import time
#
# def sync_sleep(seconds):
#     print(f'Начинаю спать на {seconds} сек...')
#     time.sleep(seconds) # Блокируем весь поток!
#     print(f'Проснулся после {seconds} сек.')
#
# # Запуск
# start = time.time()
# sync_sleep(5)
# sync_sleep(4)
# print(f'Общее время: {time.time() - start:.2f} сек')


"""Пример ручного loop"""
# import asyncio
#
# async def task1():
#     print("Task 1 start")
#     await asyncio.sleep(1)
#     print("Task 1 end")
#
# async def task2():
#     print("Task 2 start")
#     await asyncio.sleep(0.5)
#     print("Task 2 end")
#
# # Ручной loop (для понимания)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.gather(task1(), task2())) # gather - параллельный запуск
# loop.close()