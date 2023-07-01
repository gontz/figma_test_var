```python
import json
from figma_api import fetch_styles

def create_variables():
    styles = fetch_styles()
    variables = {}

    for style in styles:
        variable_name = style['name'].replace(' ', '_').lower()
        variables[variable_name] = style['value']

    return variables

def save_variables_to_file(variables, filename='variables.json'):
    with open(filename, 'w') as file:
        json.dump(variables, file)

if __name__ == "__main__":
    variables = create_variables()
    save_variables_to_file(variables)
```