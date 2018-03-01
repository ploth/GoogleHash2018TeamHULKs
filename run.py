#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

from parser import load_problem

def main():
    # read command line arguments
    arg_parser = argparse.ArgumentParser(description="Runs the hashcode solution",
                                         formatter_class=argparse.RawTextHelpFormatter)
    arg_parser.add_argument("input_path", help="help_text")
    args = arg_parser.parse_args()
    input_path = args.input_path

    city = load_problem(input_path)
    print(city)

    #  pizza.slices = [(0, 0, 2, 1), (0, 2, 3, 3), (3, 0, 4, 2)]

    #  write_solution_file(pizza)

if __name__ == '__main__':
    main()
