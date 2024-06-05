from flask import Flask,request
from redis import Redis
import hashlib
import pickle
import base64
import urllib
app = Flask(__name__)
redis = Redis(host='127.0.0.1', port=6379)
def get_result(url):
    url_key=hashlib.md5(url.encode()).hexdigest()
    res=redis.get(url_key)
    if res:
        return pickle.loads(base64.b64decode(res))
    else:
        try:
            print(url)
            info = urllib.request.urlopen(url)
            res = info.read()
            pickres=pickle.dumps(res)
            b64res=base64.b64encode(pickres)
            redis.set(url_key,b64res,ex=300)
            return res
        except urllib.error.URLError as e:
            print(e) @app.route('/')
def hello():
    url = request.args.get("url")
    return '''%s ''' % get_result('http://'+url).decode(encoding='utf8',errors='ignore')
@app.route('/source')
def source():
    return