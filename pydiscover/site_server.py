from pydiscover import server
import argparse

"""
IN pydiscover 
Server sends data
Client recieve data
"""

# server will send required details to cabinet cclient
# will recieve ip address so has to also act as an client
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='PyDiscover Server',
                                     formatter_class=argparse.RawTextHelpFormatter, epilog='')
    parser.add_argument("-v", "--verbosity", dest="VERBOSE", action="count", help="verbosity level: -v, -vv, -vvv.",
                        default=3)

    parsed_args = parser.parse_args()

    # Setting
    server.log.setLevel(abs(50 - (parsed_args.VERBOSE * 10)))

    server.server_discover(answer='example.cfg',
                           magic='magic_word',
                           listen_ip='0.0.0.0',
                           port=40000,
                           password='password',
                           disable_hidden=True)


