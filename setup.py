import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()
with open("requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh]

setuptools.setup(
    name="fixdate",
    version="1.13.5",
    author="Hendrik du Toit",
    author_email="hendrik@brightedge.co.za",
    description="Fix a date and present it in specified format.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    # packages=setuptools.find_packages(),
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=requirements,
)
