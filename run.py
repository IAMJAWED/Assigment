"""Setup Module"""
from setuptools import setup

setup(name='sample',
      version='0.1',
      description='Sample Project Package',
      licence="Assignment",
      platform="windows",
      author='Md Jawed',
      author_email='jawed.ace@gmail.com',
      # packages=['WorkingPython', 'WorkingPython.templates'],
      packages=["WorkingPython"],
      # Include additional files into the package
      include_package_data=True,
     )

__author__ = 'MD Jawed'
