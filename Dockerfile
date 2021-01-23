FROM python:3.8.5-alpine3.12

RUN apk update && apk add --no-cache py3-virtualenv gcc git python3-dev

WORKDIR /app

COPY . .

RUN chmod a+x sortApi/run-api.sh

RUN ./setup-python-env.sh

EXPOSE 5000
WORKDIR /app/sortApi
RUN chmod a+x run-api.sh
# CMD ./run-api.sh
RUN ll
ENTRYPOINT ["./run-api.sh"]