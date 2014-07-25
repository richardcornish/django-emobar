from distutils.core import setup


setup(name='django-emo',
      version='0.1',
      description='Emo is a Django app that enhances the admin with a markdown and emoji WYSIWYG for textareas.',
      author='Richard Cornish',
      author_email='rich@richardcornish.com',
      url='https://github.com/richardcornish/django-emo',
      packages=[
            'emo'
      ],
      classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Framework :: Django',
            'Topic :: Utilities'
      ],
      install_requires=[
            'django'
      ],
)
