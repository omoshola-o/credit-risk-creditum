from setuptools import setup, find_packages

setup(
    name="credit-risk-assessment",
    version="0.1.0",
    author="Omoshola",
    author_email="owolabi.omoshola@outlook.com",
    description="A credit risk assessment package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="hhttps://github.com/omoshola-o/credit-risk-creditum",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "scikit-learn>=0.24.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)