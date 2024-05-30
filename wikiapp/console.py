import textwrap

import click

from wikiapp import __version__
from wikiapp.wikipedia import random_page


@click.command()
@click.option(
    "--language",
    "-l",
    default="en",
    help="Gets random page from Wikipedia in given language",
    metavar="LANG",
    show_default=True,
)
@click.version_option(version=__version__)
def main(
    language:str #The language you want to use, as a two character string
         ) -> None: #This is a console function so returns nothing
    
    """
    This is the console interface to 'random_page' function in wikipedia.py.

    it comes with cool colors
    """
    page= random_page(language=language)
    title = page.title
    extract = page.extract
    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))


if __name__ == "__main__":
    main()
