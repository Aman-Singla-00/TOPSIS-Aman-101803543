from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
	name='TOPSIS-Aman-101803543' ,
	version='0.0.1' ,
	description='TOPSIS Package' ,
	long_description=long_description,
    long_description_content_type="text/markdown",
	py_modules=["helloworld"] ,
	author="Aman Singla",
    author_email="asingla2_be18@thapar.edu",
	classifiers=[
        	"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
        	"License :: OSI Approved :: MIT License",
        	"Operating System :: OS Independent",
	],
	install_requires = [
		"blessings ~= 1.7",
	],
	extras_require = {
		"dev": [
			"pytest>=3.7",
		],
	},
	package_dir={'':'src'}
)