"""Console script for testservier."""

import click

from src.testservier import run, get_top


@click.group()
def cli():
    pass


@click.command()
def run_pipeline():
    run()


@click.command()
@click.option("--top", default=1, help="Get top N jounals.")
def top_journals(top):
    print(get_top(top))


cli.add_command(run_pipeline)
cli.add_command(top_journals)
