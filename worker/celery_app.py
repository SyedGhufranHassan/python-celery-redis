import os
from celery import Celery
celery_app = Celery('image_worker', broker=os.getenv('REDIS_URL'))
