```python
import requests
import json

class FigmaAPI:
    def __init__(self, token):
        self.token = token
        self.headers = {'X-Figma-Token': self.token}

    def fetch_styles(self, file_id):
        url = f"https://api.figma.com/v1/files/{file_id}/styles"
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            raise Exception("Failed to fetch styles from Figma API")
        return json.loads(response.text)

    def fetch_style(self, style_id):
        url = f"https://api.figma.com/v1/styles/{style_id}"
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            raise Exception("Failed to fetch style from Figma API")
        return json.loads(response.text)
```