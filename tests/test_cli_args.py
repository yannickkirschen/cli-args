import sys

import cli_args


sys.argv.append('--integer_a=3')
sys.argv.append('--integer_b=5')


# or: cli_args.from_file('path/to/schema.json')
cli_args.from_schema({
    "description": "Process some integers.",
    "arguments": [
        {
            "short": "a",
            "long": "integer_a",
            "var": "NUMBER",
            "help": "The first integer",
            "default": 0,
            "type": "int"
        },
        {
            "short": "b",
            "long": "integer_b",
            "var": "NUMBER",
            "help": "The second integer",
            "default": "0",
            "type": "int"
        }
    ]
})


def test_cli():
    assert cli_args.argv['integer_a'] == 3
    assert cli_args.argv['integer_b'] == 5
