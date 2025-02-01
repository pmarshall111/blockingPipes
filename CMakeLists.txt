cmake_minimum_required(VERSION 3.28)

project(pipes VERSION 1.0)

add_executable(pipes.tsk main.cpp)
target_compile_options(pipes.tsk PRIVATE -ggdb)
