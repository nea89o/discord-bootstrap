from functools import partial

tasks = {}


def task(name: str):
    return partial(tasks.__setitem__, name)


__all__ = ['task']
