import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="point2d",
    version="0.0.1",
    author="Fabricio J.C. Montenegro",
    author_email="fabriciojcmontenegro@gmail.com",
    description="2D point class to represent cartesian and polar coordinates seemlessly.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SplinterDev/point2d",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
)