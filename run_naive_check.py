#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys
from parser import get_lines_from_file, interpret_lines
from writer import write_solution_file
from strategies import naive_check_strategy

def main():
    # read command line arguments
    arg_parser = argparse.ArgumentParser(description="Runs the hashcode solution",
                                         formatter_class=argparse.RawTextHelpFormatter)
    arg_parser.add_argument("input_path", help="help_text")
    args = arg_parser.parse_args()
    input_path = args.input_path

    lines = get_lines_from_file(input_path)
    city = interpret_lines(lines)

    naive_city = naive_check_strategy(city)

    print(naive_city)

if __name__ == '__main__':
    main()
