FROM python:3.9-slim


COPY . /app

WORKDIR /app/home

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8080

CMD ["python","app.py"]

