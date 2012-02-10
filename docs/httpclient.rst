.. _httpclient:

HTTPClient
==========

.. module:: httpclient

Synopsis
--------

::

   >>> from http import Request
   >>> from httpclient import HTTPClient
   >>> request = Request('GET', 'http://lumberjaph.net')
   >>> client = HTTPClient()
   >>> client.request(request)
   >>> response = client.request(request)
   >>> print response.status
   200


Interface
---------

:class:`HTTPClient` instances have the following methods:

.. autoclass:: HTTPClient()
   :members:
   :undoc-members: