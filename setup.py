import json
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="oemetadata",
    version="1.5.1a1",
    description="Open Energy Platform (OEP) - metadata schemas, examples and templates package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OpenEnergyPlatform/oemetadata",
    author="Alexis Michaltsis",
    author_email="oep_dev@lists.riseup.net",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="JSON metadata schema open energy platform oep",
    packages=find_packages(exclude=["tests"]),
    package_data={"": ["./*.json"]},
    python_requires=">=3.6",
)
