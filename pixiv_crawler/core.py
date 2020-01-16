import asyncio
from pixivpy_async import AppPixivAPI, PixivClient, PixivAPI


async def login():
    async with PixivClient() as client:
        aapi = PixivAPI(client=client)
        await aapi.login('id', 'pwd')
        illusts = await aapi.ranking('illust', 'daily', 1)
        print(illusts)


loop = asyncio.get_event_loop()
loop.run_until_complete(login())
loop.close()
