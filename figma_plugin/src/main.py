```python
import figma_api
import style_reader
import variable_creator

def main():
    # Fetch styles from Figma API
    styles = figma_api.fetch_styles()

    # Read the styles
    style_data = style_reader.read_styles(styles)

    # Create variables from the styles
    variables = variable_creator.create_variables(style_data)

    # Print the variables
    for variable in variables:
        print(variable)

if __name__ == "__main__":
    main()
```