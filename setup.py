import setuptools


setuptools.setup(
    name="onfinance_db_model_master",
    version="1.0.0",
    author="Priyesh Srivastava",
    author_email="priyesh@onfinance.in",
    description="-",
    long_description="------",
    long_description_content_type="text/markdown",
    url="https://github.com/OnFinance/onfinance_db_model_master",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["mongoengine==0.24.1"]
)