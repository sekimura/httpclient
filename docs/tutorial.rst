Creating your first client
--------------------------

The client implement a web user agent. It is used to dispatch web requests.

In the most common usage, the application creates a Client, and set the default values for the agent string, the timeout, etc. 

Then a Request object is created. The request is then passed to the client, which dispatch the request and a Response object is returned.

    >>> from http import Request
    >>> from httpclient import HTTPClient
    >>> client = HTTPClient()
    >>> req = Request('GET', 'http://lumberjaph.net')
                                                                                                                                                      
The default client will set the timeout to 60 seconds, the useragent string to 'python-http', and the number of redirection to follow to 7.

    >>> client = Client(agent='my uber application', timeout=10)

How to use this library
-----------------------

For the purpose of this documentation, let's start with a simple client for the GitHub API.

::

    from httpclient import HTTPClient
    from http import Request, Url
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

::

    >>> gh = GitHubClient()
    >>> res = gh.get_user('franckcuny')
    >>> print res['name']
    'franck'

Setting the useragent
~~~~~~~~~~~~~~~~~~~~~

You should let the possibility for the developper to set its own ``user_agent``.

How to test
-----------

Now, we will add tests for this client.

::

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
            
If we execute these test, the callback ``cb`` will be called, and since it returns a class:``Response`` object, the request is never sent over the wire.