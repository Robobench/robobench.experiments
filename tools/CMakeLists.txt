### Maintainer: jon.weisz[@gmail.comB] ###

cmake_minimum_required(VERSION 2.8)
PROJECT(robobench-experiments-tools)
SET(CMAKE_BUILD_TYPE distribution)

MESSAGE("-- You are building on: ${CMAKE_SYSTEM_NAME}")
MESSAGE("-- If you don't set -DCMAKE_INSTALL_PREFIX defaults are used.")

SET(PREFIX "/usr/local")
IF (CMAKE_INSTALL_PREFIX)
    SET(PREFIX ${CMAKE_INSTALL_PREFIX})
    MESSAGE("-- Found install PREFIX: " ${PREFIX})
ENDIF()

### Glob, then install the files ###
INSTALL(PROGRAMS "${CMAKE_CURRENT_SOURCE_DIR}/kill_operf.bash"      DESTINATION ${PREFIX}/bin/)
INSTALL(PROGRAMS "${CMAKE_CURRENT_SOURCE_DIR}/send_goal"      DESTINATION ${PREFIX}/bin/)
