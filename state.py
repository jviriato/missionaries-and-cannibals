#!/usr/bin/env python
# -*- coding: utf-8 -*-
from operator import sub, add

LEFT_SIDE = 0
RIGHT_SIDE = 1

class State:
    def __init__(self, missionaries, missionaries_max, 
                       cannibals, cannibals_max, 
                       boat_dir, 
                       valid_operators, parent = None):
        """
            Constrói um novo objeto.
            :param missionaries: Número de missionários no lado esquerdo
            :param cannibals: Número de canibais no lado esquerdo
            :param missionaries_max: Número total de missionários
            :param cannibals_max: Número total de canibais
            :param boat_dir: Direção do barco (esquerda, direita)
            :param value: Tupla com missionários e canibais
            :param valid_operators: Operadores válidos
            :param parent: Pai do Estado
        """
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.missionaries_max = missionaries_max
        self.cannibals_max = cannibals_max
        self.boat_dir = boat_dir
        self.value = (missionaries, cannibals)
        self.valid_operators = valid_operators
        self.parent = parent

    def __str__(self):
        if  (self.boat_dir == 0):
            return '<State {}, {}, "Left Side">'.format(self.value[0], self.value[1])
        elif(self.boat_dir == 1):
            return '<State {}, {}, "Right Side">'.format(self.value[0], self.value[1])
    __repr__ = __str__

    def __eq__(self, other):
        return self.missionaries == other.missionaries and self.cannibals == other.cannibals
   
    def __hash__(self):
        return hash(self.value)

    def printBothSides(self):
        """
        Printa ambos os lados
        """
        if  (self.boat_dir == 0):
            return '<Left Side {}, {}>b\t\t  <Right Side {}, {}">'.format(self.value[0], self.value[1],
            self.missionariesOnRight(), self.cannibalsOnRight())
        elif(self.boat_dir == 1):
            return '<Left Side {}, {}>\t\t b<Right Side {}, {}">'.format(self.value[0], self.value[1],
                            self.missionariesOnRight(), self.cannibalsOnRight())

    def isFinalState(self):
        """
        Função para verificar se está no estado final. Onde não há nenhum missionário ou canibal 
        do lado esquerdo, e o barco está do lado direito. 
        
        Retorna um booleano. 
        """
        return self.value == (0, 0) and self.boat_dir == RIGHT_SIDE
    
    def cannibalsOnRight(self):
        """
        Retorna o número de canibais do lado direito
        """
        return self.cannibals_max - self.cannibals

    def missionariesOnRight(self):
        """
        Retorna o número de missionarios do lado direito
        """
        return self.missionaries_max - self.missionaries

    def isStateValid(self):
        """
        Função para verificar se o estado é válido. Para um estado ser válido, o número de
        canibais nunca pode ser maior que o de missionários. 
        
        Retorna um booleano.
        """
        if(self._invalidStates() or self._cannibalsOutnumbersMissionaries() ):
            return False
        else:
            return True

    def _invalidStates(self):
        """
        Função auxiliar que trata de casos impossíveis.
        """
        return (self.missionaries < 0           or 
                self.cannibals    < 0           or
                self.cannibalsOnRight() < 0     or
                self.missionariesOnRight() < 0  or
               (self.boat_dir != 0 and self.boat_dir != 1))

    def _cannibalsOutnumbersMissionaries(self):
        """
        Função auxiliar que trata dos casos em que canibais estão em maior número.
        """ 
        #         canibais > missionarios na esquerda
        return  ( (self.missionaries > 0 and self.cannibals > self.missionaries) or
        #         canibais > missionarios na direita
                  (self.missionariesOnRight() > 0 and 
                   self.cannibalsOnRight() > self.missionariesOnRight()) 
                )

    def __addTuple(self, a, b):
        """
        Funções auxiliares para operações com tuplas
        """
        return tuple(map(add, a, b))

    def __subTuple(self, a, b):
        """
        Funções auxiliares para operações com tuplas
        """
        return tuple(map(sub, a, b))


    def _getStateSuccessors(self):
        """
        Função que retorna os estados sucessores
        """
        successors = []
        for operator in self.valid_operators:
            if(self.boat_dir == LEFT_SIDE):
                tuplex = self.__subTuple(self.value, operator)
                st = State(tuplex[0], self.missionaries_max, tuplex[1], self.cannibals_max,
                            RIGHT_SIDE, self.valid_operators, parent = self)
                successors.append(st)
            elif (self.boat_dir == RIGHT_SIDE):
                tuplex = self.__addTuple(self.value, operator)
                st = State(tuplex[0], self.missionaries_max, tuplex[1], self.cannibals_max,
                            LEFT_SIDE, self.valid_operators, parent = self)
                successors.append(st)
        return successors
        
    def getValidStateSuccessors(self):
        """
        Função que retorna os estados sucessores VÁLIDOS
        """
        valid_successors = []
        states = self._getStateSuccessors()
        for state in states:
            if state.isStateValid():
                valid_successors.append(state)
        return valid_successors