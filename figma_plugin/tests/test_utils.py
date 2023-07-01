import unittest
from figma_plugin.src import utils

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.style_data = {
            "styles": [
                {"id": "1", "name": "style1", "description": "desc1", "value": "#FFFFFF"},
                {"id": "2", "name": "style2", "description": "desc2", "value": "#000000"}
            ]
        }
        self.variable_data = {
            "variables": [
                {"name": "style1", "value": "#FFFFFF"},
                {"name": "style2", "value": "#000000"}
            ]
        }

    def test_convert_style_to_variable(self):
        result = utils.convert_style_to_variable(self.style_data)
        self.assertEqual(result, self.variable_data)

    def test_get_style_by_id(self):
        style_id = "1"
        result = utils.get_style_by_id(self.style_data, style_id)
        self.assertEqual(result, self.style_data["styles"][0])

    def test_get_variable_by_name(self):
        variable_name = "style1"
        result = utils.get_variable_by_name(self.variable_data, variable_name)
        self.assertEqual(result, self.variable_data["variables"][0])

if __name__ == '__main__':
    unittest.main()