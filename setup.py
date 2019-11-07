from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="oep-metadata",
    version="1.0.0",
    description="Open Energy Platform (OEP) - metadata schemas, examples and templates package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OpenEnergyPlatform/metadata",
    author="Alexis Michaltsis",
    author_email="a.michaltsis@rl-institut.de",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    keywords="JSON metadata schema open energy platform oep",
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.6",
)
