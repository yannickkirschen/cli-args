import cli_args


cli_args.from_file('demo/schema.json')

print(cli_args.argv['integer_a'])
print(cli_args.argv['integer_b'])
