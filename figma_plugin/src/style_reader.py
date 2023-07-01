```python
import json
from figma_api import fetch_styles

def read_styles():
    styles = fetch_styles()
    style_data = json.loads(styles)

    return style_data

def extract_color_styles(style_data):
    color_styles = {}

    for style in style_data:
        if style['type'] == 'FILL':
            color_styles[style['name']] = style['color']

    return color_styles

def extract_text_styles(style_data):
    text_styles = {}

    for style in style_data:
        if style['type'] == 'TEXT':
            text_styles[style['name']] = {
                'font_family': style['fontFamily'],
                'font_size': style['fontSize'],
                'font_weight': style['fontWeight'],
                'line_height': style['lineHeight'],
                'letter_spacing': style['letterSpacing']
            }

    return text_styles

def extract_effect_styles(style_data):
    effect_styles = {}

    for style in style_data:
        if style['type'] == 'EFFECT':
            effect_styles[style['name']] = style['effects']

    return effect_styles
```