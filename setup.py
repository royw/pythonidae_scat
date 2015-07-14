import os
import re
from setuptools import setup

from sys import version

if version < '2.2.3':
    print('Pythonidae Scat requires python 2.6 or newer')
    exit(-1)


VERSION_REGEX = r'__version__\s*=\s*[\'\"](\S+)[\'\"]'


def get_project_version():
    """
    Get the version from __init__.py with a line: /^__version__\s*=\s*(\S+)/
    If it doesn't exist try to load it from the VERSION.txt file.
    If still no joy, then return '0.0.0'

    :returns: the version string
    :rtype: str
    """

    # trying __init__.py first
    try:
        file_name = os.path.join(os.getcwd(), 'pythonidae_scat', '__init__.py')
        with open(file_name, 'r') as inFile:
            for line in inFile.readlines():
                match = re.match(VERSION_REGEX, line)
                if match:
                    return match.group(1)
    except IOError:
        pass

    # no joy, so try getting the version from a VERSION.txt file.
    try:
        file_name = os.path.join(os.getcwd(), 'pythonidae_scat', 'VERSION.txt')
        with open(file_name, 'r') as inFile:
            return inFile.read().strip()
    except IOError:
        pass

    # no joy again, so return default
    return '0.0.0'


setup(
    name='Pythonidae Scat',
    version=get_project_version(),
    author='royw',
    author_email='roy@wright.org',
    url='http://pythonidae_scat.example.com',
    packages=['pythonidae_scat'],
    package_dir={'': '.'},
    package_data={'pythonidae_scat': ['*.txt', '*.js', '*.html', '*.css'],
                  'tests': ['*'],
                  '': ['*.rst', '*.txt', '*.rc', '*.in']},
    license='license.txt',
    description='Python Articles',
    long_description=open('README.rst').read(),
    # use keywords relevant to the application
    keywords=[],
    # use classifiers from:  https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    install_requires=[
        # "argparse",
        # "mako"
        # "Foo >= 1.2.3",
        'fullmonty',
    ],
    entry_points={
        'console_scripts': ['pythonidae_scat = pythonidae_scat.pythonidae_scat_main:main']
    })
