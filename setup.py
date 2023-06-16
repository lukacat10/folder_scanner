from pathlib import Path
from setuptools import find_packages, setup

dependencies = []

# read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
    name="folder-scanner",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    version="0.0.1",
    description="Recursive file lookup by extension or name",
    author="Tom",
    author_email="lukacat100@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    project_urls={
        "Bug Tracker": "https://github.com/lukacat100/folder-scanner",
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=dependencies,
    extras_require={
        'dev': [
            'pytest',
            'IPython'
        ]
    },
    entry_points={
        "console_scripts": [
            "folder_scanner = folder_scanner:main",
        ]
    },
)
