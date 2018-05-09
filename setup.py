from setuptools import setup, find_packages
import os

version = '1.3.2'

setup(name='collective.blogging',
      version=version,
      description="A blogging extension for Plone 4.x.",
      long_description=open(os.path.join("README.rst")).read() + "\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from https://pypi.org/pypi?:action=list_classifiers
      classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='web plone blogging system extension cms',
      author='Lukas Zdych',
      author_email='lukas.zdych@gmail.com',
      url='https://github.com/collective/collective.blogging',
      license='GPL',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      extras_require = {
          'test': [
              'plone.app.testing',
          ],
      },
      install_requires=[
          'setuptools',
          'z3c.autoinclude',  # Required for Plone 3.2 compatibility
          'archetypes.schemaextender',
          'archetypes.markerfield',
          'plone.indexer',
          'plone.app.jquerytools',
          'Products.ATReferenceBrowserWidget',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
