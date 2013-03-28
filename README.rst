.. 

stockmanager
======================

Quickstart
----------

To bootstrap the project::

    virtualenv stockmanager
    source stockmanager/bin/activate
    cd path/to/stockmanager/repository
    pip install -r requirements.pip
    pip install -e .
    cp stockmanager/settings/local.py.example stockmanager/settings/local.py
    manage.py syncdb --migrate

Documentation
-------------

Developer documentation is available in Sphinx format in the docs directory.

Initial installation instructions (including how to build the documentation as
HTML) can be found in docs/install.rst.
