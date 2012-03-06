from setuptools import setup

from httpclient import __version__

setup(
    name='httpclient',
    version=__version__,
    description='HTTP Client library for Python',
    long_description=open('README.rst').read(),
    author='Franck Cuny',
    author_email='franck.cuny@gmail.com',
    url='https://github.com/franckcuny/httpclient',
    packages=['httpclient'],
    license='MIT',
    tests_require=['coverage', 'nose', 'unittest2', 'pep8'],
    install_requires=['http==0.02', 'urllib3'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
    ]
)
