#!/bin/bash

env_setup () {
    # install requirements
    if [ "$dev_env" == "windows" ]
    then
        pip install -r ../requirements.txt
    else
        pip3 install -r ../requirements.txt
    fi
}

config_secrets() {
    # executes python script to config GH secrets
    if [ "$dev_env" == "windows" ]
    then
        python config_setup.py
    else
        python3 config_setup.py
    fi
}

# Ask user for development environment
echo "Please follow the prompts for setting up the CICD pipeline"
echo "Enter which environment you're developing on (windows, mac, linux, unix): "
read dev_env
env_setup
config_secrets



