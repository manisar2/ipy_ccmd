from os import path
from setuptools import setup

def get_long_description():
    with open(
        path.join(path.dirname(path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()

setup(
    name='ipy_codecell_md',
    author='manisar',
    author_email='manisar@randompearls.com',
    install_requires=[
        'forbiddenfruit',
        'ipython'
    ],
    description='Show markdown from code cells in IPython',
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    license='MIT License',
    packages=['ipy_codecell_md'],
    keywords='ipython, markdown, codecell',
    varsion='0.0.1',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ]
)