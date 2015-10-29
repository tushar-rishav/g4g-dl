try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sys

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True
setup(name='g4g-dl',
      version='0.0.1',
      install_requires=[
          r for r in open('requirements.txt', 'r').read().split('\n') if r],
      author='Tushar Gautam',
      author_email='tushar.rishav@gmail.com',
      packages=['G4Gdl', ],
      entry_points={
          'console_scripts': ['g4g-dl=G4Gdl:main'],
      },
      license='GNU General Public License v3 (GPLv3)',
      url='https://github.com/tushar-rishav/g4g-dl/',
      description="Downloads all Data Structures and Algorithms tutorials from Geeks for Geeks and save as PDF",
      long_description=open('README.rst').read(),
      keywords=['pdf', 'algorithms','data structures', 'Geeks for Geeks', 'python', 'scrapping'],
      classifiers=[
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Topic :: System :: Monitoring'
      ],
      )