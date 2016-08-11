# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="mail_room",
    description="Mail Room Madness Assignment.",
    version=0.1,
    author="David Banks and Jeff Russel",
    author_email="crashtack@gmail.com, jefferyrayrussel@gmail.com",
    license='MIT',
    py_modules=['mail_room'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'tox']},
)
