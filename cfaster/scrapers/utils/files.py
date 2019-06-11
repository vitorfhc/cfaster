import logging
from os import mkdir
from os.path import exists
from shutil import rmtree

logger = logging.getLogger(__name__)


def file_saver(inputs, outputs):
    in_folder = 'inputs/'
    out_folder = 'outputs/'

    in_exists = exists(in_folder)
    out_exists = exists(out_folder)

    if in_exists or out_exists:
        logger.warning('Input and/or output directories already exists')
        choice = input('Overwrite existing input/output folders? [yN] ')
        if choice.lower() == 'y':
            rmtree(in_folder)
            rmtree(out_folder)
        else:
            logger.error('Can\'t overwrite inputs/outputs directories')
            exit(1)

    mkdir(in_folder)
    mkdir(out_folder)

    for ind, inp in enumerate(inputs):
        filename = '{}input_{}.txt'.format(in_folder, ind+1)
        logger.debug('Writing to ' + filename)
        with open(filename, 'w') as f:
            f.write(inp)

    for ind, out in enumerate(outputs):
        filename = '{}output_{}.txt'.format(out_folder, ind+1)
        logger.debug('Writing to ' + filename)
        with open(filename, 'w') as f:
            f.write(out)
