import unittest
from Classes.unit_of_work import UnitOfWork
from Classes.repository import Repository
from Classes.api_handler import APIHandler
from File_Handler.file_saver import FileSaver
from Interface_Handler.color_picker import get_color_choice
from Interface_Handler.user_input import UserInputHandler
from colorama import Fore

class TestAPIHandler(unittest.TestCase):
    def setUp(self):
        self.api_handler = APIHandler()
    
    def test_get_all_posts(self):
        posts = self.api_handler.get_all_posts()
        self.assertIsInstance(posts, list, "Expected a list of posts")

    def test_get_post_by_id(self):
        post = self.api_handler.get_post_by_id(1)
        self.assertIsInstance(post, dict, "Expected a dictionary for a single post")
        self.assertEqual(post["id"], 1, "Post ID should match requested ID")

class TestUnitOfWork(unittest.TestCase):
    def setUp(self):
        self.uow = UnitOfWork(APIHandler())

    def test_add_and_get_history(self):
        self.uow.add_to_history({"id": 1, "title": "Test"})
        history = self.uow.get_history()
        self.assertEqual(len(history), 1, "History should contain one entry")

class TestFileSaver(unittest.TestCase):
    def setUp(self):
        self.file_saver = FileSaver()
        self.sample_data = [{"id": 1, "title": "Sample Title", "body": "Sample Body"}]
    
    def test_save_to_json(self):
        self.file_saver.save_to_json(self.sample_data, "test_posts.json")
        with open("test_posts.json", "r") as file:
            content = file.read()
            self.assertIn("Sample Title", content)

    def test_save_to_csv(self):
        self.file_saver.save_to_csv(self.sample_data, "test_posts.csv")
        with open("test_posts.csv", "r") as file:
            content = file.read()
            self.assertIn("Sample Title", content)

class TestColorPicker(unittest.TestCase):
    def test_get_color_choice(self):
        self.assertEqual(get_color_choice("1"), Fore.RED, "Color choice 1 should return Fore.RED")
        self.assertEqual(get_color_choice("3"), Fore.BLUE, "Color choice 3 should return Fore.BLUE")

class TestUserInputHandler(unittest.TestCase):
    def setUp(self):
        self.handler = UserInputHandler()

    def test_validate_id_valid(self):
        self.assertTrue(self.handler.validate_id("5"))

    def test_validate_id_invalid(self):
        self.assertFalse(self.handler.validate_id("abc"))

if __name__ == "__main__":
    unittest.main()
