FROM python:3.8.5-alpine3.12

RUN apk update && apk add --no-cache py3-virtualenv gcc git python3-dev

WORKDIR /app

COPY . .

RUN chmod a+x sortApi/run-api.sh

RUN ./setup-python-env.sh

EXPOSE 5000
RUN chmod a+x /app/sortApi/run-api.sh
WORKDIR /app/sortApi
CMD ./run-api.sh