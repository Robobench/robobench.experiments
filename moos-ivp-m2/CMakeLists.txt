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

SET(DATA_DIR "${PREFIX}/etc/robobench-experiments/moos-ivp-m2-berta/")

### Glob, then install the files ###
INSTALL(FILES "${CMAKE_CURRENT_SOURCE_DIR}/moos-ivp-m2-berta.ini" DESTINATION ${DATA_DIR})



