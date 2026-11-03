import os
REDIS_URL = os.getenv('REDIS_URL')
TASK_QUEUE_NAME = os.getenv('TASK_QUEUE_NAME', 'default')
APP_SECRET = os.getenv('APP_SECRET')
