from setuptools import setup, find_packages
import pathlib

# Read the long description from README.md
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="gpsa",
    version="0.6.1",
    author="Andy Jones",
    author_email="ajones788@gmail.com",
    description="Gaussian Process Spatial Alignment (GPSA)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/engelhardtgpsa/spatial-alignment",
    download_url="https://github.com/engelhardtgpsa/spatial-alignment/archive/refs/tags/v0.6.tar.gz",
    packages=find_packages(include=["gpsa", "gpsa.*"]),
    python_requires=">=3.7, <4.0",
    install_requires=[
        "torch==2.2.2",
        "numpy>=1.21,<1.25",
        "pandas>=1.3.5,<2.3",
        "scikit-learn==1.0.2",
        "pcpca==0.3",
        "plottify==1.1",
        "scanpy==1.9.1",
        "scipy>=1.8,<1.11",
        "seaborn==0.11.2",
        "statsmodels==0.13.2",
        "anndata==0.8.0",
        "auto_mix_prep==0.2.0",
        "matplotlib==3.5.1",
        "tensorflow-macos>=2.10,<2.13",
        "tqdm==4.64.0",
        "squidpy==1.1.2",
    ],
    extras_require={
        "dev": [
            "flake8",
            "pytest",
            "pip-tools"
        ]
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: Apache Software License",
    ],
)
