from setuptools import find_packages, setup

setup(
    name="sqroot",
    packages=find_packages(
        where="src",
    ),
    package_dir={"": "src"},
    version="1.0.0",
    description="A simple test python library",
    author="Me",
    license="MIT",
    install_requires=[],#other dependencies for library to be installed
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='',

)
