#!/usr/bin/env python
# -*- coding: utf-8 -*-
from state import State
from argparse import ArgumentParser

def bfs(root): 
	queue = [root]
	path = []
	for state in queue:
		if state.isFinalState():
			path = [state]
			while state.parent:
				path.insert(0, state.parent)
				state = state.parent
			break
		queue.extend(state.getValidStateSuccessors())
	return path

def main():
	parser = ArgumentParser()
	parser.add_argument("missionaries", help="number of missionaries", type=int)
	parser.add_argument("cannibals", help="number of cannibals", type=int)
#   parser.add_argument("operators", help="number of valid operators", type=int)
	args = parser.parse_args()

	LEFT_SIDE = 0
	initial_state = State(args.missionaries, args.missionaries,
	args.cannibals, args.cannibals, LEFT_SIDE, [(1,0), (2,0), (1,1), (0,1), (0,2)])
	path = bfs(initial_state)
	
	for s in path:
		print(s.printBothSides())

if __name__ == "__main__":
	main()