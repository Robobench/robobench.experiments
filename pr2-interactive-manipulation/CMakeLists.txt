### Maintainer: flier[@techfak.uni-bielefeld.de] ###

cmake_minimum_required(VERSION 2.8)
PROJECT(robobench-experiments-pr2-interactive-navigation)
SET(CMAKE_BUILD_TYPE distribution)

MESSAGE("-- You are building on: ${CMAKE_SYSTEM_NAME}")
MESSAGE("-- If you don't set -DCMAKE_INSTALL_PREFIX defaults are used.")

SET(PREFIX "/usr/local")
IF (CMAKE_INSTALL_PREFIX)
    SET(PREFIX ${CMAKE_INSTALL_PREFIX})
    MESSAGE("-- Found install PREFIX: " ${PREFIX})
ENDIF()

SET(DATA_DIR "${PREFIX}/etc/robobench-experiments/pr2-interactive-manipulation/")

### Glob, then install the files ###
INSTALL(DIRECTORIES "${CMAKE_CURRENT_SOURCE_DIR}/data/"  DESTINATION ${DATA_DIR})
INSTALL(FILES "${CMAKE_CURRENT_SOURCE_DIR}/pr2-interactive-navigation.ini"      DESTINATION ${DATA_DIR})


