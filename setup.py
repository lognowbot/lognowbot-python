from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="lognowbot",
    version="0.1.0",
    author="LogNowBot",
    author_email="contact@lognowbot.com",
    description="Python library for sending notifications via LogNowBot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lognowbot/lognowbot-python",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
    ],
    keywords="notification, logging, bot, telegram",
    project_urls={
        "Bug Reports": "https://github.com/lognowbot/lognowbot-python/issues",
        "Source": "https://github.com/lognowbot/lognowbot-python",
    },
)