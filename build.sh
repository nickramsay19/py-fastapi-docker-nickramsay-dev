#!/bin/bash

# get directory of script
DIR="$(cd "$(dirname "$0")" && pwd)"

CONTAINER="nickramsay-dev"
IMAGE="py-fastapi-docker-nickramsay-dev"

# stop the container if it is already running
docker container stop nickramsay-dev > /dev/null 2>&1 && docker container rm nickramsay-dev > /dev/null

docker build -t $IMAGE $DIR
