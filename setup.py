# -*- coding: utf8 -*-

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup

setup(
      name = 'ldpy',
      version = '0.1.0',
      description = 'LDP Client for Python',
      long_description = 'LDP Client for Python. Very prototypical, initially written to cross-testing Apache Marmotta reference implementation.',
      license = 'Apache Software License 2.0',
      author = "Sergio Fernandez",
      author_email = "sergio@wikier.org",
      url = 'http://github.com/wikier/ldpy',
      download_url = 'http://github.com/wikier/ldpy/releases',
      platforms = ['any'],
      packages = ['ldpy'],
      requires = ['rdflib', 'requests'],
      install_requires = ['rdflib >= 4.1.0'],
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

