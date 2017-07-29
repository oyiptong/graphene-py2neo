from setuptools import setup, find_packages

setup(
    name="graphene-py2neo",
    url="https://github.com/oyiptong/graphene-py2neo",
    version="1.0.0",
    description="Graphene Py2Neo Integration",
    author="Olivier Yiptong",
    author_email="olivier@olivieryiptong.com",
    packages=find_packages(exclude=['tests']),
    license='Apache License, Version 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=[
        'six==1.10.0',
        'graphene==1.4.1',
        'py2neo==3.1.2',
        'singledispatch==3.4.0.3',
    ],
    tests_require=[
        'nose==1.3.7',
        'mock==2.0.0'
    ],
)
