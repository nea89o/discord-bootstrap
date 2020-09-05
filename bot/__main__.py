from sys import argv

from ._bs.load import load
from ._bs.tasks import tasks


def main():
    load('tasks')
    if len(argv) <= 1:
        print(f"Please provide a task to run: {' '.join(tasks.keys())}")
        return 1
    to_run = tasks.get(argv[1])
    if not to_run:
        print(f"Unknown task: {argv[1]}")
    to_run()


if __name__ == '__main__':
    exit(main())
