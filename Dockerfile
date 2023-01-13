#FROM python:3.8-slim-buster
#
#COPY . /app
#WORKDIR /app
#
#RUN pip install --upgrade pip
#RUN pip install -r requirements.txt
#
#CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
#

FROM python:3.10-buster

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
