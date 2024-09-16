import os

def get_workdir():

    WORK_DIR = os.path.dirname(os.path.abspath(__file__))
    
    return WORK_DIR