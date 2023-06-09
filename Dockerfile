FROM python:3.11.3-bullseye

WORKDIR /

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY ./app ./app

CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "80"]
