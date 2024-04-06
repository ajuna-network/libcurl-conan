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
libcurl/8.6.0@svnscha/dev

[generators]
cmake
```

## 🧪 Export the Package

To export the Conan package, navigate to the directory containing conanfile.py and run:

```sh
conan export --user svnscha --channel dev --version 8.6.0 .
```

This exports the package to your local cache, usable by other projects.

## 🧪 Building the Package

For local development you could simply use

```sh
conan create --version 8.6.0 --build=missing .
```

or similar.
