from argparse import ArgumentParser


def parse_arguments():
    argparser = ArgumentParser(description='Compares two configuration files and shows a difference.')  # noqa: E501
    argparser.add_argument('first_file', type=str)
    argparser.add_argument('second_file', type=str)
    argparser.add_argument('-f', '--format', default='stylish', choices=['stylish', 'plain', 'json'], help='set format of output (default: "stylish")', type=str)  # noqa: E501
    args = argparser.parse_args()
    return args