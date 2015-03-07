import argparse
import os


def process_command_line_arguments():
    parser = argparse.ArgumentParser(description='Connect the dots')

    help='Path to top-level input folder'
    parser.add_argument('input_path', help=help)

    parser.add_argument('outputfile', help='Output file name')

    help = 'Path to exclude file. ' \
           'Paths included there will be listed ' \
           'but not traversed'
    parser.add_argument('--exclude-file',
        help=help, default='')

    args=parser.parse_args()
    return args

def isexcluded(path, excludes):
    for exclude in excludes:
        if path.startswith(exclude):
            return True
    return False

args = process_command_line_arguments()

excludes = []
if args.exclude_file and os.path.exists(args.exclude_file):
    f = open(args.exclude_file)
    for line in f:
        excludes.append(line.strip())

for dirpath, dirnames, filenames in os.walk(args.input_path):
    print(dirpath)
    if not isexcluded(dirpath, excludes):
        for dirname in dirnames:
            print('  {}/'.format(dirname))
        for filename in filenames:
            print('  {}'.format(filename))
    print()
