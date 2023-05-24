# This is the error message returned after running option 2, the script still works properly !

Wordpress+Web\webscrapping-works> python .\emails_file3.py
Please select a search option:
1. Search using a URL
2. Use a CSV file with URLs to scrape for email addresses
2
Scraping pages: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 80/80 [00:33<00:00,  2.36it/s]
Writing to file: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:00<?, ?it/s] 
{'fn@domain.ie', 'frs@domain.ie'}
Traceback (most recent call last):
  File "C:\Users\david\AppData\Local\Programs\Python\Python311\Lib\site-packages\urllib3\connection.py", line 200, in _new_conn
    sock = connection.create_connection(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\david\AppData\Local\Programs\Python\Python311\Lib\site-packages\urllib3\util\connection.py", line 60, in create_connection
    for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\david\AppData\Local\Programs\Python\Python311\Lib\socket.py", line 962, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
socket.gaierror: [Errno 11001] getaddrinfo failed

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\david\AppData\Local\Programs\Python\Python311\Lib\site-packages\urllib3\connectionpool.py", line 790, in urlopen
    response = self._make_request(
               ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\david\AppData\Local\Programs\Python\Python311\Lib\site-packages\urllib3\connectionpool.py", line 491, in _make_request
    raise new_e
  File "C:\Users\david\AppData\Local\Programs\Python\Python311\Lib\site-packages\urllib3\connectionpool.py", line 467, in _make_request
    self._validate_conn(conn)
  File "C:\Users\david\AppData\Local\Programs\Python\Python311\Lib\site-packages\urllib3\connectionpool.py", line 1092, in _validate_conn
    conn.connect()
  File "C:\Users\david\AppData\Local\Programs\Python\Python311\Lib\site-packages\urllib3\connection.py", line 604, in connect
    self.sock = sock = self._new_conn()
                       ^^^^^^^^^^^^^^^^
  File "C:\Users\david\AppData\Local\Programs\Python\Python311\Lib\site-packages\urllib3\connection.py", line 207, in _new_conn
    raise NameResolutionError(self.host, self, e) from e
urllib3.exceptions.NameResolutionError: <urllib3.connection.HTTPSConnection object at 0x0000021C6F34DB30>: Failed to resolve 'www.robiotics.com' ([Errno 11001] getaddrinfo failed)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\david\AppData\Local\Programs\Python\Python311\Lib\site-packages\requests\adapters.py", line 486, in send
    resp = conn.urlopen(
           ^^^^^^^^^^^^^
  File "C:\Users\david\AppData\Local\Programs\Python\Python311\Lib\site-packages\urllib3\connectionpool.py", line 844, in urlopen
    retries = retries.increment(
              ^^^^^^^^^^^^^^^^^^
  File "C:\Users\david\AppData\Local\Programs\Python\Python311\Lib\site-packages\urllib3\util\retry.py", line 515, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='www.robiotics.com', port=443): Max retries exceeded with url: / (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x0000021C6F34DB30>: Failed to resolve 'www.electrobiotics.com' ([Errno 11001] getaddrinfo failed)"))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\david\OneDrive\Projects_Mac\scripts-chat-ai\Wordpress+Web\webscrapping-works\emails_file3.py", line 111, in <module>
    url_emails = extract_emails(url)
                 ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\david\OneDrive\Projects_Mac\scripts-chat-ai\Wordpress+Web\webscrapping-works\emails_file3.py", line 30, in extract_emails
    response = requests.get(url)
               ^^^^^^^^^^^^^^^^^
  File "C:\Users\david\AppData\Local\Programs\Python\Python311\Lib\site-packages\requests\api.py", line 73, in get
    return request("get", url, params=params, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\david\AppData\Local\Programs\Python\Python311\Lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\david\AppData\Local\Programs\Python\Python311\Lib\site-packages\requests\sessions.py", line 587, in request
    resp = self.send(prep, **send_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\david\AppData\Local\Programs\Python\Python311\Lib\site-packages\requests\sessions.py", line 701, in send
    r = adapter.send(request, **kwargs)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\david\AppData\Local\Programs\Python\Python311\Lib\site-packages\requests\adapters.py", line 519, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPSConnectionPool(host='www.iotics.com', port=443): Max retries exceeded with url: / (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x0000021C6F34DB30>: Failed to resolve 'www.electrobiotics.com' ([Errno 11001] getaddrinfo failed)"))