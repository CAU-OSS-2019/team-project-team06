#!/usr/bin/env python

import argparse
import re

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    detect_path_parser=parser.add_argument('path')

    args = parser.parse_args()

