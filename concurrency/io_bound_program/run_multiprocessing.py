"""
Downloads multiple sites by going through the list of site
URLs and making GET HTTP request for each of them using
multiprocessing.
"""
import sys

import requests
import multiprocessing
import time

from data import urls
from utils import Args

session: requests.Session | None = None


def set_global_session():
    global session
    if not session:
        session = requests.Session()


def download_site(args):
    url = args[0]
    log = args[1]
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        if log:
            print(f"{name}:Read {len(response.content)} from {url}")


def download_all_sites(log):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        args_list = [(url, log) for url in urls]
        pool.map(download_site, args_list)


if __name__ == "__main__":
    script_args = Args(*sys.argv)
    start_time = time.time()
    print(f"Downloading {len(urls)} sites...")
    download_all_sites(script_args.verbose)
    duration = time.time() - start_time
    print(f"Downloaded {len(urls)} in {duration} seconds")
