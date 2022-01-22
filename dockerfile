FROM python:3.8
EXPOSE 8000
ENV PYTHONUNBUFFERED 1
ADD . /Open_HMS
WORKDIR /Open_HMS
RUN apt-get update
RUN pip install -U pip
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
CMD ["python", "manage.py","runserver","0.0.0.0:8000"]
