import io
import os
from setuptools import setup, find_packages

version = __import__('django_choices_enum').__version__

setup(
    name='django-choices-enum',
    version=version,

    description='make enum34 package play well with django choices',
    long_description=io.open('README.rst', encoding='utf-8').read(),
    author='Tommy Wang',
    author_email='twang@joinem.com',
    url='http://github.com/tcwang817/django-choices-enum',
    download_url='https://github.com/tcwang817/django-choices-enum/tarball/{version}'.format(version=version),

    packages=find_packages(),
    install_requires=['enum34 >= 1.0.4'],
    test_require=[],
    test_suite='tests',
    include_package_data=True,

    license='MIT',
    platforms=['any'],
    keywords='django choices enum',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Web Environment',
        'Topic :: Internet',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Framework :: Django',
    ],
)
