### Maintainer: flier[@techfak.uni-bielefeld.de] ###

cmake_minimum_required(VERSION 2.8)
PROJECT(robobench-experiments-tum-simulation)
SET(CMAKE_BUILD_TYPE distribution)

MESSAGE("-- You are building on: ${CMAKE_SYSTEM_NAME}")
MESSAGE("-- If you don't set -DCMAKE_INSTALL_PREFIX defaults are used.")

SET(PREFIX "/usr/local")
IF (CMAKE_INSTALL_PREFIX)
    SET(PREFIX ${CMAKE_INSTALL_PREFIX})
    MESSAGE("-- Found install PREFIX: " ${PREFIX})
ENDIF()

SET(DATA_DIR "${PREFIX}/etc/robobench-experiments/tum-simulation/")

### Glob, then install the files ###
INSTALL(DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/data/"  DESTINATION ${DATA_DIR})
INSTALL(PROGRAMS "${CMAKE_CURRENT_SOURCE_DIR}/scripts/send_flight_plan"  DESTINATION ${PREFIX}/bin )
INSTALL(FILES "${CMAKE_CURRENT_SOURCE_DIR}/tum-ardrone-profile.ini" DESTINATION ${DATA_DIR})



