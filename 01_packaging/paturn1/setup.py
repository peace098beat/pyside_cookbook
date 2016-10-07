# from distutils.core import setup
from setuptools import setup, find_packages
setup(
    name='ffp2',
    version='1.0',
    packages=['ffp2',
              'ffp2.model',
              'ffp2.view'],
    package_dir={'ffp2': 'src',
                 'ffp2.model': 'src/model',
                 'ffp2.view': 'src/view'
                 },
    test_suite='tests'
)
