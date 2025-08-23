ARG PYTHON_VERSION=3.13.7
FROM python:${PYTHON_VERSION}

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
