FROM python:3.11.7-slim

WORKDIR /imdb_app
COPY . /imdb_app
RUN pip install -r requirments.txt

CMD ["python", "main.py"]