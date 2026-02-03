from argparse import ArgumentParser


def parse_args():
    argparser = ArgumentParser(description='Compares two configuration files and shows a difference.') # noqa: E501
    argparser.add_argument('first_file', type=str)
    argparser.add_argument('second_file', type=str)
    argparser.add_argument('-f', '--format', type=str)
    args = argparser.parse_args()
    print(f'{args.first_file} {args.second_file}')
    return args.first_file, args.second_file
