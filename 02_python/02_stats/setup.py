from setuptools import setup, find_packages

setup(
    name='op_stats',
    version='0.1.0',
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=[
        'flask'
    ]
)
