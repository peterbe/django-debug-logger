from setuptools import setup, find_packages

setup(
    name='django-debugger',
    version=__import__('debugger').__version__,
    description='A configurable set of plugins that log various debug information about the current request/response to the database.',
    long_description=open('README.rst').read(),
    # Get more strings from http://www.python.org/pypi?:action=list_classifiers
    author='Rob Hudson',
    author_email='rob@cogit8.org',
    url='http://github.com/robhudson/django-debugger/',
    download_url='http://github.com/robhudson/django-debugger/downloads',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False, # because we're including media that Django needs
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
