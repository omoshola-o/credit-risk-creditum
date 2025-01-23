from setuptools import setup, find_packages

setup(
    name="credit_risk_assessment",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "scikit-learn>=0.24.0",
        "typing>=3.7.4",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A credit risk assessment system for individual and corporate applications",
    keywords="credit, risk, assessment, finance",
    python_requires=">=3.7",
)