# Trends

## How to use this package
#### 1. Fork the repository 
#### 2. (optional) Create virtual env
```shell script
    virtualenv venv
    cd venv
    source bin/activate
```
#### 3. Install dependencies
Tip: Use `pyenv` to maintain python versions locally.

From root: 
```shell script
pip install . # verify python version requirement
pip freeze -r requirements.txt 
pip install -r requirements.txt
pip list #verify package list
python --version #verify python version
```

#### 4. Run
Go to root directory
* Unit tests run: `pytest`. These runs make twitter api call so be cautious and do not 
make too many calls.
* App run
    ```shell script
    python setup.py build
    ./bin/run_local.sh
    ```
* `gunicorn -b :8080 twitter.main:app`: This command will run server with gunicorn. You do not have to use it unless
you want to deploy it on gcloud.

## With Docker 
This is docker compatible application that you can run with docker image as well. 
* Install docker from [here](https://docs.docker.com/get-docker/) 
```shell script
docker build .
docker images # get image id 
docker run -p 5001:5001 <image id>
```

* If you are too lazy to checkout code, you can direclty download docker image from [dockerhub](https://hub.docker.com/repository/docker/gaganmani90/trends/tags)


