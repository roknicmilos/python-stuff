"""
Downloads multiple sites by going through the list of site
URLs and making GET HTTP request for each of them using
multiprocessing.
"""
import requests
import multiprocessing

from concurrency.data import urls
from concurrency.io_bound_program.utils import wrap_site_downloads

session: requests.Session | None = None


def set_global_session():
    global session
    if not session:
        session = requests.Session()


def download_site(url):
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"{name}:Read {len(response.content)} from {url}")


@wrap_site_downloads(
    url_count=len(urls),
    optimization="`multiprocessing`"
)
def run():
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site, urls)
