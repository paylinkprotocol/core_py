from setuptools import setup, find_packages

setup(
    name="paylink_protocol",
    version="1.0.0",
    description="A Python library for managing the PayLink Protocol on Ethereum.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Paylink Protocol",
    author_email="mail@paylinkprotocol.com",
    url="https://github.com/paylinkprotocol",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "web3>=5.0.0",
        "hexbytes>=0.2.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
