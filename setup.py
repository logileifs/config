# -*- coding: utf-8 -*-

from setuptools import setup

setup(
	name='figa',
	#packages=['guid'],
	include_package_data=True,
	zip_safe=False,
	install_requires=['pyyaml'],
	keywords='config python',
	version='0.1.0',
	description="Human friendly YAML parser and configuration module",
	long_description="Human friendly YAML parser and configuration module",
	author='Logi Leifsson',
	author_email='logileifs@gmail.com',
	url='https://github.com/logileifs/figa.git',
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
		"Operating System :: OS Independent",
	],
)
