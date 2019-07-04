#https://packaging.python.org/tutorials/packaging-projects/
#this is only necessary if you want to upload your package to the PyPI. (pip install example_pkg)
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-your-username",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package doing some math.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tomasdembelli/samplePythonPackage",
    packages=setuptools.find_packages(),
    #https://pypi.org/classifiers/
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
