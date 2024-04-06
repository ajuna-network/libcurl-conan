from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, cmake_layout
from conan.tools.scm import Git

#
# The existence of this recipe is due to the official one lacking support for ENABLE_WEBSOCKETS. You can find the official recipe at the provided GitHub link.
# https://github.com/conan-io/conan-center-index/blob/master/recipes/libcurl/all/conanfile.py
#
class LibcurlConan(ConanFile):
    name = "libcurl"
    description = "command line tool and library for transferring data with URLs"
    license = "curl"
    version = "8.7.0"
    package_type = "library"
    url = "https://github.com/svnscha/libcurl-conan"
    description = "command line tool and library for transferring data with URLs"
    topics = ("conan", "curl", "http", "https", "websocket")
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "ENABLE_WEBSOCKETS": [True, False],
        "BUILD_TESTING": [True, False],
        "USE_ZLIB": [True, False],
        "USE_LIBSSH2": [True, False],
        "BUILD_LIBCURL_DOCS": [True, False],
        "BUILD_CURL_EXE": [True, False],
        "HTTP_ONLY": [True, False],
        "CURL_USE_SCHANNEL": [True, False],
    }
    default_options = {
        "shared": False,
        "ENABLE_WEBSOCKETS": True,
        "BUILD_TESTING": False,
        "USE_ZLIB": False,
        "USE_LIBSSH2": False,
        "BUILD_LIBCURL_DOCS": False,
        "BUILD_CURL_EXE": False,
        "HTTP_ONLY": True,
        "CURL_USE_SCHANNEL": True,
    }
    generators = "CMakeDeps"

    def source(self):
        git = Git(self)
        git.clone(url="https://github.com/curl/curl.git", target=".")
        git.checkout("curl-%s" % self.version.replace(".", "_"))

    def generate(self):
        tc = CMakeToolchain(self)
        if self.options.shared:
            tc.variables["BUILD_SHARED_LIBS"] = "ON"
        else:
            tc.variables["BUILD_SHARED_LIBS"] = "OFF"

        if self.options.BUILD_TESTING:
            tc.variables["BUILD_TESTING"] = "ON"
        else:
            tc.variables["BUILD_TESTING"] = "OFF"

        if self.options.USE_ZLIB:
            tc.variables["USE_ZLIB"] = "ON"
        else:
            tc.variables["USE_ZLIB"] = "OFF"

        if self.options.USE_LIBSSH2:
            tc.variables["USE_LIBSSH2"] = "ON"
        else:
            tc.variables["USE_LIBSSH2"] = "OFF"

        if self.options.BUILD_LIBCURL_DOCS:
            tc.variables["BUILD_LIBCURL_DOCS"] = "ON"
        else:
            tc.variables["BUILD_LIBCURL_DOCS"] = "OFF"

        if self.options.BUILD_CURL_EXE:
            tc.variables["BUILD_CURL_EXE"] = "ON"
        else:
            tc.variables["BUILD_CURL_EXE"] = "OFF"

        if self.options.HTTP_ONLY:
            tc.variables["HTTP_ONLY"] = "ON"
        else:
            tc.variables["HTTP_ONLY"] = "OFF"

        if self.options.CURL_USE_SCHANNEL and self.settings.os == "Windows":
            tc.variables["CURL_USE_SCHANNEL"] = "ON"
        else:
            tc.variables["CURL_USE_SCHANNEL"] = "OFF"

        if self.options.ENABLE_WEBSOCKETS:
            tc.variables["ENABLE_WEBSOCKETS"] = "ON"
        else:
            tc.variables["ENABLE_WEBSOCKETS"] = "OFF"
        tc.generate()

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        if self.settings.build_type == "Debug":
            self.cpp_info.libs = ["libcurl-d"]
        else:
            self.cpp_info.libs = ["libcurl"]

        if not self.options.shared:
            self.cpp_info.defines.append("CURL_STATICLIB=1")

        if self.settings.os == "Windows":
            self.cpp_info.system_libs = ["ws2_32"]
            if self.options.CURL_USE_SCHANNEL:
                self.cpp_info.system_libs.append("crypt32")
