import asyncio

# 获取事件循环
loop = asyncio.get_event_loop()

# 定义协程
async def myfunc(url):
    # await get_url(url)
    pass

tasks = [loop.create_task(myfunc(url)) for url in urls]

loop.run_until_complete(asyncio.wait(tasks))
