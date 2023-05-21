#!/bin/bash

PORT=8080
CONTAINER="nickramsay-dev"
IMAGE="py-fastapi-docker-nickramsay-dev"

# get directory of script
DIR="$(cd "$(dirname "$0")" && pwd)"

DB="$DIR/db/posts.db"

docker run -d -p $PORT:80 --rm -v $DB:/posts.db --name $CONTAINER $IMAGE 
