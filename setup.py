from setuptools import setup, find_packages
from io import open
import os

console_scripts = """
[console_scripts]
cwl2atom=cwl2atom.__init__:main
"""

print(find_packages(where='src'))

setup(entry_points=console_scripts,
      packages=find_packages(where='src'),
      package_dir={'': 'src'},
      install_requires=['nose'],
      setup_requires=['nose>=1.0'],
      test_suite='nose.collector',
      tests_require=['nose'])
