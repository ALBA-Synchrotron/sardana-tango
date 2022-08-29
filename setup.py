#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

setup(
    name="sardana_tango",
    version="0.0.3",
    author="Sardana Controller Developers",
    author_email="sardana-devel@lists.sourceforge.net",
    maintainer="ALBA",
    maintainer_email="sardana-devel@lists.sourceforge.net",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    url="https://github.com/ALBA-Synchrotron/sardana-tango",
    packages=find_packages(),
    description="sardana tango controllers & macros",
    license="GPLv3",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="tango,sardana",
    python_requires=">=3.5",
    install_requires=["sardana", "pytango"]
)
