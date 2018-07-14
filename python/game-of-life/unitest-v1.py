# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 14:57:34 2017

@author: yourself
"""

import unittest

import Tkinter as Tk

class GameOfLife():
    
    def alive_cell_and_populationequals1(self):
        return (False)
        
    def alive_cell_and_sustainable_population(self):
        return (True)
        
    def alive_cell_and_over_population(self):
        return (False)
        
    def dead_cell_and_population_equals_3(self):
        return (True)


class alive_cell_should(unittest.TestCase):

    def test_die_if_populationequals0(self):
        
        cell = alive_cell;
        
        cell_new_state = cell.underpopulation()
        
        self.assertFalse(cell_is_alive)
        
    def test_die_if_populationequals1(self):
        
        Game = GameOfLife()
        
        cell_is_alive = Game.alive_cell_and_populationequals1()
        
        self.assertFalse(cell_is_alive)

    def test_stayalive_if_sustainable_population(self):
    
        Game = GameOfLife()
        
        cell_is_alive = Game.alive_cell_and_sustainable_population()
        
        self.assertTrue(cell_is_alive)

    def test_die_if_over_population(self):
    
        Game = GameOfLife()
        
        cell_is_alive = Game.alive_cell_and_over_population()
        
        self.assertFalse(cell_is_alive)
        
class dead_cell_should(unittest.TestCase):
    
    def test_pop_if_population_equals_3(self):
        
        Game = GameOfLife()
        
        cell_is_alive = Game.dead_cell_and_population_equals_3()
        
        self.assertTrue(cell_is_alive)
    
        

unittest.main()

window.mainloop()