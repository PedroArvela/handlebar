from setuptools import setup, find_packages

setup(
    name="handlebar.py",
    version="0.1",

    author="José Pedro Arvela",
    author_email="jparvela@gmail.com",
    description="Debian build system with copy-on-write containers",
    license="MIT",

    packages=find_packages(),
    scripts=['handlebar'], requires=['toml.py']
)
