import setuptools

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
	name = "openTIDAL",
	version = "1.0.1",
	license = "MIT",
	description = "Python Wrapper for libopenTIDAL",
	author = "DerNuntius",
	author_email = "hugo.melder@gmail.com",
	long_description=long_description,
	long_description_content_type='text/markdown',
	packages = setuptools.find_packages(),
	classifiers = [
		"Programming Language :: Python :: 3"
    	],
	platforms = "any",
	install_requires = ["cffi"],
	cffi_modules=['openTIDAL/_openTIDAL_build.py:ffibuilder']	
)
