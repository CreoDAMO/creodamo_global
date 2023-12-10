# monitoring.py

from prometheus_client import start_http_server
import logging
from logstash_async.handler import AsyncLogstashHandler

def setup_monitoring():
    start_http_server(8000)
  
    logger = logging.getLogger('logstash')
    logger.setLevel(logging.INFO)
    logger.addHandler(AsyncLogstashHandler())
