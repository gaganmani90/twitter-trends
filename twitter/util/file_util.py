import os

def create_if_not_available(path):
    if not os.path.exists(path):
        open(path, 'w+')