```python
import requests
import json

def fetch_styles(api_key, file_key):
    headers = {
        "X-Figma-Token": api_key
    }
    response = requests.get(f"https://api.figma.com/v1/files/{file_key}/styles", headers=headers)
    return json.loads(response.text)

def read_styles(style_data):
    styles = {}
    for style in style_data["meta"]["styles"]:
        styles[style["name"]] = style["style_type"]
    return styles

def create_variables(styles):
    variables = {}
    for style_name, style_type in styles.items():
        variables[style_name] = f"var {style_name} = styles.{style_name};"
    return variables

def send_message(message_name, data):
    figma.ui.postMessage({
        'pluginMessage': {
            'type': message_name,
            'data': data
        }
    })
```