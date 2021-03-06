from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES
import os

VERSION = '1.1'

# Make data go to the right place.
# http://groups.google.com/group/comp.lang.python/browse_thread/thread/35ec7b2fed36eaec/2105ee4d9e8042cb
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']


setup(
    name='django-input-mask',
    version=VERSION,
    description="JavaScript input masks for Django",
    long_description="This module provides JavaScript input masks for Django projects.",
    author="Codasus Technologies",
    author_email="contact@codasus.com",
    url="http://github.com/codasus/django-input-mask",
    license="Creative Commons Attribution-ShareAlike 3.0 Unported License",
    platforms=["any"],
    packages=['input_mask'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    include_package_data=True,
)
