"""
Downloads multiple sites by going through the list of site
URLs and making GET HTTP request for each of them using
asyncio (async/await).
"""
import asyncio
import sys
import time
import aiohttp

from data import urls
from utils import Args


async def download_site(session, url, log):
    async with session.get(url) as response:
        if log:
            print("Read {0} from {1}".format(response.content_length, url))


async def download_all_sites(sites, log):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url, log))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    script_args = Args(*sys.argv)
    start_time = time.time()
    print(f"Downloading {len(urls)} sites...")
    asyncio.get_event_loop().run_until_complete(download_all_sites(urls, script_args.verbose))
    # Instead of the asyncio.get_event_loop().run_until_complete()
    # tongue-twister, you can just use asyncio.run()
    duration = time.time() - start_time
    print(f"Downloaded {len(urls)} sites in {duration} seconds")
