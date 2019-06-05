import click
from scraper import Scraper, CFScraper, UvaScraper

@click.group()
def main_cmd():
    pass

@main_cmd.command()
@click.argument('url')
@click.option('-t', '--target', default='cf', show_default=True, type=click.Choice(['cf', 'uva']))
def scrap(url, target):
    scraper = object()
    if target == 'cf':
        scraper = CFScraper(url)
    elif target == 'uva':
        scraper = UvaScraper(url)

    scraper.scrap()
    #scraper.save()

if __name__ == '__main__':
    main_cmd()
