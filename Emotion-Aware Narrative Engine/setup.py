from setuptools import setup, find_packages

setup(
    name="emotion-narrative-engine",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "transformers",
        "torch",
    ],
    author="Sanjana Robbi",
    author_email="sanjanarobbi123@gmail.com",
    description="An emotion detection system for game narrative enhancement",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sanjthebest/emotion-aware-narrative-engine",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
) 