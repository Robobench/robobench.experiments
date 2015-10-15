### Maintainer: jweisz[@cs.columbia.edu] ###

cmake_minimum_required(VERSION 2.8)
PROJECT(robobench-experiments-moos-ivp-m2)
SET(CMAKE_BUILD_TYPE distribution)

MESSAGE("-- You are building on: ${CMAKE_SYSTEM_NAME}")
MESSAGE("-- If you don't set -DCMAKE_INSTALL_PREFIX defaults are used.")

SET(PREFIX "/usr/local")
IF (CMAKE_INSTALL_PREFIX)
    SET(PREFIX ${CMAKE_INSTALL_PREFIX})
    MESSAGE("-- Found install PREFIX: " ${PREFIX})
ENDIF()

SET(DATA_DIR "${PREFIX}/etc/robobench-experiments/moos-ivp-m2-berta")

### Glob, then install the files ###
FILE(GLOB macro_files "${CMAKE_CURRENT_SOURCE_DIR}/missions/m2_berta/*.moos" "${CMAKE_CURRENT_SOURCE_DIR}/missions/*.bhv")
FILE(GLOB script_files "${CMAKE_CURRENT_SOURCE_DIR}/missions/m2_berta/*.sh")


INSTALL(FILES "${CMAKE_CURRENT_SOURCE_DIR}/moos-ivp-m2-berta.ini" DESTINATION ${DATA_DIR})
INSTALL(FILES ${macro_files} DESTINATION ${DATA_DIR}/missions/m2_berta/)
INSTALL(PROGRAMS ${script_files} DESTINATION ${DATA_DIR}/missions/m2_berta/)



