import argparse

arg_parser = argparse.ArgumentParser(description=":ARGUMENT PARSER MENU:")

#----------optional arguments----------#
arg_parser.add_argument("--hostname",help="SPECIFY HOSTNAME")
arg_parser.add_argument("--port",help="SPECIFY PORT")

args = arg_parser.parse_args()

if args.hostname:
    print(f"ENTERED HOSTNAME IS:{args.hostname}")
elif args.port:
    print(f"ENTERED PORT IS:{args.port}")
