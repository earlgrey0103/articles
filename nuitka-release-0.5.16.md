# Python替代编译器Nuika发布0.5.16稳定版

11月11日，Nuitka开发团队通过博客，发布了最新的稳定版本。

据介绍，这次主要是维护版本发布，主要是改进对新平台的支持，并进行部分修正。该版本会提升独立模式下的运行速度，以及部分使用场景下的编译效率。

## Bug修复

- Python: Fix, the gi_running attribute of generators is no longer an int, but bool instead.

- Python3: Fix, the int built-in with two arguments, value and base, raised UnicodeDecodeError instead of ValueError for illegal bytes given as value.

- Python3: Using tokenize.open to read source code, instead of reading manually and decoding from tokenize.detect_encoding, this handles corner cases more compatible.

- Fix, the PyLint warnings plug-in could crash in some cases, make sure it's more robust.

- Windows: Fix, the combination of AnaConda Python, MinGW 64 bits and mere acceleration was not working. Issue#254.

- Standalone: Preserve not only namespace packages created by .pth files, but also make the imports done by them. This makes it more compatible with uses of it in Fedora 22.

- Standalone: The extension modules could be duplicated, turned this into an error and cache finding them during compile time and during early import resolution to avoid duplication.

- Standalone: Handle "not found" from ldd output, on some systems not all the libraries wanted are accessible for every library.

- Python3.5: Fixed support for namespace packages, these were not yet working for that version yet.

- Python3.5: Fixes lack of support for unpacking in normal tuple, list, and set creations.

更多Bug修复信息和此次更新的其他情况，请查看[官方网站](http://nuitka.net/)。


## 什么是Nuitka？
Nuitka 是一个Python的替代品，支持 CPython 提供的代码，可翻译 Python 代码到 C++ 程序，并使用 libpython 来执行这些代码，就像 CPython 一样。兼容 Python 2.6, 2.7, 3.2, 3.3 ，3.4和3.5。一些团队正用它做完全的Python编译工具，并尝试将Python代码转译为其它可高速运行的编程语言。

从反馈情况来看，Nuitka编译后的Python程序虽然可移植性降低，但是同时也减少了一些开销，对提升Python程序的效率有一定效果。