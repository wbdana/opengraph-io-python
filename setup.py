from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="opengraphio",
    version="1.0.0",
    author="Will Dana",
    author_email="william.b.dana@gmail.com",
    description="A Python client for opengraph.io, a website scraper to grab OpenGraph tags or supplement them when they don't exist.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.github.com/wbdana/opengraph-io-python",
    packages=['opengraphio'],
    install_requires=[
        "requests>=2.19",
    ],
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)