#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys
from parser import get_lines_from_file, interpret_lines
from writer import write_solution_file

def main():
    # read command line arguments
    arg_parser = argparse.ArgumentParser(description="Runs the hashcode solution",
                                         formatter_class=argparse.RawTextHelpFormatter)
    arg_parser.add_argument("input_path", help="help_text")
    args = arg_parser.parse_args()
    input_path = args.input_path

    lines = get_lines_from_file(input_path)
    city = interpret_lines(lines)

    print(city)

    #  pizza.slices = [(0, 0, 2, 1), (0, 2, 3, 3), (3, 0, 4, 2)]

    #  write_solution_file(pizza)

if __name__ == '__main__':
    main()
