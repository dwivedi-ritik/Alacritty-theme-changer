#!/bin/python
import argparse
from alac import *

parser = argparse.ArgumentParser(description="Simple Python Script for changing alacritty terminal emulator theme")
parser.add_argument("-l", "--list", help="Listing out all available themes", action="store_true")
parser.add_argument("-t", "--theme", help="Set theme by passing theme name" , metavar='')
parser.add_argument("-c", "--curr", help="Shows current theme of alacritty", action="store_true")
parser.add_argument("-d", "--default",help="Write my alacritty config", action="store_true")

#Argument for parsing disco sub parser
disco_info = '''
    A tool for making color change in alacritty. Try `python alac-theme.py disco`  Press ctrl+ c for closing the party'''

#parsing a subparser with their arguments
disco_parser = parser.add_subparsers(description=disco_info, dest="child_parser")

child_disco_parser = disco_parser.add_parser('disco')

child_disco_parser.add_argument("--count",type=int,help="How many time do you want to happen disco",default=30 , metavar='')
child_disco_parser.add_argument("--gap",type=float, help="Time in which you want to make transition" , default=0.5 , metavar='')

args = parser.parse_args()

if args.list:
    list_themes()

if args.curr:
    print(current_theme())

if args.theme:
    changing_theme(args.theme)

if args.default:
    writing_default_config()

if args.child_parser:
    disco_term(num_of_times=args.count , gap_time=args.gap)
