import os

alacritty_config_path = "{}/.config/alacritty/alacritty.yml".format(
    os.path.expanduser("~")
)


def create_config_dir():
    usr_dir = os.path.expanduser("~")    
    if not os.path.exists(alacritty_config_path):
        os.mkdir(f"{usr_dir}/.config/alacritty")

    with open(f"{usr_dir}/.config/alacritty/alacritty.yml") as config_f:

