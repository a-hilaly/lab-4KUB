from flask import Flask
import time
import os
import sys
from redis import Redis, RedisError
import requests

app = Flask(__name__)

version = os.getenv("VERSION")
hostname = os.getenv("HOSTNAME")
redis_hostname = sys.argv[1]
postgres_hostname = sys.argv[2]

r = Redis(host=redis_hostname, db=0, socket_connect_timeout=2, socket_timeout=2)

@app.route("/hello")
def hello():
    print(time.time())
    return "hello world"


@app.route("/info")
def info():
    print("{0}: url=/info".format(time.time()))
    return "version={0} hostname={1}".format(version, hostname)

@app.route("/redis")
def redis():
    try:
        # Try to increment value "value"
        resp = "value: " + str(r.incr("value"))
    except RedisError:
        # If error probably cannot connect to redis
        resp = "cannot connect to redis\n"

    # return resp value or error
    return resp

@app.route("/postgres")
def postgres():
    # ping postgres
    r = requests.get("http://" + postgres_hostname + ":5432", timeout=2)

    return "postgres response: {0}".format(r.content)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)