# -*- coding: utf-8 -*-

import sys
import json
from pprint import pprint
import argparse


def open_psort_json(custom_json):
    with open(custom_json) as f:
        pfile = json.load(f)
        return pfile


def main():
    pfile_name = sys.argv[1]
    pfile = open_psort_json(pfile_name)
    pprint(pfile)
