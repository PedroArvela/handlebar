handlebar
=========

### This project is unmaintained

## Description

Debian build system using containers and copy on write. Compiled executables
are then packaged using [fpm](https://github.com/jordansissel/fpm).

This project is a proof-of-concept which needs to be refactored.

This is a program which reads a `.toml` file. With the info in this file the
program can either launch a container in a copy-on-write mount to compile the
source code or grab the compiled code and create a package out of it.

## Instalation

For the moment, python 3.4, systemd-nspawn, aufs and fpm are required. After
these dependencies are met, handlebar can be installed with the command:

```
pip install git+https://github.com/jparvela/handlebar.git
```
