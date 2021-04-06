import argparse

from alac import list_themes , current_theme , changing_theme

parser = argparse.ArgumentParser(description="Simple Python Script for changing alacritty terminal emulator theme")
parser.add_argument("-l" , "--list" , help="Listing out all available themes" , action="store_true")
parser.add_argument("-t" , "--theme" , help="Set theme by passing theme name")
parser.add_argument("-c" , "--curr" , help="Shows current theme of alacritty" , action="store_true")

args = parser.parse_args()

if args.list:
    list_themes()

if args.curr:
    print(current_theme())

if args.theme:
    print(args.theme)

if args.theme:
    changing_theme(args.theme)