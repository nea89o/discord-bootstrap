from ._bs.config import prompt_missing_configs
from ._bs.default_tasks import install_requirements, run_bot, install_systemd
from ._bs.load import load
from ._bs.tasks import task


@task('run')
def run():
    run_bot()


@task('install')
def install():
    install_requirements()
    prompt_missing_configs()
    install_systemd()


@task('configurate')
@task('config')
def config():
    load('config')
    prompt_missing_configs()
