# cli-args

Do you belong to those who have to look up the calls you have to make to
[argparse](https://github.com/ThomasWaldmann/argparse)? And are you longing for
a way to just import the parsed arguments as you would import `sys.argv`? Then
`cli-args` is the way to go!

`cli-args` is a Python library for an easier parsing of command line arguments.
It wraps the popular [argparse](https://github.com/ThomasWaldmann/argparse) to
allow importing parsed arguments from anywhere in the code. One of the key
features is the way you define what arguments you accept. By providing a
dictionary - that also can be read from a JSON file! - you can easily set all
available command line arguments at one specific, easy-to-find place.

## Get it!

```shell
pip install cli-args
```

## Use it!

**`demo.py`**

```python
import cli_args


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


print(cli_args.argv['integer_a']) # 3
print(cli_args.argv['integer_b']) # 5
```

`python demo.py --integer_a=3 --integer_b=5`

## License

Licensed under the [MIT](https://github.com/yannickkirschen/cli-args/blob/master/LICENSE) License. Happy forking :)
