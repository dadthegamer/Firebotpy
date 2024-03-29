from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="firebotpy",
    version="4.0",
    license="MIT",
    description="Python library to connect to Firebots API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="DadTheGam3r",
    author_email="bailey_craig@me.com",
    url="https://github.com/whatupcraig/Firebotpy",
    download_url="https://github.com/whatupcraig/Firebotpy.git",
    keywords=["firebot", "api", "twitch"],
    install_requires=["requests"],
    packages=find_packages(),
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",  # Define that your audience are developers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
