# -*- coding: utf-8 -*-
import click
import json


@click.command()
@click.argument("input", type=click.File("rb"))
def cli(input):
    """Pexplore works with json files created by pinfo. To create a 
       file to use with pexplore run:

       pinfo.py -v --output_format json -w pinfo.json myfile.plaso

       By default pexplore will printout the section of the pinfo.json file
       that has the tag counts. To run it type:

       pexplore.py pinfo.json
       """
       
    pfile = json.load(input)
    for session in pfile:
        if pfile[session]["analysis_reports_counter"].get("tagging"):
            tags = pfile[session]["event_labels_counter"]
            ptags = json.dumps(tags)
    click.echo(ptags, nl=False)


if __name__ == "__main__":
    cli()
