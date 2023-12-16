from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in test_repo/__init__.py
from test_repo import __version__ as version

setup(
	name="test_repo",
	version=version,
	description="Test Repository",
	author="Balamurugan",
	author_email="bramachandran@techfinite.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
