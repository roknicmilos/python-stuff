"""
Downloads multiple sites by going through the list of site
URLs and making GET HTTP request for each of them using
threading (ThreadPoolExecutor).
"""
import requests
import threading

from concurrent.futures import ThreadPoolExecutor

from concurrency.data import urls
from concurrency.io_bound_program.utils import wrap_site_downloads

# threading.local() creates an object that looks like
# a global but is specific to each individual thread
thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        # requests.Session() is not thread-safe, which
        # is why a new Session is set to each thread
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


@wrap_site_downloads(
    url_count=len(urls),
    optimization="`threading`",
)
def run():
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for url in urls:
            futures.append(executor.submit(download_site, url))
        [future.result() for future in futures]
