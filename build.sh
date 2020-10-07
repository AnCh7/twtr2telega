#!/usr/bin/env bash

AWS_ACCOUNT_ID=xxxxxxxxxx
NAME=twtr2telega
TAG=latest

OUTPUT="$(aws ecr get-login --no-include-email --region us-east-1)"
${OUTPUT}

docker build -t ${NAME}:${TAG} -f "Dockerfile" "."
docker tag ${NAME}:${TAG} ${AWS_ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com/${NAME}:${TAG}
docker push ${AWS_ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com/${NAME}:${TAG}
docker rmi ${AWS_ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com/${NAME}:${TAG}
