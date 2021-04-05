FROM python:3.7-alpine
WORKDIR /code
COPY requirements.txt requirements.txt
COPY /src .
COPY /mongo ./mongo
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "./app.py"]