### setup.py file 

from setuptools import setup
setup(
   name = 'hackathon',
   version = '1.0.11',
   author = 'aroun coumar',
   description = 'Fetches hackathons list',
   packages = ['hackathon'],
   install_requires = ['docopt','requests','pandas'],
   entry_points = {
      'console_scripts': [
         'hackathon=hackathon:main'
      ]
   }
)