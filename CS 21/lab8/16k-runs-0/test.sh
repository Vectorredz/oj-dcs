#!/bin/bash

OUTPUT="/home/cs21FWX1/Desktop/lab8/part3/16k-runs-0"

for i in {001..100};
    do perf stat -o "${OUTPUT}/transpose-0.${i}" -B \
    -e all_data_cache_accesses\
    -e l2_cache_accesses_from_dc_misses\
    -e l2_cache_hits_from_dc_misses\
    -e l2_cache_misses_from_dc_misses\
    -e cycles,instructions\
    ./transpose 16k.ppm 0
done