import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ripple-effect",
    version="0.1.0",
    author="Nikhil Pandey",
    author_email="nikhil@nikhil.com.np",
    description="Ripple Effect Solver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nikhil-pandey/ripple-effect",
    packages=setuptools.find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Games/Entertainment :: Puzzle Games',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
)