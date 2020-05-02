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
```.shell script
pip freeze -r ../twitter/requirements.txt 
pip install -r ../twitter/requirements.txt
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



