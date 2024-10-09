import requests as rq
import logging
from rich.logging import RichHandler

# Set up logging for the RichHandler
logging.basicConfig(
    level="NOTSET",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)

# Set logging level for requests library to INFO to suppress debug messages
logging.getLogger("requests").setLevel(logging.INFO)

log = logging.getLogger("rich")


def bo1() -> None:
    url = "https://snips.sh/f/SuUcj6kw21?r=1"
    url2 = "https://snip.sh/f/SuUcj6kw21?r=1"
    timeout = 5  # Set the timeout to 5 seconds
    try:
        rez = rq.get(url, timeout=timeout)
        log.info(f"[{rez.elapsed.total_seconds()}s] Success - {rez.status_code}")
        print(rez.text)
    except rq.exceptions.Timeout:
        log.error("The request timed out")
    except Exception as e:
        log.exception(e)
