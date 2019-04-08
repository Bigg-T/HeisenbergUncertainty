#!/usr/bin/python3
import unittest
from dfs import *

class Test(unittest.TestCase):
    jobs = {
        'A': ['D', 'B', 'C', 'F'],
        'B':['D'],
        'C':['E'],
        'D':['F'],
        'E':[],
        'F':['E'],
        'G':[]
    }
    """Ensure that jobs have dependencies ran after its dependencies"""
    def test_add1(self):
        schedule = getSchedule(jobs)
        self.assertTrue(schedule['A'] > schedule['D'])
        self.assertTrue(schedule['A'] > schedule['B'])
        self.assertTrue(schedule['A'] > schedule['C'])
        self.assertTrue(schedule['A'] > schedule['F'])
        self.assertTrue(schedule['B'] > schedule['D'])
        self.assertTrue(schedule['C'] > schedule['E'])
        self.assertTrue(schedule['F'] > schedule['E'])

if __name__ == '__main__':
    unittest.main()
