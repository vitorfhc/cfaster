import logging
from click import Choice, group, command, option, argument

from .scrapers.codeforces import codeforces_scraper as cf_scraper

logger = logging.getLogger(__name__)

target_scraper = {
    'cf': cf_scraper,
}

targets = [key for key in target_scraper.keys()]


@group()
@option('-v', '--verbose', is_flag=True, help='Output INFO level logs.')
@option('-d', '--debug', is_flag=True, help='Output DEBUG level logs.')
def main_cmd(verbose, debug):
    level = logging.WARNING
    format_ = '[%(levelname)s]: %(message)s'
    if verbose:
        level = logging.INFO
    if debug:
        level = logging.DEBUG
    logging.basicConfig(level=level, format=format_)
    logger.info('Level of logs set to ' +
                logging.getLevelName(logger.getEffectiveLevel()))


@main_cmd.command(
    short_help='Scraps the problem and saves inputs and outputs.'
)
@argument('url')
@option('-t', '--target', default=targets[0],
        show_default=True, type=Choice(targets),
        help='Website you are targeting to scrap.')
def scrap(url, target):
    logger.info('Running scrap command')
    target_scraper[target](url)


if __name__ == '__main__':
    main_cmd()
