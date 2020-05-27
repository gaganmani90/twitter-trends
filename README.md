1. [ Description. ](#trends)
2. [ Usage tips. ](#how-to-use-this-package)
3. [ Docker ](#with-docker)

<a name="trends"></a>
# Trends

<a name="how-to-use-this-package"></a>
## How to use this package
#### 1. Fork the repository 
Assuming that you have forked and cloned this repository on your machine.

```shell script
git remote -v # check if you have setup my branch as upstream
git remote add upstream https://github.com/gaganmani90/python-programming.git # if not, add
git fetch upstream 
git merge upstream/master # merge changes from upstream
git push origin master # sync your master branch with upstream
```
#### 2. (optional) Create virtual env
```shell script
    virtualenv venv
    cd venv
    source bin/activate
```
#### 3. Install dependencies
Tip: Use `pyenv` to maintain python versions locally.

* Check running python version by using command `python -V`
* Install python 3.8.0 with pyenv
```shell script
pyenv install 3.8.0
eval "$(pyenv init -)"
python -V # it should result in 3.8.0
```

Install pip dependencies: 
```shell script
pip install . # verify python version requirement
pip freeze -r requirements.txt 
pip install -r requirements.txt
pip list #verify package list
```

#### 4. Run (with flask)
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

#### 5. Run (with gunicorn)
`gunicorn -c twitter/gunicorn_config.py twitter.main:app`

<a name="with-docker"></a>
## With Docker (not recommended)
This is docker compatible application that you can run with docker image as well. 
* Install docker from [here](https://docs.docker.com/get-docker/) 
```shell script
docker build .
docker images # get image id 
docker run -p 5001:5001 <image id>
```

* If you are too lazy to checkout code, you can direclty download docker image from [dockerhub](https://hub.docker.com/repository/docker/gaganmani90/trends/tags)

## Heroku Deployment 
`git push` will automatically deploy to Heroku. 

```shell script
heroku logs --tail -a trending-topic-demo # monitor logs
heroku local # test heroku locally before delpoyment
heroku local web # test
heroku config:get JAWSDB_MARIA_URL -a trending-topic-demo  # get database url
heroku addons:open jawsdb-maria  # open database page 
```

## Database credentials
* Create `twitter/password.ini` in the following format with db credentials:
```
[database]
Host=
Username=
Password=
Port=3306
Database=
```
