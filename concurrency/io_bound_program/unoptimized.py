"""
Downloads multiple sites by going through the list of site
URLs and making GET HTTP request for each of them.
"""
import requests

from concurrency.data import urls
from concurrency.io_bound_program.utils import wrap_site_downloads


def download_site(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


@wrap_site_downloads(url_count=len(urls))
def run():
    with requests.Session() as session:
        # It is possible to simply use get() from requests directly,
        # but creating a Session object allows requests to do some
        # fancy networking tricks and really speed things up.
        for url in urls:
            download_site(url, session)
