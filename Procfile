web: gunicorn mysite.wsgi --log-file -
worker: celery -A mysite worker
beat: celery -A mysite beat -S django