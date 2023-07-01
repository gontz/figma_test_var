import unittest
from figma_plugin.src.variable_creator import create_variables

class TestVariableCreator(unittest.TestCase):

    def setUp(self):
        self.style_data = {
            "styles": [
                {
                    "name": "Primary Color",
                    "value": "#ff0000"
                },
                {
                    "name": "Secondary Color",
                    "value": "#00ff00"
                }
            ]
        }
        self.expected_variables = {
            "Primary Color": "#ff0000",
            "Secondary Color": "#00ff00"
        }

    def test_create_variables(self):
        variables = create_variables(self.style_data)
        self.assertEqual(variables, self.expected_variables)

if __name__ == '__main__':
    unittest.main()