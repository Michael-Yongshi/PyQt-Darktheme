import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Michael-Yongshi_Gui-Dark-Theme", # Replace with your own username
    version="1.0.0",
    author="Michael-Yongshi",
    author_email="4registration@outlook.com",
    description="A dark theme desktop gui package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Michael-Yongshi/Gui-Dark-Theme",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU GPL 3 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)