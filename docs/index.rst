.. topic:: Easy-to-use HTTP client

    ``httpclient`` is a Python library to build HTTP client

Basic usage
===========

This module is heavily inspired by LWP::UserAgent

    >>> from httpclient import HTTPClient
    >>> from http import Request
    >>> request = Request('GET', 'http://lumberjaph.net')
    >>> cclient = HTTPClient()
    >>> response = cclient.request(request)
    >>> print response.status
    200

User Guide
==========

.. toctree::
   :maxdepth: 2

   contents
