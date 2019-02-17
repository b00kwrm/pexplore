from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="pexplore",
    version="0.0.1",
    description="Explore plaso files that have been turned to json by psort",
    long_description="long_description",
    long_description_content_type="text/markdown",
    url = "https://github.com/b00wrm/pexplore",
    author="b00kwrm",
    author_email="b00kwrm@example.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Topic :: Security",
        "License :: OSI Approved :: GPLv3",
        "Programming Language :: Python 3",
        "Programming Language :: Python 3.7",
        ],
    keywords="forensics, tooling, development",
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.7",
    extras_require={
        "dev": ["pytest", "pytest-cov"]
        },
    entry_points={
        "console_scripts": [
            "pexplore=pexplore.pexplore:main"
            ],
        },
    project_urls={
        "Source": "http://github.com/b00kwrm/pexplore"
        },
)
