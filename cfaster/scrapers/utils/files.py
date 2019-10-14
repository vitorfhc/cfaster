import logging
from os import mkdir
from os.path import exists
from shutil import rmtree

logger = logging.getLogger(__name__)


def create_dirs(in_folder, out_folder):
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


def file_saver(inputs, outputs):
    in_folder = 'inputs/'
    out_folder = 'outputs/'

    create_dirs(in_folder, out_folder)

    for filename_base, files in {'input': inputs, 'output': outputs}.items():
        for ind, dat in enumerate(files, start=1):
            filename = '{fnb}s/{fnb}_{ind}.txt'.format(
                fnb=filename_base, ind=ind)

            logger.debug('Writing to ' + filename)
            with open(filename, 'w') as f:
                f.write(dat)
