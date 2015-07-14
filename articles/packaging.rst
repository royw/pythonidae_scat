Python Packaging Melee
======================

14 November 2014

Packaging a project facilitates installing and using your software.  Packaging is very useful if you use virtual
environments.  The python community recognizes the need and have attempted several packaging schemes in the past,
and probably more in the future.  For details, please start with Martijn Faassen's 2009 article: 'A history of
Python packaging <http://blog.startifact.com/posts/older/a-history-of-python-packaging.html>'_.

Since Martijn's article, the python community has established a working group for packaging, Python Packaging
Authority (PyPA), to improve python packaging.  The PyPA publishes the 'Python Packaging User Guide
<https://python-packaging-user-guide.readthedocs.org/en/latest/>'_ which is a great starting point for
understanding current python packaging.

Here's the authoritative list for python 'Packaging History <https://packaging.python.org/en/latest/history.html>'_.

One of the side-effects of pythons turbulent packaging history is there are useful projects out there that
do not support the packaging schemes, so you can not install them with pip.  What do you do then?
First, try to find an equivalent project that is properly packaged.  If for some reason you can't, then
you can create a setup.py, populate with your best guesses, then build a local package that pip can then
install.  And if you are feeling really nice, you can issue a pull request.
