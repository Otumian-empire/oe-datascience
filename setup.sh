#!/usr/bash

# update system
sudo apt update

# enable environmental support for visualization
sudo apt install python3-pip python3-dev python3-tk

# create a virtual environment
python -m venv venv

# activate the virtual environment
source venv/bin/activate

# install packages from requirements.txt file
pip install -r requirements.txt

# the end, Bon!!
echo "Setup completed!!!"