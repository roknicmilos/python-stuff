from datetime import datetime
from typing import Callable


def wrap_site_downloads(url_count: int, optimization: str = None) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            _print_start_message(url_count=url_count, optimization=optimization)
            func(*args, **kwargs)
            duration = datetime.now() - start_time
            _print_end_message(
                url_count=url_count,
                duration=duration.total_seconds(),
                optimization=optimization
            )

        return wrapper

    return decorator


def async_wrap_site_downloads(
        url_count: int,
        optimization: str = None
) -> Callable:
    def decorator(func: Callable) -> Callable:
        async def wrapper(*args, **kwargs):
            start_time = datetime.now()
            _print_start_message(url_count=url_count, optimization=optimization)
            await func(*args, **kwargs)
            duration = datetime.now() - start_time
            _print_end_message(
                url_count=url_count,
                duration=duration.total_seconds(),
                optimization=optimization
            )

        return wrapper

    return decorator


def _print_start_message(url_count: int, optimization: str = None) -> None:
    start_message = f"Downloading {url_count} sites"
    if optimization:
        start_message += f" using `{optimization}`..."
    else:
        start_message += " without any optimization..."

    print(start_message)


def _print_end_message(
        url_count: int,
        duration: float,
        optimization: str = None
) -> None:
    end_message = f"Downloaded {url_count} sites in {duration} seconds"
    if optimization:
        end_message += f" using `{optimization}`"
    else:
        end_message += " without any optimization"

    print(end_message)
