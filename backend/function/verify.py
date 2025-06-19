import re
from urllib.parse import urlparse

regex1=r'^[a-zA-Z0-9:/?&=#._\-@%~+,]+$'
regex2=r'^[a-zA-Z]+$'

# Check if is a valid url
def is_valid_url(url):
    if bool(re.fullmatch(regex1,url)):
        try:
            parsed=urlparse(url)
            if parsed.scheme in ("http","https") and parsed.netloc:
                return url
        except Exception:
            pass
        return None
    else:
        return None


def is_valid_short(route):
    return bool(re.fullmatch(regex2,route))