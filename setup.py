from setuptools import setup, find_packages

setup(
    name='pybrowser',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'PyQt5',
        'PyQtWebEngine'
    ],
    entry_points={
        'console_scripts': [
            'pybrowser=pybrowser.browser:main',
        ],
    },
)