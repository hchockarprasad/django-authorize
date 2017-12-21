=====
Authorize
=====

|travis| |codacy| |coverage| |pypipackage|

Authorize is a simple Django authentication app to to provide role based
authentication for users.

Detailed documentation will be uploaded soon.

Quick start
-----------

1. Install "authorize" like this::

    pip install django-authorize

2. Add "authorize" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'authorize',
    ]

3. Include the authorize URLconf in your project urls.py like this::

    path('auth/', include('authorize.urls')),

4. Include the authorize API URLconf in your project urls.py like this::

    path('auth/api/' include('authorize.api.urls'))

5. Run `python manage.py migrate` to create the authorize models.

6. Start the development server and visit http://127.0.0.1:8000/auth/
   to view authorize index.

.. |travis| image:: https://travis-ci.org/hchockarprasad/django-authorize.svg?branch=master
    :target: https://travis-ci.org/hchockarprasad/django-authorize
.. |codacy| image:: https://api.codacy.com/project/badge/Grade/094403a27f8843f388824c2d2ab1e3b1
   :alt: Codacy Badge
   :target: https://www.codacy.com/app/hchockarprasad/django-authorize?utm_source=github.com&utm_medium=referral&utm_content=hchockarprasad/django-authorize&utm_campaign=badger
.. |pypipackage| image:: https://img.shields.io/pypi/v/django-authorize.svg
.. |coverage| image:: https://img.shields.io/codecov/c/github/hchockarprasad/django-authorize/master.svg
   :target: https://codecov.io/gh/hchockarprasad/django-authorize
