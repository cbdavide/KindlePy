from setuptools import setup, find_packages
from os.path import abspath, dirname, join
from codecs import open

this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name = 'kindlepy',
    version = '1.0.0',
    description = 'CLI tool for mailing your documents to your kindle device.',
    long_description = long_description,
    url = 'https://github.com/cbdavide/KindlePy',
    author = 'David Castelblanco Benavides',
    author_email = 'cbdavides@gmail.com',
    license = 'GPLv3',
    keywords = 'email documents kindle send ebooks',
    packages = find_packages(),
    install_requires = ['docopt', 'validate_email'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Communications :: Email',
        'Topic :: Communications :: File Sharing'
    ],
    entry_points={
        'console_scripts': [
            'kindlepy=kindlepy.__main__:main',
        ],
    },
)
