# Copyright 2014 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License.  You may obtain a copy of
# the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# License for the specific language governing permissions and limitations under
# the License.

"""This module installs the pyaff4 library."""
from distutils.core import setup
from setuptools.command.test import test as TestCommand

try:
    with open('../README.md') as file:
        long_description = file.read()
except IOError:
    long_description = ""


class NoseTestCommand(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # Run nose ensuring that argv simulates running nosetests directly
        import nose
        nose.run_exit(argv=['nosetests'])


setup(
    name='PyAFF4',
    long_description=long_description,
    version='0.13',
    description='Python Advanced Forensic Format Version 4 library.',
    author='Michael Cohen',
    author_email='scudette@gmail.com',
    url='https://www.aff4.org/',
    packages=['pyaff4'],
    package_dir={"pyaff4": "."},
    cmdclass={'test': NoseTestCommand},
    install_requires=[
        "rdflib >= 4.1",
        "intervaltree >= 2.0.4",
    ],
)
