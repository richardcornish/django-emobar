from distutils.core import setup
import os


setup(name='django-emo',
      version='1.0',
      description='A utility to enhance the Django admin',
      author='Richard Cornish',
      author_email='rich@richardcornish.com',
      url='hhttps://github.com/richardcornish/django-emo',
      download_url='https://github.com/richardcornish/django-emo/archive/master.zip', 
      packages=['emo'],
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.3',
                   'Topic :: Utilities'],
      )
