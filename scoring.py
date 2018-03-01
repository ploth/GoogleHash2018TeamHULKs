#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from parser import load_problem, load_solution, save_solution


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
    city.vehicles[0].ride_queue.append(city.rides[0])
    city.vehicles[1].ride_queue.append(city.rides[2])
    city.vehicles[1].ride_queue.append(city.rides[1])
    save_solution(solution_path+".me", city)


if __name__ == '__main__':
    main()
