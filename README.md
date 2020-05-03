# Twitter Trends

## How to use this package
#### 1. Fork the repository 
#### 2. Create virtual env
```shell script
    virtualenv venv
    cd venv
    source bin/activate
```
#### 3. Install dependencies
From root: 
```.shell script
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
    .bin/run_local.sh
    ```
* `gunicorn -b :8080 twitter.main:app`: This command will run server with gunicorn. You do not have to use it unless
you want to deploy it on gcloud.
--- 
## TODO
* Integrate with Google Firebase 
* Interpret twitter hashtags
* Interpret common trends across countries
* UI improvements

