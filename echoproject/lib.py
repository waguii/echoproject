import argparse
from art import *

def try_me(message):
    Art=text2art(str(message))
    print(Art)


if __name__ == '__main__':
    description = 'stkrgcp_description'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--message',
                        nargs='+',
                        help='Message to echo',
                        required=True)
    args = parser.parse_args()
    message = args.message
    try_me(message)
