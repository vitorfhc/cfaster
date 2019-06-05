#!/bin/bash

# Start container and exec
sudo docker-compose up -d && \
sudo docker-compose exec cfaster bash
