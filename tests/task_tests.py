import unittest

from src.task import Task

class TestTask(unittest.TestCase):

    def setUp(self):
        self.wash_dishes = Task("wash dishes", 30, ["cook dinner", "wash clothes"])
        self.cook_dinner = Task("cook dinner", 45, ["clean windows", "do ironing"])
        self.do_ironing = Task("do_ironing", 60, ["wash dishes", "wash clothes"])
        self.wash_clothes = Task("wash_clothes", 60, ["cook dinner", "clean windows"])
        self.clean_windows = Task("clean windows", 60, ["do ironing", "wash dishes"])
    
    def test_task_has_description(self):
        self.assertEqual("wash dishes", self.wash_dishes.description)
    
    def test_task_has_duration(self):
        self.assertEqual(45, self.cook_dinner.duration)

    def test_task_has_preferred_over(self):
        self.assertEqual(["do ironing", "wash dishes"], self.clean_windows.preferred_over)