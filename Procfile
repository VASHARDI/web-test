web: pip freeze && gunicorn --pythonpath=./{{web-test-vashardi}} --bind 0.0.0.0:$PORT  --log-file - wsgi:application
