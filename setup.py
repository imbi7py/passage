from setuptools import setup

__author__ = 'Mark Williams'
__version__ = '0.0.1'
__author_email__ = 'markrwilliams@gmail.com'
__url__ = 'https://github.com/markrwilliams/sendfileobj'
__license__ = 'BSD'

__description__ = 'Send file objects between Python processes on Linux'


if __name__ == '__main__':
    setup(name='passage',
          version=__version__,
          description=__description__,
          author=__author__,
          author_email=__author_email__,
          package=['passage'],
          license=__license__,
          platforms='linux') # ??
