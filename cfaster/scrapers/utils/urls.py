import re
import logging

logger = logging.getLogger(__name__)


def validate_url(url, expected_domain):
    logger.info('Validating url {} with expected domain {}'.format(
        url, expected_domain))
    url = url.strip()
    reg = r'^(?:https?://)?(?:www.)?(\w+)(?:.\w+)+(?:/\w*)*$'
    match = re.search(reg, url)
    if match is None:
        return False
    if len(match.groups()) and match.group(1) == expected_domain:
        return True
    return False
