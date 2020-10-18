from setuptools import setup, find_packages

setup(
    name="crispycarnival",
    version="0.1",
    author="Rachael Elizabeth",
    description="Test project with dependencies and fake tests for writing Jenkins libaries.",
    install_requires=[
        'jinja2',
        'click',
        'pyyaml',
        'cerberus'
    ],
    entry_points={
        'console_scripts': [
            'crispycarnival=crispycarnival.__main__:main'
        ],
    },
    packages=find_packages(exclude="test")
)
