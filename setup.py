#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name="autoflight",
      py_modules=['autoflight'],
      version="1.0.2",
      description="A simple script to upload a given .apk or .ipa to testflight.",
      license="MIT",
      author="Andrea Stagi",
      author_email="stagi.andrea@gmail.com",
      url="https://github.com/atooma/autoflight",
      keywords= "testflight app ios android test apk ipa script",
      install_requires=[
        "requests",
      ],
      entry_points = {
        'console_scripts': [
            'autoflight = autoflight:main',
        ],
      },
      zip_safe = True)
