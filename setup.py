# -*- coding: utf-8 -*-
"""scons-tool-cxxtestgen
"""

from setuptools import setup
import setuptools.command.install
import setuptools.command.develop
import os
import sys

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    readme = f.read()

class develop(setuptools.command.develop.develop):

    def run(self, *args, **kw):
        subdir = os.path.join(here, 'sconstool', 'cxxtestgen')
        if not os.path.exists(subdir):
            os.makedirs(subdir)

        initpy = os.path.join(subdir, '__init__.py')
        if not os.path.exists(initpy):
            os.symlink('../../__init__.py', initpy)

        readme = os.path.join(subdir, 'README.txt')
        if not os.path.exists(readme):
            with open(readme, 'w') as f:
                f.write('The __init__.py symlink is just a workaround for ' +
                        'broken "pip install -e ."')

        if sys.version_info < (3,0):
            super(develop, self).run(*args, **kw)
        else:
            super().run(*args, **kw)

install = setuptools.command.install.install


setup(
        name='scons-tool-cxxtestgen',
        version='0.1.0',
        package_dir={'sconstool.cxxtestgen': '.'},
        packages=['sconstool.cxxtestgen'],
        namespace_packages=['sconstool'],
        description='SCons tool for cxxtestgen command',
        long_description=readme,
        long_description_content_type='text/x-rst',
        url='https://github.com/ptomulik/scons-tool-cxxtestgen',
        author='Paweł Tomulik',
        author_email='ptomulik@meil.pw.edu.pl',
        cmdclass={'develop': develop, 'install': install}
)

# vim: set expandtab tabstop=4 shiftwidth=4:
