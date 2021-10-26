#!/usr/bin/env bash

AWS_ACCOUNT_ID=xxxxxxxxxx
NAME=twtr2telega
LOG_GROUP=twtr2telega
TAG=3

aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com

docker pull ${AWS_ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com/${NAME}:${TAG}
docker run -d \
  --log-driver=awslogs \
  --log-opt awslogs-region=us-east-1 \
  --log-opt awslogs-group=${LOG_GROUP} \
  --log-opt awslogs-stream=${NAME} \
  --name ${NAME} \
  --env-file secrets.env \
  --mount type=bind,source=$(pwd)/peewee.db,target=/usr/app/twtr2telega/peewee.db \
  ${AWS_ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com/${NAME}:${TAG}
