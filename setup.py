from setuptools import setup

setup(
    name='cyrildutrieux',
    version='0.0.1',
    description='My website',
    author='cdtx',
    classifiers=[
        'Programming Language :: Python :: 3.4',
    ],
    packages=['cdtx.cyrildutrieux'],
    package_data={'cdtx.cyrildutrieux': ['templates/*', 'static/*',]},
    install_requires = []
)


