cmake_minimum_required(VERSION 3.12)
project(MiniGMPQRCodeTest)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)

conan_basic_setup(KEEP_RPATHS)

find_package(minigmp REQUIRED QUIET)

add_executable(testApp main.cpp)

target_link_libraries(testApp
    PRIVATE
       minigmp::minigmp
)
