import logging
from os import mkdir

logger = logging.getLogger(__name__)


def file_saver(inputs, outputs):
    in_folder = 'inputs/'
    out_folder = 'outputs/'
    mkdir(in_folder)
    mkdir(out_folder)

    for ind, inp in enumerate(inputs):
        filename = f'{in_folder}input_{ind+1}.txt'
        logger.debug('Writing to ' + filename)
        with open(filename, 'w') as f:
            f.write(inp)

    for ind, out in enumerate(outputs):
        filename = f'{out_folder}output_{ind+1}.txt'
        logger.debug('Writing to ' + filename)
        with open(filename, 'w') as f:
            f.write(out)
