from conans import ConanFile, CMake, tools
import os

class MiniGMPTestConan(ConanFile):
    settings = 'os', 'compiler', 'build_type', 'arch'
    generators = 'cmake'

    def imports(self):
        self.copy('*.dll', src='bin', dst='bin')

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        self.run(os.path.join(os.curdir, 'bin', 'testApp'))
