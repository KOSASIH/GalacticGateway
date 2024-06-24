cmake_minimum_required(VERSION 3.10)

# Project Information
project(GalacticGateway VERSION 1.0.0 LANGUAGES CXX)

# Set Compiler Flags
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Define Project Structure
set(PROJECT_SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR})
set(PROJECT_BINARY_DIR ${CMAKE_CURRENT_BINARY_DIR})

# Add Subdirectories
add_subdirectory(core)
add_subdirectory(ai)
add_subdirectory(web)
add_subdirectory(tests)

# Core Library
add_library(galactic_gateway_core
  ${PROJECT_SOURCE_DIR}/core/entanglement_auth.cpp
  ${PROJECT_SOURCE_DIR}/core/yolov4_object_detection.cpp
  ${PROJECT_SOURCE_DIR}/core/agi_chatbot.cpp
)

target_link_libraries(galactic_gateway_core
  ${CMAKE_THREAD_LIBS_INIT}
  ${OpenCV_LIBS}
  ${DL_LIBS}
)

# AI Library
add_library(galactic_gateway_ai
  ${PROJECT_SOURCE_DIR}/ai/neural_network.cpp
  ${PROJECT_SOURCE_DIR}/ai/deep_learning.cpp
)

target_link_libraries(galactic_gateway_ai
  ${galactic_gateway_core}
  ${TensorFlow_LIBS}
  ${PyTorch_LIBS}
)

# Web Application
add_executable(galactic_gateway_web
  ${PROJECT_SOURCE_DIR}/web/main.cpp
)

target_link_libraries(galactic_gateway_web
  ${galactic_gateway_core}
  ${galactic_gateway_ai}
  ${Boost_LIBS}
  ${Qt_LIBS}
)

# Tests
add_executable(galactic_gateway_tests
  ${PROJECT_SOURCE_DIR}/tests/tests.cpp
)

target_link_libraries(galactic_gateway_tests
  ${galactic_gateway_core}
  ${galactic_gateway_ai}
  ${GTest_LIBS}
)

# Install Targets
install(TARGETS galactic_gateway_core galactic_gateway_ai galactic_gateway_web
  LIBRARY DESTINATION lib
  ARCHIVE DESTINATION lib
  RUNTIME DESTINATION bin
)

# Package Configuration
include(CPack)

set(CPACK_PACKAGE_NAME "GalacticGateway")
set(CPACK_PACKAGE_VERSION "1.0.0")
set(CPACK_PACKAGE_DESCRIPTION "Galactic Gateway Project")
set(CPACK_PACKAGE_VENDOR "Galactic Gateway Team")

set(CPACK_GENERATOR "TGZ;ZIP")

include(CPackConfig.cmake)
