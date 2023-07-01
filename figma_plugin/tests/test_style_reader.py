import unittest
from figma_plugin.src.style_reader import read_styles

class TestStyleReader(unittest.TestCase):

    def setUp(self):
        self.style_data = {
            "styles": [
                {
                    "id": "1",
                    "name": "Primary",
                    "styleType": "FILL",
                    "description": "Primary color",
                    "color": {
                        "r": 0.11,
                        "g": 0.59,
                        "b": 0.93,
                        "a": 1
                    }
                },
                {
                    "id": "2",
                    "name": "Secondary",
                    "styleType": "FILL",
                    "description": "Secondary color",
                    "color": {
                        "r": 0.96,
                        "g": 0.65,
                        "b": 0.14,
                        "a": 1
                    }
                }
            ]
        }

    def test_read_styles(self):
        result = read_styles(self.style_data)
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 2)
        self.assertIn('Primary', result)
        self.assertIn('Secondary', result)

if __name__ == '__main__':
    unittest.main()