from pathlib import Path
import os
import configparser
from telbox.config.config_template import template as config_template


home = Path.home()
config_folder = home / ".telbox"
config_file = config_folder / "config.py"


def make_config_folder():
    if not config_folder.is_dir():
        config_folder.mkdir(parents=True)


def get_config():
    make_config_folder()
    if  not config_file.is_file():
        config_file.touch()
        with   open(config_file,'w') as f:
            f.writelines(config_template)

    config = configparser.ConfigParser()
    config.read(config_file)
    return config['DEFAULT']
    
