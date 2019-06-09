from click.testing import CliRunner
from cfaster.__main__ import scrape

runner = CliRunner()

invalid_urls = [
        'http://domain.com/problem',
        'https://domain.com/problem',
        'domain.com',
        'https://codeforces.com',
        'https://codeforces.com/contests',
        'sadaddsg.sda..sad',
        'www.codeforces.com/sad/dasdas/problem/A',
        'www.codeforces.com',
]

valid_urls = [
    'https://codeforces.com/contest/1172/problem/A',
    'https://codeforces.com/contest/1172/problem/C1',
    'https://codeforces.com/contest/1172/problem/E',
    'https://codeforces.com/contest/1174/problem/B',
    'https://codeforces.com/contest/1174/problem/D',
]

def test_no_url():
    result = runner.invoke(scrape)
    assert result.exit_code == 2

def test_invalid_urls():
    for invalid_url in invalid_urls:
        result = runner.invoke(scrape, invalid_url)
        assert result.exit_code != 0

def test_verbose_scrape():
    pass

def test_valid_url():
    pass

def test_count_inputs():
    pass

def test_count_outputs():
    pass

def test_inputs():
    pass

def test_outputs():
    pass
