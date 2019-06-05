import re


def validate_url(url, expected_domain):
    # TODO: logging
    url = url.strip()
    reg = r'^(?:https?://)?(?:www.)?(\w+)(?:.\w+)+(?:/\w*)*$'
    match = re.search(reg, url)
    if match is None:
        return False
    if match[1] == expected_domain:
        return True
    return False
