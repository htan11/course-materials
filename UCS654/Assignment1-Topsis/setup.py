from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Topsis-Harsh-102303812",
    version="1.0.0",
    author="Harsh Tanwar",
    author_email="htanwar_be23@thapar.edu",
    description="A Python package to implement TOPSIS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/htan11/course-materials/tree/main/UCS654/Assignment1-Topsis",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "topsis=Topsis_Harsh_102303812.topsis:main",
        ],
    },
)
