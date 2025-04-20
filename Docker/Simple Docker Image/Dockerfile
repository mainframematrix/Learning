FROM python:3.10-alpine

WORKDIR /app

COPY /app/* /app
RUN chmod +x /app/hello-world.py

CMD [ "/app/hello-world.py" ]