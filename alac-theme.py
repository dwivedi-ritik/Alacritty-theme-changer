    #!/bin/python

    import argparse

    from alac import *

    parser = argparse.ArgumentParser(
        description="Simple Python Script for changing alacritty terminal emulator theme")
    parser.add_argument(
        "-l", "--list", help="Listing out all available themes", action="store_true")
    parser.add_argument("-t", "--theme", help="Set theme by passing theme name")
    parser.add_argument(
        "-c", "--curr", help="Shows current theme of alacritty", action="store_true")
    parser.add_argument("-d", "--default",
                        help="Write my alacritty config", action="store_true")
    parser.add_argument(
        "-do", "--disco", help="Change random in each half second", action="store_true")
    args = parser.parse_args()

    if args.list:
        list_themes()

    if args.curr:
        print(current_theme())

    if args.theme:
        changing_theme(args.theme)

    if args.default:
        writing_default_config()

    if args.disco:
        disco_term()
