import sys
import json
from pprint import pprint

def open_psort_json(custom_json):
    with open(custom_json) as f:
        pfile = json.load(f)
        return pfile

if __name__ == "__main__":
    pfile = open_psort_json(sys.argv[1])
    pprint(pfile)
