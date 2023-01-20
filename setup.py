#!/usr/bin/env python
from setuptools import setup

setup(name='FeedSDK-Python',
      version='1.0.1',
      description='Python SDK for downloading and filtering item feed files',
      install_requires=[
          "urllib3==1.26.5",
          "certifi==2019.3.9",
          "aenum==2.1.2",
          "pandas==0.24.2",
          "SQLAlchemy==1.3.3"
      ],
      url='https://github.com/dimetris/FeedSDK-Python')
