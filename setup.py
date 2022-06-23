from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in core_crm/__init__.py
from core_crm import __version__ as version

setup(
	name="core_crm",
	version=version,
	description="crm",
	author="crm",
	author_email="crm@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
