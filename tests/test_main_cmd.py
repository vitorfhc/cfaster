import re
from click.testing import CliRunner
from cfaster.__main__ import main_cmd

runner = CliRunner()

def test_version():
    result = runner.invoke(main_cmd, ['--version'])
    reg = r'\d+\.\d+\.\d+'
    match = re.match(reg, result.output)
    assert result.exit_code == 0
    assert match is not None
