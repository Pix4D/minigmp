from conans import ConanFile, CMake, tools
import os


class MiniGMPConan(ConanFile):
    name = 'minigmp'
    lib_version = '6.1.2'
    revision = '0'
    version = '{}-{}'.format(lib_version, revision)
    settings = 'os', 'compiler', 'build_type', 'arch'
    description = 'A small implementation of a subset of GMP\'s mpn and mpz interfaces'
    license = 'GNU LESSER GENERAL PUBLIC LICENSE Version 3'
    url = 'https://gmplib.org/'
    generators = 'cmake'
    exports_sources = ('mini-gmp.c', 'mini-gmp.h', 'CMakeLists.txt', 'minigmpConfig.cmake')

    def build(self):
        cmake = CMake(self, parallel=True)

        if(tools.cross_building(self.settings) and
           str(self.settings.os).lower() == 'android'):
            # this is a workaround for the lack of proper Android support from Conan
            # see https://github.com/conan-io/conan/issues/2856#issuecomment-421036768
            cmake.definitions["CONAN_LIBCXX"] = ""

        cmake.configure()
        cmake.build(target='install')

    def package_info(self):
        self.cpp_info.includedirs = ['include']  # Ordered list of include paths
        self.cpp_info.libs = ['minigmp']  # The libs to link against
        self.cpp_info.libdirs = ['lib']  # Directories where libraries can be found
