FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

# Install cron
RUN apt-get update && apt-get -y install cron nano

CMD python manage.py runserver 0.0.0.0:$PORT
