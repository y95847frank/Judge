# Usage

## Preparation

#### MongoDB
1. Go to https://docs.mongodb.com/manual/administration/install-community/
2. Follow the instruction and get mongodb for your OS.
3. Use `mongod` to start the database.

#### Redis
1. Go to https://redis.io/
2. Follow the instruction and get redis for your OS.
3. Start your redis and make sure it can be accessed via port 6379.

#### RabbitMQ
1. Go to https://www.rabbitmq.com/
2. Follow the instruction and get RabbitMQ for your OS.
3. Start your RabbitMQ and make sure it can be accessed via port 15672.

#### RabbitMQ
1. Use `pip install celery` to install celery.
2. Use `celery -A tasks worker --loglevel=info` to start celery.

## Build server
```
# git clone [this repo]
cd judgeme/
npm install
```

## Run Server
```
node app.js
```
Then you can access judge system through `localhost:3001`

