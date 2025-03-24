#!/usr/bin/env python3
from download import *
from convertion import *
import argparse
import subprocess, sys


def get_exe_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["download", "convert", "open"])
    parser.add_argument('param', nargs="*")

    args = parser.parse_args()

    try:
        if args.command == "download":
            download(args.param[0])
        elif args.command == "convert":
            convert(args.param[0], args.param[1], args.param[2])
        elif args.command == "open":
            current_dir = get_exe_dir()
            folder_path = os.path.join(current_dir, 'downloads')
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            subprocess.Popen(['explorer', folder_path])
    except IndexError:
        print('Fail to execute: Missing parameters')


if __name__ == "__main__":
    main()
