# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ""
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, "README.rst")
if os.path.exists(readme_path):
    with open(readme_path, "rb") as stream:
        readme = stream.read().decode("utf8")


setup(
    long_description=readme,
    name="pan-os-python",
    version="1.0.0",
    description="Framework for interacting with Palo Alto Networks devices via API",
    python_requires="!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,<4.0,>=2.7",
    project_urls={
        "documentation": "https://pan-os-python.readthedocs.io",
        "homepage": "https://github.com/PaloAltoNetworks/pan-os-python",
        "repository": "https://github.com/PaloAltoNetworks/pan-os-python",
    },
    author="Palo Alto Networks",
    author_email="devrel@paloaltonetworks.com",
    license="ISC",
    keywords="panos pan-os-python",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["examples", "panos"],
    package_dir={"": "."},
    package_data={"examples": ["*.rst"]},
    install_requires=["pan-python==0.*,>=0.10.0"],
    extras_require={
        "dev": [
            "bandit==1.*,>=1.6.2",
            'black==19.*,>=19.10.0; python_version == "3.*" and python_version >= "3.6.0"',
            'dephell==0.*,>=0.8.3; python_version == "3.*" and python_version >= "3.6.0"',
            'fissix==19.*,>=19.2.0; python_version == "3.*" and python_version >= "3.6.0"',
            "flake8==3.*,>=3.7.9",
            'flake8-bugbear==20.*,>=20.1.2; python_version == "3.*" and python_version >= "3.6.0"',
            "flake8-builtins==1.*,>=1.4.2",
            'flake8-comprehensions==3.*,>=3.1.4; python_version == "3.*" and python_version >= "3.5.0"',
            "flake8-docstrings==1.*,>=1.5.0",
            'flake8-eradicate==0.*,>=0.2.4; python_version == "3.*" and python_version >= "3.6.0"',
            "flake8-logging-format==0.*,>=0.6.0",
            "flake8-mock==0.*,>=0.3.0",
            "flake8-mutable==1.*,>=1.2.0",
            "flake8-pep3101==1.*,>=1.3.0",
            "flake8-pytest==1.*,>=1.3.0",
            "flake8-string-format==0.*,>=0.2.3",
            "flake8-variables-names==0.*,>=0.0.3",
            "isort==4.*,>=4.3.21",
            "m2r==0.*,>=0.2.1",
            "pep8-naming==0.*,>=0.9.1",
            'pytest==5.*,>=5.3.2; python_version == "3.*" and python_version >= "3.5.0"',
            'pytest-cov==2.*,>=2.8.1; python_version == "3.*" and python_version >= "3.5.0"',
            'sphinx==2.*,>=2.3.1; python_version == "3.*" and python_version >= "3.5.0"',
            'sphinx-autobuild==0.*,>=0.7.1; python_version == "3.*" and python_version >= "3.5.0"',
            'sphinx-rtd-theme==0.*,>=0.4.3; python_version == "3.*" and python_version >= "3.5.0"',
        ]
    },
)
