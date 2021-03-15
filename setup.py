#!/usr/bin/env python

from setuptools import setup, find_packages
from datetime import datetime

release = datetime.today().strftime('%Y.%m.%d.%H.%M').replace(".0", ".")

setup(name='sardana_tango',
      version=release,
      author="Sardana Controller Developers",
      author_email="sardana-devel@lists.sourceforge.net",
      maintainer="ALBA",
      maintainer_email="sardana-devel@lists.sourceforge.net",
      url="https://github.com/ALBA-Synchrotron/sardana-tango",
      packages=find_packages()
)
