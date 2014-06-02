import os

from setuptools import setup, find_packages()

README = open( os.path.join( os.path.dirname( __file__ ), 'README.rst' ) ).read()

# allow setup.py to be run from any path
os.chdir( os.path.normpath( os.path.join( os.path.abspath( __file__ ), os.pardir ) ) )

setup(
    name = 'django-dynamic-fields',
    version = '0.1',
    packages = [ 'dynamicfields' ],
    include_package_data = True,
    license = 'BSD License',
    description = 'Dynamic meta fields that allow a set of custom fields to be specified on a model instance',
    long_description = README,
    author='twstd.dev',
    classifiers=[
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
    ],
)
