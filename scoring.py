#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

from parser import load_problem, load_solution
from simulate import score_solution


def main():
    # read command line arguments
    arg_parser = argparse.ArgumentParser(description="Scores the HashCode solution for the given problem",
                                         formatter_class=argparse.RawTextHelpFormatter)
    arg_parser.add_argument("problem", help="The problem file")
    arg_parser.add_argument("solution", help="The solution file")
    args = arg_parser.parse_args()
    problem_path = args.problem
    solution_path = args.solution

    city = load_problem(problem_path)
    solution = load_solution(solution_path, city)

    print(score_solution(solution))



if __name__ == '__main__':
    main()
