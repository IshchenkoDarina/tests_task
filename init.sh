touch /var/log/cron.log
(crontab -l ; echo "* * * * * /usr/local/bin/python /code/manage.py runcrons > /var/log/cron.log") | crontab
service cron start
python manage.py runserver 0.0.0.0:8000
#gunicorn tests_task.wsgi:application --bind 0.0.0.0:80
