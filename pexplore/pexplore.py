# -*- coding: utf-8 -*-
import click
import json


@click.command()
@click.argument("input", type=click.File("rb"))
def cli(input):
    pfile = json.load(input)
    for session in pfile:
        if pfile[session]["analysis_reports_counter"].get("tagging"):
            tags = pfile[session]["event_labels_counter"]
            ptags = json.dumps(tags)
    click.echo(ptags)


if __name__ == "__main__":
    cli()
