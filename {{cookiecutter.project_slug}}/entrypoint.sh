chmod +x /code/wait-for-it.sh
./wait-for-it.sh db:5432
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec "$@"