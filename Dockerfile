FROM python:3.10

RUN apt-get update && apt-get install -y python3-pip

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]