import sys

from .load import base_path, load

# language=ini
TEMPLATE = """
[Unit]
Description = {description}

[Service]
Type=simple
ExecStart={python_executable} -m bot run
WorkingDirectory={working_directory}
Restart=always

[Install]
WantedBy=multi-user.target
"""


def generate_template():
    bot = load('bot')
    return TEMPLATE.format(
        python_executable=sys.executable,
        working_directory=str(base_path),
        description=bot.description,
    )


def install_systemd():
    bot = load('bot')
    with open(f'/etc/systemd/system/{bot.name}.service', 'w') as fp:
        fp.write(generate_template())
    print(f"Service created. Use systemd enable/start {bot.name} to start/enable the bot")
