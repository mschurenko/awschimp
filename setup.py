from setuptools import setup

import awschimp

setup(
    name="awschimp",
    version=awschimp.__version__,
    description="aws utils fit for a chimp",
    author="Matt Schurenko",
    author_email="matt.schurenko@gmail.com",
    url="https://github.com/mschurenko/awschimp",
    license="MIT",
    packages=["awschimp"],
    keywords=["aws", "sts", "boto", "profile", "awschimp", ],
    install_requires=[
        "boto3",
        "botocore",
    ],
    zip_safe=False
)
