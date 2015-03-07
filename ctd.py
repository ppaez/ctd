import argparse


def process_command_line_arguments():
    parser = argparse.ArgumentParser(description='Connect the dots')

    help='Path to top-level input folder'
    parser.add_argument('input_path', help=help)

    parser.add_argument('outputfile', help='Output file name')

    args=parser.parse_args()
    return args

args = process_command_line_arguments()
