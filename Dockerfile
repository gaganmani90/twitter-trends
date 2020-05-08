FROM python:3

# add code
ADD . /usr/src/app

# set working directory
WORKDIR /usr/src/app

## install dependencies
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install Flask
RUN pip install -r /var/www/requirements.txt


# Set environment variables
ENV FLASK_APP=twitter/main.py
ENV PYTHONPATH=${PWD}/test:${PWD}/bin

EXPOSE 5001
#ENTRYPOINT ['/usr/src/app/bin/run_local.sh']
#CMD ["flask","run","--host=0.0.0.0"]
CMD ["flask","run"]
