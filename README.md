handlebar
=========

Build Debian packages from source easily using [fpm](https://github.com/jordansissel/fpm).

This project is a proof-of-concept which needs to be refactored.

This is a program which reads a `.toml` file. With the info in this file the program can either launch a container in a copy-on-write mount to compile the source code or grab the compiled code and create a package out of it.
