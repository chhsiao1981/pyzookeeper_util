import os

from setuptools import setup, Extension, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

# requires
requires = [
]

setup(
    name='pyzookeeper_util',
    version='0.0',
    description='pyzookeeper_util',
    long_description=README,
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    author='',
    author_email='',
    url='',
    packages=find_packages(),
    keywords='web flask nirscloud',
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "ujson==5.4.0",
    ],
    dependency_links=[
    ],
    tests_require=[
    ],
    test_suite="",
)
