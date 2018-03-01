#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

import os

from parser import load_problem, save_solution
from simulate import score_solution
import strategies
def main():
    # read command line arguments
    arg_parser = argparse.ArgumentParser(description="Runs the hashcode solution",
                                         formatter_class=argparse.RawTextHelpFormatter)

    total_score = 0
    arg_parser.add_argument("strategy_name", help="Strategy name")
    for filename in os.listdir("./problems"):
        args = arg_parser.parse_args()
        strategy_name = args.strategy_name

        city = load_problem("./problems/%s" % filename)
        solution = strategies.__dict__[strategy_name](city)

        score = score_solution(solution)
        print("Score: %s" % score)
        save_solution("./solutions/%s_%s.out" % (filename, strategy_name), solution)
        total_score = total_score + score

    print("TotalScore: %s" % total_score)

if __name__ == '__main__':
    main()
