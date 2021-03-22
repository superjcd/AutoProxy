'''
   将访问的ip存入到待检验的redisset中
'''
import redis
from flask import request, Flask, Response
import config

conn = redis.Redis(host=config.host, port=config.port, password=config.password)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    return "Hooya Proxy Recording System"


@app.route('/record/<key>', methods=['GET'])
def record(key):
    # breakpoint()
    if key == config.KEY:
        ip = request.remote_addr
        proxy = ip + ":" + config.port
        store_ip_to_set(conn, config.key, proxy)
        return proxy + '\n'
    else:
        return 'Invalid Key'

def store_ip_to_set(conn, key_name, ip):
    print("Adding Ip {} to redis key {}".format(ip, key_name))
    conn.zadd(key_name, {ip:config.max_score})
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)
