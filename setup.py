from distutils.core import setup
from pathlib import Path

version = "1.0.1"
long_description = (Path(__file__).parent / "README.md").read_text(encoding="utf-8")

setup(
    name="Moogle",
    packages=["moogle", "DataStructures"],
    version=version,
    license="MIT",
    description="📦 Google Search API - Simple Python Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Deepak Soni",
    author_email="sonniiii@outlook.com",
    url="https://github.com/diezo/moogle",
    download_url=f"https://github.com/diezo/moogle/archive/refs/tags/v{version}.tar.gz",
    keywords=[
        "python",
        "google",
        "google-api",
        "google-search",
        "python-google",
        "google-search-api",
        "python-google-search"
    ],
    install_requires=[
        "requests",
        "bs4"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10"
    ]
)