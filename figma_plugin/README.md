# Figma Style Reader Plugin

This is a Figma plugin that reads the styles from a Figma document and creates variables from them.

## Installation

1. Clone this repository
2. Navigate to the `figma_plugin` directory
3. Run `python setup.py install`

## Usage

1. Open Figma and navigate to the Plugins menu
2. Select the 'Figma Style Reader' plugin
3. The plugin will automatically read the styles from the current Figma document and create variables from them

## Files

- `src/main.py`: The main entry point for the plugin
- `src/figma_api.py`: Contains functions for interacting with the Figma API
- `src/style_reader.py`: Contains functions for reading styles from the Figma API response
- `src/variable_creator.py`: Contains functions for creating variables from the styles
- `src/utils.py`: Contains utility functions used across the plugin
- `tests/test_main.py`: Contains tests for `main.py`
- `tests/test_figma_api.py`: Contains tests for `figma_api.py`
- `tests/test_style_reader.py`: Contains tests for `style_reader.py`
- `tests/test_variable_creator.py`: Contains tests for `variable_creator.py`
- `tests/test_utils.py`: Contains tests for `utils.py`
- `setup.py`: Contains setup information for the plugin

## Contributing

Please read through our contributing guidelines. Included are directions for opening issues, coding standards, and notes on development.

## License

This project is licensed under the MIT License.