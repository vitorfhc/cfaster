#!/bin/bash

# Start container and exec
sudo docker-compose up -d --build && \
sudo docker-compose exec cfaster bash
