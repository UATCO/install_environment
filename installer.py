import argparse
import logging
import os
import platform
import sys

handler = logging.StreamHandler(sys.stdout)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)

path_conf = os.path.join(os.getcwd(), "config.ini")
encoding = 'UTF-8'
section = 'general'
folder = 'Scripts' if platform.system() == 'Windows' else 'bin'
python = 'python' if platform.system() == 'Windows' else 'python3'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Clone/update/checkout repositories')
    parser.add_argument('-clone', action='store_true', help='Clone repositories')
    parser.add_argument('-create_venv', action='store_true', help='Create venv')
    parser.add_argument('-reqs', action='store_true', help='Install requirements')
    parser.add_argument('-checkout', type=str, help='Checkout branches')
    parser.add_argument('-pull', action='store_true', help='Pull branches')
    args = parser.parse_args()
    # if args.clone:
    #     clone()
    # if args.create_venv:
    #     create_venv()
    # if args.reqs:
    #     install_requirements()
    # if args.checkout:
    #     checkout(args.checkout)
    # if args.pull:
    #     pull()