import unittest
from figma_plugin.src.main import Main

class TestMain(unittest.TestCase):

    def setUp(self):
        self.main = Main()

    def test_fetch_styles(self):
        result = self.main.fetch_styles()
        self.assertIsNotNone(result)

    def test_read_styles(self):
        styles = self.main.fetch_styles()
        result = self.main.read_styles(styles)
        self.assertIsNotNone(result)

    def test_create_variables(self):
        styles = self.main.fetch_styles()
        read_styles = self.main.read_styles(styles)
        result = self.main.create_variables(read_styles)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()