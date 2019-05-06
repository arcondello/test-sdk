# Copyright 2018 D-Wave Systems Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#
# ================================================================================================
from __future__ import absolute_import

import sys
from setuptools import setup

_PY2 = sys.version_info.major == 2

# add __version__, __author__, __authoremail__, __description__ to this namespace
# equivalent to:
if _PY2:
    execfile("./dwaveoceansdk/package_info.py")
else:
    exec(open("./dwaveoceansdk/package_info.py").read())


# the packages that have pinned versions
dwave_install_requires = [
    'dwave-networkx==0.7.1',
    'dwave-system==0.7.2',
    'dwave-qbsolv==0.2.10',
    'dwave-hybrid==0.2.1',
    'dwave-neal==0.4.6',
    'dwave-tabu==0.1.4',
    'dimod==0.8.11',
    ]

dwave_extras_require = {
    ':(platform_machine == "x86_64" or platform_machine == "amd64" or platform_machine == "AMD64") and python_version != "3.4"': [
        'dwavebinarycsp[mip]==0.0.11'
    ],
    ':platform_machine != "x86_64" and platform_machine != "amd64" and platform_machine != "AMD64" or python_version == "3.4"': [
        'dwavebinarycsp[maxgap]==0.0.11'
    ]
}

# other packages that we support/require that have version ranges
install_requires = [
    'numpy<1.16.0',     # only while we support py34
    'pyqubo>=0.3.0',
]
install_requires.extend(dwave_install_requires)


extras_require = {}
extras_require.update(dwave_extras_require)


packages = ['dwaveoceansdk']

classifiers = [
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
]

python_requires = '>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*'

setup(
    name='dwave-ocean-sdk',
    version=__version__,
    author=__author__,
    author_email=__authoremail__,
    description=__description__,
    url='https://github.com/dwavesystems/dwave-ocean-sdk',
    long_description=open('README.rst').read(),
    classifiers=classifiers,
    python_requires=python_requires,
    license='Apache 2.0',
    packages=packages,
    install_requires=install_requires,
    extras_require=extras_require
)
