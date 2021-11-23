import argparse


arg_parser = argparse.ArgumentParser(description="This is argument parser")

#----------optional arguments----------#
arg_parser.add_argument("--port",help="For specifying port number",type=int)
arg_parser.add_argument("--proxy",help="For specifying proxy url",type=str)

#----------positional arguments----------#
arg_parser.add_argument("hostname",help="For specifying Hostname ")
arg_parser.add_argument("website_url",help="Website to visit",choices=["google.com","yahoo.com"])


args = arg_parser.parse_args()


if args.port:
    print(f"Entered PORT IS: {args.port}")
if args.proxy:
    print(f"Entered PROXY IS: {args.proxy}")
if args.hostname:
    print(f"Entered HOSTNAME IS: {args.hostname}")
if args.website_url:
    print(f"Entered WEBSITE_URL IS: {args.website_url}")

