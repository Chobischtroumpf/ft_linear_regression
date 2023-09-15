#!/bin/bash

echo "setting up virtual environment :"

python3 -m venv ./linear_regression_env;
source ./linear_regression_env/bin/activate
pip install -r ./requirements.txt

echo "Virtual environment has been set, type 'source ./linear_regression_env/bin/activate' to enter it!"