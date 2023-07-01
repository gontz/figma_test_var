import unittest
from figma_plugin.src.figma_api import fetch_styles

class TestFigmaAPI(unittest.TestCase):

    def setUp(self):
        self.style_data_schema = {
            "name": str,
            "description": str,
            "style_type": str,
            "values": list
        }

    def test_fetch_styles(self):
        styles = fetch_styles()
        self.assertIsInstance(styles, list)
        for style in styles:
            self.assertDictContainsSubset(self.style_data_schema, style)

if __name__ == '__main__':
    unittest.main()