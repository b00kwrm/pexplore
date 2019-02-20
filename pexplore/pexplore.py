# -*- coding: utf-8 -*-
import click
import json
from pprint import pprint

@click.command()
@click.argument('input', type=click.File('rb'))
def cli(input):
    pfile = json.load(input)
    for session in pfile:
        if pfile[session]["analysis_reports_counter"].get("tagging"):
            tags = pfile[session]["event_labels_counter"]
    pprint(tags)

if __name__ == "__main__":
    cli()


