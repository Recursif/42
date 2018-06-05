# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 14:03:48 2017

@author: yourself
"""

import unittest


def GameOfLife(is_alive, nb_voisin):
    if (nb_voisin < 2 or nb_voisin > 3):
        return (False)
    else:
        return (True)

 
class GameOfLifeTest(unittest.TestCase):

    def test_under_population(self):
        
        cell_is_alive = True
        population = 2
        
        cell_is_alive = GameOfLife(cell_is_alive, population)
        
        self.assertFalse(result)
    
    def test_normal_population(self):
        
        is_alive = True
        nb_neighbours = 2
        
        result = GameOfLife(is_alive, nb_neighbours)
        
        self.assertTrue(result)
    
    def test_over_population(self):
        
        is_alive = True
        nb_neighbours = 4
        
        result = GameOfLife(is_alive, nb_neighbours)
        
        self.assertFalse(result)
        
    
        

unittest.main()