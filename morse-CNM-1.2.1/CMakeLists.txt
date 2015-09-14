### Maintainer: flier[@techfak.uni-bielefeld.de] ###

cmake_minimum_required(VERSION 2.8)
PROJECT(robobench-experiments-morse-CNM-1.2.1-profile)
SET(CMAKE_BUILD_TYPE distribution)

MESSAGE("-- You are building on: ${CMAKE_SYSTEM_NAME}")
MESSAGE("-- If you don't set -DCMAKE_INSTALL_PREFIX defaults are used.")

SET(PREFIX "/usr/local")
IF (CMAKE_INSTALL_PREFIX)
    SET(PREFIX ${CMAKE_INSTALL_PREFIX})
    MESSAGE("-- Found install PREFIX: " ${PREFIX})
ENDIF()

### Glob, then install the files ###
INSTALL(PROGRAMS "${CMAKE_CURRENT_SOURCE_DIR}/tools/cat_script.py"      DESTINATION ${PREFIX}/bin/)
INSTALL(PROGRAMS "${CMAKE_CURRENT_SOURCE_DIR}/tools/mouse_script.py"    DESTINATION ${PREFIX}/bin/)
INSTALL(PROGRAMS "${CMAKE_CURRENT_SOURCE_DIR}/tools/cat_mouse_game.py"  DESTINATION ${PREFIX}/bin/)
INSTALL(PROGRAMS "${CMAKE_CURRENT_SOURCE_DIR}/tools/assess_cat_log.sh"  DESTINATION ${PREFIX}/bin/)
INSTALL(PROGRAMS "${CMAKE_CURRENT_SOURCE_DIR}/../operf_script.sh"    DESTINATION ${PREFIX}/bin/)
INSTALL(PROGRAMS "${CMAKE_CURRENT_SOURCE_DIR}/morse-profile-CNM-1.2.1.ini"      DESTINATION ${PREFIX}/etc/robobench-experiments/morse-CNM-1.2.1/)


