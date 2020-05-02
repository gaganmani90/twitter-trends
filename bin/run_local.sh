#!/usr/bin/env bash
set -exu


export FLASK_APP=twitter/main
export PYTHONPATH=${PWD}/test:${PWD}/bin
flask run