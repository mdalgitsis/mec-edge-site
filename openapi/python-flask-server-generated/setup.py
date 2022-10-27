# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion",
    "swagger-ui-bundle>=0.0.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="Edge-API",
    author_email="mdalgitsis@vicomtech.org",
    url="",
    keywords=["Swagger", "Edge-API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    The Edge-API is built under the BIND5G project and its purpose is to act as an intermidiator between the NaaS API and the Kubernetes cluster. The NaaS API is a general API in respect of the project to remotely and automatically deploy, manage and control 5G and MEC infrastructures for a vast amount of experiments. On the other hand, the Edge-API is a specific backend API to manage Kubernetes resources and deploy application instances into the cluster.
    """
)
