"""Convert text files with '<number> CR' and '<number> DB' to signed numbers.

This is useful for converting Think-or-Swim FOREX account reports into something that can actually be imported in a spreadsheet.
"""
import sys, re

def main():
    import argparse, logging
    logging.basicConfig(level=logging.INFO, format='%(levelname)-8s: %(message)s')
    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument('filenames', nargs='+', help='Filenames')
    opts = parser.parse_args()

    for fn in opts.filenames:
        for line in open(fn):
            if ',' not in line:
                continue
            line = re.sub(r'\xc2\xa0', r' ', line)
            line = re.sub(r'([-+]?[0-9][0-9.,]+) CR', r'\1', line)
            line = re.sub(r'([-+]?[0-9][0-9.,]+) DB', r'-\1', line)
            sys.stdout.write(line)


if __name__ == '__main__':
    main()