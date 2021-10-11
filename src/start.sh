exec python3 manage.py makemigrations &
exec python3 manage.py migrate &
exec python manage.py runserver 0.0.0.0:8001 --noreload