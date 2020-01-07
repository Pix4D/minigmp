cmake_minimum_required(VERSION 3.12)
project(minigmp)

include(GenerateExportHeader)

add_library(minigmp SHARED
    mini-gmp.h
    mini-gmp.c
)
generate_export_header(minigmp)
target_include_directories(minigmp 
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_BINARY_DIR}>
        $<INSTALL_INTERFACE:include>
)

install(TARGETS minigmp EXPORT minigmpTargets
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
)
install(
    FILES mini-gmp.h ${CMAKE_CURRENT_BINARY_DIR}/minigmp_export.h
    DESTINATION include/
)
# Package configuration
set(configPackageLocation ${CMAKE_INSTALL_LIBDIR}/cmake/minigmp)
set(inputConfigFile "${CMAKE_CURRENT_SOURCE_DIR}/minigmpConfig.cmake")
set(outputConfigFile "${CMAKE_CURRENT_BINARY_DIR}/minigmpConfig.cmake")
configure_file(${inputConfigFile} ${outputConfigFile} @ONLY)
install(FILES ${outputConfigFile}
        DESTINATION ${configPackageLocation}
)
export(EXPORT minigmpTargets
    FILE "${CMAKE_CURRENT_BINARY_DIR}/minigmpTargets.cmake"
    NAMESPACE minigmp::
)
install(EXPORT minigmpTargets
    NAMESPACE minigmp::
    DESTINATION ${configPackageLocation}
)
