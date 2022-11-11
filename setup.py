import os
from setuptools import setup

def recursive(paths, rel='.'):
    l = []
    for path in paths:
        for x, y, z in os.walk(os.path.join(rel, path)):
            if z:
                l.append(os.path.relpath(os.path.join(x, '*'), rel))
    return l

setup(
    name='cyrildutrieux',
    version='0.0.1',
    description='My website',
    author='cdtx',
    classifiers=[
        'Programming Language :: Python :: 3.4',
    ],
    packages=['cdtx.cyrildutrieux'],
    package_data={'cdtx.cyrildutrieux': recursive(['templates', 'templatetags', 'static'], rel='cdtx/cyrildutrieux')},
    install_requires = []
)


