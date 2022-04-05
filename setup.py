#!/usr/bin/python
import io
import os

from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name="rfc-tidy",
        version="0.1.1",
        author="Martin Thomson",
        author_email="mt@lowentropy.net",
        scripts=["rfc-tidy"],
        packages=find_packages(),
        description="Cleanup RFC XML",
        long_description=open("README.md").read(),
        long_description_content_type="text/markdown",
        classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: Console",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python",
        ],
        keywords="rfc ietf xml",
        python_requires=">=3.6",
        install_requires=[],
        url="https://github.com/martinthomson/rfc-tidy",
        license="MIT",
    )
