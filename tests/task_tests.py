import unittest

from src.task import Task

class TestTask(unittest.TestCase):

    def setUp(self):
        self.wash_dishes = Task("wash dishes", 30, "cook dinner")
        self.cook_dinner = Task("cook dinner", 45, "clean windows")
        self.clean_windows = Task("clean windows", 60, "wash dishes")
    
    def test_task_has_description(self):
        self.assertEqual("wash dishes", self.wash_dishes.description)