#!/bin/bash

# changing to api directory
cd ./api

# remove the old image
docker image rm api-odd

# build the docker image
docker build -t api-odd:latest .

# run the container in the background
docker run -p 5000:5000 -d api-odd:latest


