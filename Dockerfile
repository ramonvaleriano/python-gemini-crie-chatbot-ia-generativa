ARG PYTHON_VERSION=3.13.7
FROM python:${PYTHON_VERSION}

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
