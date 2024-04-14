"""
Downloads multiple sites by going through the list of site
URLs and making GET HTTP request for each of them using
threading (ThreadPoolExecutor).
"""
import sys

import requests
import threading
import time

from concurrent.futures import ThreadPoolExecutor

from data import urls
from utils import Args

# threading.local() creates an object that looks like
# a global but is specific to each individual thread
thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        # requests.Session() is not thread-safe, which
        # is why a new Session is set to each thread
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(*args):
    session = get_session()
    url = args[0]
    log = args[1]
    with session.get(url) as response:
        if log:
            print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites, log):
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for url in sites:
            futures.append(
                executor.submit(download_site, url, log)
            )
        [future.result() for future in futures]


if __name__ == "__main__":
    script_args = Args(*sys.argv)
    start_time = time.time()
    print(f"Downloading {len(urls)} sites...")
    download_all_sites(urls, script_args.verbose)
    duration = time.time() - start_time
    print(f"Downloaded {len(urls)} in {duration} seconds")
