#!/bin/bash
clear
sudo docker image build -t home:GUNTEBERG .
sudo docker run --name GUNTEBERG home:GUNTEBERG