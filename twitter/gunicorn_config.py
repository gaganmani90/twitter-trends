import multiprocessing

from gunicorn.http import Request
from gunicorn.http.wsgi import Response
from gunicorn.workers.base import Worker

bind = "127.0.0.1:8000"
backlog = 2048
# workers = multiprocessing.cpu_count() * 2+ 1
worker = 1
worker_connections = 1000
timeout = 30
keepalive = 2
threads = 2

#   daemon - Detach the main Gunicorn process from the controlling
#       terminal with a standard fork/fork sequence.
#
#       True or False
daemon = False

proc_name = 'twitter-trends-gunicorn'


def on_starting(server):
    # register some variables here
    server.log.info("Starting gunicorn app ...")


def on_exit(server):
    # perform some clean up tasks here using variables from the application
    server.log.info("Shutting down gunicorn app ...")


def post_fork(server, worker):
    server.log.info("Worker spawned (pid: %s)", worker.pid)


def pre_fork(server, worker):
    pass


def pre_exec(server):
    server.log.info("Forked child, re-executing.")


def when_ready(server):
    server.log.info("Server is ready. Spawning workers")


def worker_int(worker: Worker):
    worker.log.info("worker received INT or QUIT signal: {}, age: {}".format(worker.pid, worker.age))


def post_request(worker: Worker, req: Request, environ, resp: Response):
    worker.log.info(
        "request query: {}, resp length: {}, worker age: {}".format(req.query, resp.response_length, worker.age))


def worker_abort(worker):
    worker.log.info("worker received SIGABRT signal")
