release: python3 manage.py makemigrations && python3 manage.py migrate
web: gunicorn economizaqui.wsgi --log-file -
