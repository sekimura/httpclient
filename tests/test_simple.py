from unittest2 import TestCase
from http import Response
from httpclient import HTTPClient
from httpclient.simple import (get, head, client)


def _cb(request):
    if request.method == 'GET':
        res = Response(200, content='everything is ok !')
    elif request.method == 'HEAD':
        res = Response(200, headers=[('Content-Length', 10)])
    return res


class TestSimple(TestCase):

    def setUp(self):
        self.url = "http://lumberjaph.net"
        custom_client = HTTPClient()
        custom_client.add_handler("request_send", _cb)
        client(custom_client)

    def test_get(self):
        result = get(self.url)
        self.assertTrue(result)
        self.assertEqual(result.status, 200)
        self.assertEqual(result.content, 'everything is ok !')

    def test_head(self):
        result = head(self.url)
        self.assertTrue(result)
        self.assertEqual(result.status, 200)
        self.assertEqual(result.content_length, 10)
