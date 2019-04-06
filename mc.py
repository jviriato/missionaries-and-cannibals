#!/usr/bin/env python
# -*- coding: utf-8 -*-

from graph import Graph
from state import State

LEFT_SIDE  = 0
RIGHT_SIDE = 1

class MissionariesCannibals:
    def __init__(self, missionaries, cannibals, boat_size):
        """
        Construtor do problema.
        :param missionaries: Número de missionários no lado esquerdo
        :param cannibals:    Número de canibais no lado esquerdo
        :param boat_size:    Número de pessoas que podem entrar no barco
        """
        self.missionaries   = missionaries
        self.cannibals      = cannibals
        self.boat_size      = boat_size
        self.operators      = self.getOperators(self.boat_size)
        self.initial_state  = State(self.missionaries, self.missionaries, 
                                    self.cannibals, self.cannibals,
                                    LEFT_SIDE, self.operators)
    def __str__(self):
        return '<Missionaries: {}, Cannibals: {}, Boat size: {}, Operators: {}>'.format(
                self.missionaries, self.cannibals, self.boat_size, self.operators)
    
    def getOperators(self, boat_size):
        """
        Função para adquirir os operadores válidos
        @param boat_size: Quantas pessoas o barco consegue levar
        """
        operators = []
        for m in range(boat_size + 1):
            for c in range(boat_size + 1):
                if ( ((c is not 0) or (m is not 0) ) and (c + m <= boat_size) ):
                    operators.append((m, c))
        return operators

    def printSolution(self, path):
        """
        Printa a solução, se houver
        @param: path é a array com a solução
        """
        for s in path:
    		print(s.printBothSides())
    
    def Search(self):
        """
        Faz a pesquisa através de um grafo
        """
        g = Graph(self.initial_state)
        path = g.bfs()
        self.printSolution(path)
