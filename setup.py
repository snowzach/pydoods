import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pydoods",
    version="1.0.2",
    author="Zach Brown",
    author_email="doods@prozach.org",
    description="A Python wrapper for the DOODS image detection service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/snowzach/pydoods",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
