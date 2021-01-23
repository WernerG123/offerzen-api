FROM python:3.8.5-alpine3.12

RUN apk update && apk add --no-cache py3-virtualenv gcc git python3-dev


WORKDIR /app

COPY . .

EXPOSE 5000
WORKDIR /app/sortApi
RUN ./setup-python-env.sh
RUN chmod a+x run-api.sh
RUN ls
RUN chmod 755 run-api.sh
ENTRYPOINT ["./run-api.sh"]