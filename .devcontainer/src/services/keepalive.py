import os
import requests
import time
from src.utils.logger import get_logger

logger = get_logger(__name__)

def start_keepalive():
    endpoint = os.getenv("HEALTH_ENDPOINT", "http://localhost:8080/health")
    while True:
        try:
            requests.get(endpoint, timeout=10)
            logger.debug("Keepalive ping successful")
        except Exception as e:
            logger.warning(f"Keepalive failed: {str(e)}")
        time.sleep(240)  # 4 minutes
