def file_saver(inputs, outputs):
    # TODO: logging
    for ind, inp in enumerate(inputs):
        with open(f'input_{ind+1}.txt', 'w') as f:
            f.write(inp)
    for ind, out in enumerate(outputs):
        with open(f'output_{ind+1}.txt', 'w') as f:
            f.write(out)
