import importlib
import pathlib


def load(what: str):
    return importlib.import_module('bot.' + what)


base_path = pathlib.Path(__file__).parent.parent.absolute()
