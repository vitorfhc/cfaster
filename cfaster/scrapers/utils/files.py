import logging

logger = logging.getLogger(__name__)


def file_saver(inputs, outputs):
    for ind, inp in enumerate(inputs):
        filename = f'input_{ind+1}.txt'
        logger.info('Writing to ' + filename)
        with open(filename, 'w') as f:
            f.write(inp)
    for ind, out in enumerate(outputs):
        filename = f'output_{ind+1}.txt'
        logger.info('Writing to ' + filename)
        with open(filename, 'w') as f:
            f.write(out)
