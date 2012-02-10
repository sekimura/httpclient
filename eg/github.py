from httpclient import HTTPClient
from http import Request, Response, Url
import unittest
import json


class GitHubClient(object):

    def __init__(self, user_agent=None, base_url='https://api.github.com'):
        self.base_url = base_url
        if user_agent is None:
            self._user_agent = HTTPClient()
        else:
            self._user_agent = user_agent

    @property
    def user_agent(self):
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        self._user_agent = user_agent

    def get_user(self, username):
        endpoint = Url(self.base_url)
        endpoint.path.append('users')
        endpoint.path.append(username)
        request = Request('GET', endpoint)
        response = self.user_agent.request(request)
        if response.is_success:
            return json.loads(response.content)
        else:
            raise Exception(response.status_line)


def _cb(request):
    response = Response(200, content=json.dumps({'name': 'batman'}))
    return response


class Test(unittest.TestCase):

    def testName(self):
        ua = HTTPClient()
        ua.add_handler('request_send', _cb)
        client = GitHubClient(user_agent=ua)
        res = client.get_user('franckcuny')
        self.assertEqual(res['name'], 'batman')


if __name__ == '__main__':
#    gh = GitHubClient()
#    res = gh.get_user('franckcuny')
#    print res['name']
    unittest.main()