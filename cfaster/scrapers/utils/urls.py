import re
import logging

logger = logging.getLogger(__name__)


def validate_url(url, expected_domain):
    logger.info(f'Validating url {url} with expected domain {expected_domain}')
    url = url.strip()
    reg = r'^(?:https?://)?(?:www.)?(\w+)(?:.\w+)+(?:/\w*)*$'
    match = re.search(reg, url)
    if match is None:
        return False
    if match[1] == expected_domain:
        return True
    return False
