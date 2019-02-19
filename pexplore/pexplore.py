# -*- coding: utf-8 -*-
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter04/dns_basic.py

import sys
import json
from pprint import pprint
import argparse


def open_psort_json(custom_json):
    with open(custom_json) as f:
        pfile = json.load(f)
        return pfile


def parse_args(custom_json):
    parser = argparse.ArgumentParser(description="Get tags from plaso json files")
    parser.add_argument("file_name", help="name of the plaso file you want to process.")
    args = parser.parse_args().name
    return args


def main():
    _file_name = sys.argv[1]
    pfile_name = parse_args(_file_name)
    pfile = open_psort_json(pfile_name)
    pprint(pfile)
