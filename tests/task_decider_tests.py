import unittest

from src.task_decider import *
from src.task import Task

class TestTaskDecider(unittest.TestCase):
    
    def setUp(self):
        self.wash_dishes = Task("wash dishes", 30, "cook dinner")
        self.cook_dinner = Task("cook dinner", 45, "clean windows")
        self.clean_windows = Task("clean windows", 60, "wash dishes")

    def test_wash_dishes_preferred_over_cook_dinner(self):
        self.assertEqual("wash dishes", get_preferred_option(self.wash_dishes, self.cook_dinner))
        self.assertEqual("wash dishes", get_preferred_option(self.cook_dinner, self.wash_dishes))

    def test_cook_dinner_preferred_over_clean_windows(self):
        self.assertEqual("cook dinner", get_preferred_option(self.cook_dinner, self.clean_windows))
        self.assertEqual("cook dinner", get_preferred_option(self.clean_windows, self.cook_dinner))