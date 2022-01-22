FROM python:3.8-alpine
EXPOSE 8000
RUN apk add --no-cache gcc python3-dev musl-dev
ADD . /Open_HMS
WORKDIR /Open_HMS
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
CMD ["python", "manage.py","runserver","0.0.0.0:8000"]
