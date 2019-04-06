#!/usr/bin/env python
# -*- coding: utf-8 -*-
from argparse import ArgumentParser
from mc import MissionariesCannibals

def main():
	parser = ArgumentParser()
	parser.add_argument("missionaries", help="number of missionaries", type=int)
	parser.add_argument("cannibals", help="number of cannibals", type=int)
  	parser.add_argument("boat_size", help="number of people who can be put on a boat", type=int)
	args = parser.parse_args()

	mc_problem = MissionariesCannibals(args.missionaries, args.cannibals, args.boat_size)
	mc_problem.Search()

if __name__ == "__main__":
	main()