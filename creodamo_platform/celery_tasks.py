from celery import Celery
import logging
from config import AppConfig

app_config = AppConfig()
app = Celery("creodamo", broker=app_config.get_setting('CELERY_BROKER_URL'))
logger = logging.getLogger(__name__)

@app.task(bind=True, max_retries=3, default_retry_delay=60)
def process_task(self, data):
    try:
        return "Task completed"
    except Exception as exc:
        logger.error("Task failed, retrying...", exc_info=exc)
        raise self.retry(exc=exc)
