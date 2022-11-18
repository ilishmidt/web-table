from setuptools import setup

from web_table_api.__version__ import __title__, __description__
from web_table_bl.__version__ import __version__

with open("README.md", "r", errors='ignore') as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as file:
    install_requires = [line.rstrip() for line in file]

setup(
    name=__title__,
    version=__version__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=install_requires,
    python_requires='>=3.8',
    include_package_data=True,
)
