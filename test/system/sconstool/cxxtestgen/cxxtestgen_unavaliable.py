# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#
# Copyright (c) 2018 by Paweł Tomulik <ptomulik@meil.pw.edu.pl>
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

"""
Ensure that the tool does not blow up if there is no cxxtestgen script in path.
"""

import TestSCons
import sys
import os

if sys.platform == 'win32':
    test = TestSCons.TestSCons(program='scons.bat', interpreter=None)
else:
    test = TestSCons.TestSCons()

test.subdir('cxxtest')
try:
    test.dir_fixture('../../../../cxxtest', 'cxxtest')
except OSError:
    # test with other cxxtest, if there is no cxxtest in project tree
    pass

test.file_fixture('../../../../__init__.py', 'site_scons/site_tools/cxxtestgen/__init__.py')
test.file_fixture('../../../../about.py', 'site_scons/site_tools/cxxtestgen/about.py')
test.file_fixture('../../../../detail_.py', 'site_scons/site_tools/cxxtestgen/detail_.py')

test.write('SConstruct', """
env = Environment(tools=['cxxtestgen'], ENV={'PATH': ''}, CXXTESTBINPATH='')
print("$CXXTESTGEN: %r" % env.subst("$CXXTESTGEN"))
print("$CXXTESTGENPYTHON: %r" % env.subst("$CXXTESTGENPYTHON"))
""")

test.run()

test.must_contain_all_lines(test.stdout(), [("$CXXTESTGEN: %r" % 'cxxtestgen'),
                                            ("$CXXTESTGENPYTHON: %r" % sys.executable)])

test.pass_test()

# Local Variables:
# tab-width:4
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=4 shiftwidth=4:
