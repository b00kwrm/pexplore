# -*- coding: utf-8 -*-

import sys
import json
from pprint import pprint

def open_psort_json(custom_json):
    with open(custom_json) as f:
        pfile = json.load(f)
        return pfile


def main():
    _file_name = sys.argv[1]
    pfile = open_psort_json(_file_name)
    pprint(pfile)

