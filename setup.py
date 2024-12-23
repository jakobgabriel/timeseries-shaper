import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "ts-shape",
    version = "0.0.0.19",
    author = "Jakob Gabriel",
    author_email = "jakob.gabriel5@googlemail.com",
    description = "ts-shape filters, transforms and engineers your timeseries dataframe",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://jakobgabriel.github.io/timeseries-shaper/timeseries_shaper.html",
    project_urls = {
        "Bug Tracker": "https://github.com/jakobgabriel/timeseries-shaper",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.10"
)