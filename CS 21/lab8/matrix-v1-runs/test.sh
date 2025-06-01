#!/bin/bash

OUTPUT="/home/cs21FWX1/Desktop/lab8/part2/matrix-v1-runs"

for i in {001..100};
    do perf stat -o "${OUTPUT}/matrix-v1.${i}c" -B -e all_data_cache_accesses,l2_cache_accesses_from_dc_misses,l2_cache_hits_from_dc_misses,l2_cache_misses_from_dc_misses,cycles,instructions ./matrix-v1
done