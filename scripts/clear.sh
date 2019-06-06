#!/bin/bash

find . -name __pycache__ -type d | xargs rm -rf
rm -rf dist build *.egg-info
