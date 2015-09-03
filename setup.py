from setuptools import setup, find_packages

setup(name='projectname',
      version='0.1',
      description='Demo Modules',
      url='https://github.com/alexanderwaldin/projectname',
      author='The Author',
      author_email='theauthor@example.com',
      license='MIT',
      packages=['projectname', 'projectname.subpackageone'],
      # or packages=find_packages(exclude=["*.tests"])
      include_package_data=True,
      test_suite='nose.collector',
      tests_require=['nose'],
      install_requires=[])
