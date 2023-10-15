from setuptools import setup
import os


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="snake",  # name of your package
    version="1.0.0",
    description="a terminal-based snake game",
    long_description=open_file("README.md"),  # only if you have a README.md
    author="Kristian and Stationary Siracha. Add your name here.",
    author_email="kristian.rother@posteo.de",
    packages=["snake"],  # same as folder name
    url="...",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
