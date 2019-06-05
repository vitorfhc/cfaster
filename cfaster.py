import logging
from click import Choice, group, command, option, argument

logger = logging.getLogger(__name__)

target_scraper = {
    'cf': None,
    'uva': None,
}

targets = [key for key in target_scraper.keys()]


@group()
@option('-v', '--verbose', is_flag=True, help='Output INFO level logs.')
@option('-d', '--debug', is_flag=True, help='Output DEBUG level logs.')
def main_cmd(verbose, debug):
    # this is not working, go figure
    if verbose:
        logger.setLevel(logging.INFO)
        logger.info('Logs level set to INFO')
    if debug:
        logger.setLevel(logging.DEBUG)
        logger.info('Logs level set to DEBUG')


@main_cmd.command(short_help='Scraps the problem and saves inputs and outputs.')
@argument('url')
@option('-t', '--target', default=targets[0],
        show_default=True, type=Choice(targets),
        help='Website you are targeting to scrap.')
def scrap(url, target):
    pass


if __name__ == '__main__':
    main_cmd()
