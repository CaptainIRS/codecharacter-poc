#!/bin/bash

docker build -f cc-compiler.dockerfile -t codecharacter-cc-compiler .
docker build -f cc-runner.dockerfile -t codecharacter-cc-runner .
docker build -f java-runner.dockerfile -t codecharacter-java-runner .
docker build -f python-runner.dockerfile -t codecharacter-python-runner .