#!/usr/bin/env python
#coding:utf-8
import prometheus_client
import redis
from prometheus_client import Gauge
from flask import Response,Flask

app = Flask(__name__)
queue_len = Gauge("www_site_queue_len","the len of redis_queue")

@app.route("/metrics")
def redis_conn():
    pool = redis.ConnectionPool(host="xxxxxxxxxxx",port=6379,db=0,password="avavavav")
    conn = redis.Redis(connection_pool=pool)
    queue_len_data = conn.llen("www_site")
    queue_len.set(queue_len_data)
    return Response(prometheus_client.generate_latest(queue_len),mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=9101)
