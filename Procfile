web: gunicorn mysite.wsgi
worker: celery -A mysite worker
beat: celery -A mysite beat -S django