# 📦 cURL Conan Package

This Conan package builds and packages the cURL library, with an option for enabling WebSocket support. This custom version of cURL is provided because the one in the central repository does not yet support setting `ENABLE_WEBSOCKETS`. If WebSocket support is not required, the official version can be used instead.

## Requirements

- Conan
- CMake
- A C++ compiler

## 🚀 Usage

Add this package to your project's `conanfile.txt`:

```ini
[requires]
libcurl/8.7.0@svnscha/dev

[generators]
cmake
```

To install dependencies, run:

```sh
conan install .
```

To build your project with Conan, run:

```sh
mkdir build && cd build
conan build ..
```

## 🧪 Building the Package

To create the Conan package, navigate to the directory containing conanfile.py and run:

```sh
conan create --user svnscha --channel dev -s build_type=Debug .
conan create --user svnscha --channel dev -s build_type=Release .
```

For local development you could simply use

```sh
conan create .
```
