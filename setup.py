from setuptools import setup

import picasa


setup(
    name='picasa',
    version=picasa.__version__,
    description='Display images from a picasa album with optional filtering on tags',
    long_description=open('README.rst').read(),
    author='George Hickman',
    author_email='george@ghickman.co.uk',
    url='http://github.com/ghickman/pelican-picasa',
    license=open('LICENSE').read(),
    install_requires=('gdata',),
)

