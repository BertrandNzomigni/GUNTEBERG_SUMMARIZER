#!/bin/bash
clear
sudo docker image build -t home:GUNTEBERG .
sudo docker run --name GUNTEBERG --volume ./model:/code/model home:GUNTEBERG