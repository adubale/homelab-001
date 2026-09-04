#!/bin/bash

docker build -t dashboard .
docker run -d --name dashboard -p 5000:5000 -v /var/run/docker.sock:/var/run/docker.sock dashboard
