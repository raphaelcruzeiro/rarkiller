import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "rarkiller",
    version = "0.0.2",
    author = "Raphael Cruzeiro",
    author_email = "raphaelcruzeiro@raphaelcruzeiro.com",
    description = ("A tool to remove all rar files from the specified directory and all of it's subdirectories"),
    license = "BSD",
    keywords = "rarkiller",
    url = "https://github.com/raphaelcruzeiro/rarkiller",
    packages=['rarkiller'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)

