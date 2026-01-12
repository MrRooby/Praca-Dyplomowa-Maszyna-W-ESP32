#!/bin/bash
start=$(date +%s.%N)

make
make clean
clear
texcount -merge -sum main.tex | grep "Words in text"

end=$(date +%s.%N)
runtime=$(echo "scale=3; ($end - $start) / 1" | bc)
echo -e "_________________________\n"
echo "Compilation time: $runtime s"
