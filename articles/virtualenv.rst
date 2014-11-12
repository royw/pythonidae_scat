Why Python Virtual Environments Aren't
======================================

11/13/2014

This is because python's virtual environments are not real virtual environments.  They copy the binary executables but
not the python environment.  Here's what I mean::

    ➤ virtualenv -p /usr/bin/python3.3 /tmp/foobar
    Running virtualenv with interpreter /usr/bin/python3.3
    Using base prefix '/usr'
    New python executable in /tmp/foobar/bin/python3.3
    Also creating executable in /tmp/foobar/bin/python
    Installing setuptools, pip...done.

    ➤ cd /tmp/foobar

    ➤ ls -l
    total 12
    drwxrwxr-x 2 wrighroy wrighroy 4096 Nov  7 11:05 bin
    drwxrwxr-x 2 wrighroy wrighroy 4096 Nov  7 11:05 include
    drwxrwxr-x 3 wrighroy wrighroy 4096 Nov  7 11:05 lib

    ➤ ls -l bin
    total 3512
    -rw-rw-r-- 1 wrighroy wrighroy    2192 Nov  7 11:05 activate
    -rw-rw-r-- 1 wrighroy wrighroy    1248 Nov  7 11:05 activate.csh
    -rw-rw-r-- 1 wrighroy wrighroy    2461 Nov  7 11:05 activate.fish
    -rw-rw-r-- 1 wrighroy wrighroy    1129 Nov  7 11:05 activate_this.py
    -rwxrwxr-x 1 wrighroy wrighroy     242 Nov  7 11:05 easy_install
    -rwxrwxr-x 1 wrighroy wrighroy     242 Nov  7 11:05 easy_install-3.3
    -rwxrwxr-x 1 wrighroy wrighroy     214 Nov  7 11:05 pip
    -rwxrwxr-x 1 wrighroy wrighroy     214 Nov  7 11:05 pip3
    -rwxrwxr-x 1 wrighroy wrighroy     214 Nov  7 11:05 pip3.3
    lrwxrwxrwx 1 wrighroy wrighroy       9 Nov  7 11:05 python -> python3.3
    lrwxrwxrwx 1 wrighroy wrighroy       9 Nov  7 11:05 python3 -> python3.3
    -rwxrwxr-x 1 wrighroy wrighroy 3558736 Nov  7 11:05 python3.3

    ➤ ls -l include
    total 0
    lrwxrwxrwx 1 wrighroy wrighroy 23 Nov  7 11:05 python3.3m -> /usr/include/python3.3m

    ➤ ls -l lib
    total 4
    drwxrwxr-x 4 wrighroy wrighroy 4096 Nov  7 11:05 python3.3

    ➤ ls -l lib/python3.3/
    total 40
    lrwxrwxrwx 1 wrighroy wrighroy    25 Nov  7 11:05 abc.py -> /usr/lib/python3.3/abc.py
    lrwxrwxrwx 1 wrighroy wrighroy    28 Nov  7 11:05 base64.py -> /usr/lib/python3.3/base64.py
    lrwxrwxrwx 1 wrighroy wrighroy    28 Nov  7 11:05 bisect.py -> /usr/lib/python3.3/bisect.py
    ***[snip]***

Virtualenv decouples the python, pip, and easy_install executables by **copying** the python executable to the virtual
environments' bin directory then writes wrappers for pip and easy_install that use the copied python.  Cool.

The **include** sub-directory contains a symbolic link to /usr/include/python3.3m which is owned by::

    ➤ dpkg -S /usr/include/python3.3m
    python3.3-minimal, python3.3-dev: /usr/include/python3.3m

and **lib/python3.3** is owned by::

    ➤ dpkg -S /usr/bin/python3.3
    python3.3-minimal: /usr/bin/python3.3

Herein lies the gotcha.  Notice the versioning is only major.minor, but python releases using three part versioning:
major.minor.patch.  So if you upgrade, say from python 3.3.5 to python 3.3.6 (with for example, an
***apt-get dist-upgrade***), your virtualenv is now using python 3.3.5 with the support files from python 3.3.6.
Needless to say dragons galore!

The work-around is to upgrade the python in your virtualenv by using the non-intuitive pattern of creating a new
virtualenv over the existing virtualenv::

    ➤ virtualenv -p /usr/bin/python3.3 /tmp/foobar

Which just happens to be the same command we created the initial environment with.

Unfortunately this does not guarantee that you have slayed all the dragons, as any site-packages you have installed
may need to be reinstalled.  YMMV

So when your virtualenv and/or python app(s) break after a package upgrade (ex: ***apt-get dist-upgrade***), it may
be time to cleanup the pythonidae scat!

.. include:: copyright.rst
