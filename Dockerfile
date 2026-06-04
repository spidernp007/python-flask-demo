FROM registry.access.redhat.com/ubi9/python-311

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python","app.py"]
