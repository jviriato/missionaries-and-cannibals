#!/usr/bin/env python
# -*- coding: utf-8 -*-

from state import State

class Graph:
    def __init__(self, root):
        """
        Constrói um grafo. 
	    @param root: O primeiro nó do grafo/árvore
        """
        self.root = root

    def bfs(self): 
	"""
	Breadth-first search
	Um algoritmo para percorrer uma árvore ou grafo.
	"""
        queue = [self.root]
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
