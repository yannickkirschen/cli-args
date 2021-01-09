import sys

import cli_args

sys.argv.append('--integer_a=3')
sys.argv.append('--integer_b=5')

cli_args.from_file('demo/schema.json')


def test_cli():
    assert cli_args.argv['integer_a'] == 3
    assert cli_args.argv['integer_b'] == 5
