#!/bin/bash
make
make clean
clear
texcount -merge -sum main.tex | grep "Words in text"
