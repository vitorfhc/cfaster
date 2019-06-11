import logging
from os import mkdir

logger = logging.getLogger(__name__)


def file_saver(inputs, outputs):
    in_folder = 'inputs/'
    out_folder = 'outputs/'
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
