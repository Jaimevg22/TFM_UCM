import os

def get_workdir():
    WORK_DIR = os.path.dirname(os.path.abspath(__file__))
    print(WORK_DIR)
    return WORK_DIR

if __name__ == '__main__':
    get_workdir()