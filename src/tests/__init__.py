import unittest

from src.tests.grid_collision_tests import TestBoatCollision


def run_suite():
    suite = unittest.TestSuite()

    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestBoatCollision))

    return unittest.TextTestRunner(verbosity=3).run(suite)
