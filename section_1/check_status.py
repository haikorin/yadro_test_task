import requests
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-8s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)

URLS = [
    "https://tools-httpstatus.pickup-services.com/561",
    "https://tools-httpstatus.pickup-services.com/200",
    "https://tools-httpstatus.pickup-services.com/300",
    "https://tools-httpstatus.pickup-services.com/400",
    "https://tools-httpstatus.pickup-services.com/500"
]


def make_request(url):
    response = requests.get(url)
    if response.status_code < 400:
        logger.info(f"Url={url}, Status={response.status_code}, body={response.text.strip()[:200]}, elapsed={response.elapsed}")
    else:
        raise RuntimeError(f"Url={url}, Status={response.status_code}, body={response.text.strip()[:200]}")


if __name__ == "__main__":
    for url in URLS:
        try:
            make_request(url)
        except RuntimeError as e:
            logger.error(e)
