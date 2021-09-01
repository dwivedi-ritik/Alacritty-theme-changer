#!/bin/python
import yaml
import os
import re
import random
import time

alacritty_config_path = "{}/.config/alacritty/alacritty.yml".format(
    os.path.expanduser("~")
)

def reading_theme(config_path):
    try:
        with open(config_path, "r") as f:
            resp = yaml.safe_load(f.read())
            return resp
    except Exception:
        raise Exception("PROVIDE VALID PATH")


def validate_theme(usr_theme):
    for theme in os.listdir("themes"):
        match = re.search(r"(.+).y", theme)
        if match and match.group(1).lower() == usr_theme.lower():
            return "themes/" + theme
    return None


def list_themes():
    theme_list = [theme for theme in os.listdir("themes")]
    for i in range(0, len(theme_list), 3):
        for j in range(i, i + 3):
            theme = re.search(r"(.+).y", theme_list[j]).group(1)
            print("{}{}".format(theme, " " * 20)[:20], end=" " * 5)
        print()
    return


def current_theme():
    curr = reading_theme(alacritty_config_path)
    for theme_f in os.listdir("themes"):
        curr_f = reading_theme("themes/" + theme_f)
        if curr["colors"]["primary"] == curr_f["colors"]["primary"]:
            matched_theme = re.search(r"(.+).y", theme_f)
            return matched_theme.group(1)
    return None


def changing_theme(usr_theme, f_theme=None):
    if not f_theme:
        validate = validate_theme(usr_theme)
    else:
        validate = "themes/" + f_theme
    if validate:
        try:
            with open(alacritty_config_path, "r") as f:
                alacritty_theme = yaml.safe_load(f.read())
        except FileNotFoundError:
            print("You have not configured alacritty yet!!")
            usr_f_resp = input("Do you want to use my config?(y/n) ")
            if usr_f_resp.lower() in ["y", "yes"]:
                writing_default_config()
            return

        selected_theme = reading_theme(validate)
        alacritty_theme["colors"] = selected_theme["colors"]

        with open(alacritty_config_path, "w") as f:
            f.write(yaml.dump(alacritty_theme))
    else:
        raise Exception("Invalid theme choice")


def writing_default_config():
    usr_dir = os.path.expanduser("~")    
    if not os.path.exists(alacritty_config_path):
        os.mkdir(f"{usr_dir}/.config/alacritty")

    with open("alacritty_config.yml", "r") as rf:
        default_confg = yaml.safe_load(rf.read())
        with open(f"{usr_dir}/.config/alacritty/alacritty.yml", "w") as f:
            f.write(yaml.dump(default_confg))


def disco_term(num_of_times , gap_time):
    theme_list = [theme for theme in os.listdir("themes")]
    last_theme = current_theme()
    try:
        for _ in range(num_of_times):
            random_theme = random.choice(theme_list)    
            time.sleep(gap_time)
            changing_theme(usr_theme=None, f_theme=random_theme)
    except KeyboardInterrupt:
        print("\nRIP DISCO")
        pass
    changing_theme(last_theme)