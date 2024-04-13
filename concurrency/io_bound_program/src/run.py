"""
Downloads multiple sites by going through the list of site
URLs and making GET HTTP request for each of them.
"""
import sys

import requests
import time

from data import urls
from utils import Args


def download_site(url, session, log):
    with session.get(url) as response:
        if log:
            print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites, log):
    with requests.Session() as session:
        # It is possible to simply use get() from requests directly,
        # but creating a Session object allows requests to do some
        # fancy networking tricks and really speed things up.
        for url in sites:
            download_site(url, session, log)


if __name__ == "__main__":
    script_args = Args(*sys.argv)
    start_time = time.time()
    print(f"Downloading {len(urls)} sites...")
    download_all_sites(urls, log=script_args.verbose)
    duration = time.time() - start_time
    print(f"Downloaded {len(urls)} in {duration} seconds")
