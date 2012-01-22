Creating your first client                                                                                                                            
--------------------------                                                                                                                            
                                                                                                                                                      
The client implement a web user agent. It is used to dispatch web requests.                                                                           
                                                                                                                                                      In the most common usage, the application creates a Client, and set the default values for the agent string, the timeout, etc. Then a Request object is created. The request is then passed to the client, which dispatch the request and a Response object is returned.                                    
                                                                                                                                                      
    >>> from http import *                                                                                                                            
    >>> client = Client()                                                                                                                             
                                                                                                                                                      
The default client will set the timeout to 60 seconds, the useragent string to 'python-http', and the number of redirection to follow to 7.           
                                                                                                                                                      
    >>> client = Client(agent='my uber application', timeout=10)                                                                                      
                                                                                           