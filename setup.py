#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

setup(
    name="sardana_tango",
    version="0.0.1",
    author="Sardana Controller Developers",
    author_email="sardana-devel@lists.sourceforge.net",
    maintainer="ALBA",
    maintainer_email="sardana-devel@lists.sourceforge.net",
    url="https://github.com/ALBA-Synchrotron/sardana-tango",
    packages=find_packages(),
    description="sardana tango controllers & macros",
    license="GPLv3",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="tango,sardana",
    python_requires=">=3.5"
)
