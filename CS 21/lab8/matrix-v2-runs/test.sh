#!/bin/bash

OUTPUT="/home/cs21FWX1/Desktop/lab8/part2/matrix-v2-runs"

for i in {001..100};
    do perf stat -o "${OUTPUT}/matrix-v2.${i}.txt" -B \
    -e all_data_cache_accesses\
    -e l2_cache_accesses_from_dc_misses\
    -e l2_cache_hits_from_dc_misses\
    -e l2_cache_misses_from_dc_misses\
    -e cycles,instructions\
    ./matrix-v2
done