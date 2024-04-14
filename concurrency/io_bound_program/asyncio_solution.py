"""
Downloads multiple sites by going through the list of site
URLs and making GET HTTP request for each of them using
asyncio (async/await).
"""
import asyncio
import aiohttp

from concurrency.data import urls
from concurrency.io_bound_program.utils import async_wrap_site_downloads


async def download_site(session, url):
    async with session.get(url) as response:
        print("Read {0} from {1}".format(response.content_length, url))


@async_wrap_site_downloads(
    url_count=len(urls),
    optimization="`asyncio`",
)
async def download_all_sites():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


def run():
    # To await an asynchronous function in Python without making the caller
    # function asynchronous is a bit tricky, because the await keyword can
    # only be used inside an async function. However, you can run the
    # asynchronous function to completion using synchronous code by using an
    # event loop from `asyncio`.
    asyncio.run(download_all_sites())
