import json
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="oemetadata",
    version="2.0.0",
    description="Open Energy Metadata (OEMetadata) - The energy metadata standard",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/OpenEnergyPlatform/oemetadata",
    author="Ludwig Hülk",
    author_email="ludwig.huelk@rl-institut.de",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="OEFamily OEP JSON metadata schema open energy",
    packages=find_packages(exclude=["tests"]),
    package_data={"": ["./*.json"]},
    python_requires=">=3.6",
)
