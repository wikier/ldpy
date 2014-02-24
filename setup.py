# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
      name = 'ldpy',
      version = '0.1.0',
      description = 'LDP Client for Python',
      long_description = 'LDP Client for Python. Very prototypical, initially written to cross-testing Apache Marmotta reference implementation.',
      license = 'Apache Software License 2.0',
      author = "Sergio Fernandez",
      author_email = "wikier@apache.org",
      url = 'http://github.com/wikier/ldpy',
      download_url = 'http://github.com/wikier/ldpy/releases',
      platforms = ['any'],
      packages = ['ldpy'],
      requires = ['rdflib']
      install_requires = ['rdflib >= 4.1.0']
      classifiers =  [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
      ],
      keywords = 'python ldp linkeddata rdf marmotta',
      use_2to3 = True,
)

