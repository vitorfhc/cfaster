import re
import logging

logger = logging.getLogger(__name__)

def url_filter(string, to_remove):
    if string.startswith(to_remove):
        return string[len(to_remove):]
    else:
        return string


def validate_url(url, expected_domain):
    logger.info('Validating url {} with expected domain {}'.format(
        url, expected_domain))
    url = url.strip()

    if expected_domain not in url:
        return False

    for leader in ('https://', 'http://', 'www', 'ftp://'):
        url = url_filter(url, leader)

    # Split off everything after the last domain
    url = url.split('/')[0]

    # ... and split up the domains
    url = url.split('.')

    if expected_domain not in url:
        return False

    for loc, url_piece in enumerate(url[::-1]):
        if loc == 0:
            continue
        elif loc == 1:
            if url_piece == expected_domain:
                return True
            if len(url_piece) > 3:
                return False

        elif loc == 2:
            if url_piece == expected_domain:
                return True
            if len(url_piece) > 3:
                return False

        else:
            return False

