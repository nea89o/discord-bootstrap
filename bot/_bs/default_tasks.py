import sys
from subprocess import call

from .load import load
from .systemd import install_systemd


def install_requirements():
    call([sys.executable, '-m', 'pip', '-r', 'requirements.txt'])


def run_bot():
    load('bot').main()


__all__ = ['run_bot', 'install_systemd', 'install_requirements']
