from http import Request
from httpclient import HTTPClient

_client = HTTPClient()


def client(custom_client=None):
    global _client
    if custom_client is None:
        return _client
    _client = custom_client
    return client


def get(url):
    result = client().get(url)
    return result


def head(url):
    req = Request('HEAD', url)
    result = client().request(req)
    if result.is_success:
        return result
    return None


def mirror(url, filename):
    client().mirror(url, filename)
