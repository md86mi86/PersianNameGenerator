from setuptools import setup, find_packages

setup(
    name="PersianNameGenerator",
    version="1.0",
    author="Mohammad Maleki",
    author_email="mohammad2007maleki@gmail.com",
    description="A library for generating random Persian names.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/PersianNameGenerator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)