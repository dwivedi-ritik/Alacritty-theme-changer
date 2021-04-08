import yaml
import os
import re

alacritty_config_path = "{}/.config/alacritty/alacritty.yml".format(os.path.expanduser("~"))

#Reading Alacritty Config File from path
def reading_theme(config_path):
    try:
        with open(config_path , "r") as f:
            resp = yaml.safe_load(f.read())
            return resp
    except Exception:
        raise Exception("PROVIDE VALID PATH")

#Validating theme
def validate_theme(usr_theme):
    for theme in os.listdir("themes"):
        match = re.search(r"(.+).y" , theme)
        if match and match.group(1).lower() == usr_theme.lower():
            return "themes/"+theme
    return None

#Lisiting Out Available Themes
def list_themes():
    themes = os.listdir("themes")
    for theme in themes:
        theme = re.search(r"(.+).y" , theme)
        print(theme.group(1)) 

#Shows current theme
def current_theme():
    curr = reading_theme(alacritty_config_path)
    for theme_f in os.listdir("themes"):
        curr_f = reading_theme("themes/"+theme_f)
        if curr["colors"]["primary"] == curr_f["colors"]["primary"]:
            matched_theme = re.search(r"(.+).y" , theme_f)
            return matched_theme.group(1)
    return None

#Changing theme
def changing_theme(usr_theme):
    validate = validate_theme(usr_theme)
    if validate:
        #Reading theme file
        try:
            with open(alacritty_config_path , "r") as f:
                alacritty_theme = yaml.safe_load(f.read())
        except FileNotFoundError:
            print("You have not configured alacritty yet!!")
            usr_f_resp = input("Do you want to use my config?(y/n) ")
            if usr_f_resp.lower() in ["y" , "yes"]:
                writing_default_config()
            return
        #Reading colors of user selected theme
        selected_theme  = reading_theme(validate)
        alacritty_theme["colors"] = selected_theme["colors"]
        #Writng changed path to alacritty config
        with open(alacritty_config_path, "w") as f:
            f.write(yaml.dump(alacritty_theme))
    else:
        raise Exception("Invalid theme choice")

def writing_default_config():
    with open("alacritty_config.yml" , "r") as rf:
        default_confg = yaml.safe_load(rf.read())
    with open(alacritty_config_path , "w") as f:
        f.write(yaml.dump(default_confg))
