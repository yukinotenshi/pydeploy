import sys
sys.path.append('./')

import click
from pydeploy.command_chain import CommandChain
import pydeploy.config as config


@click.command()
@click.argument("config_file")
@click.option("--endpoint", default="", help="A unique endpoint name for the github webhook")
def load_config(config_file, endpoint):
    CommandChain.load_from_config(config_file)
    if endpoint != "":
        config.route = endpoint


if __name__ == "__main__":
    load_config()
    from pydeploy.webhook import app
    app.run(host="0.0.0.0", port=9999)
