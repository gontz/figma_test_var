from setuptools import setup, find_packages

setup(
    name='figma-style-variable-creator',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'figma_style_variable_creator=figma_plugin.src.main:main',
        ],
    },
    url='https://github.com/user/figma-style-variable-creator',
    license='MIT',
    author='Your Name',
    author_email='your.email@example.com',
    description='A Figma plugin that reads styles and creates variables from them',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)