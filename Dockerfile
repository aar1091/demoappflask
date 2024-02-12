FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 python3-pip

WORKDIR /app

COPY . .

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 8080

CMD ["python3", "app.py"]