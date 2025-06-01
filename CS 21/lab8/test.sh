#!/bin/bash

OUTPUT_DIR="/home/cs21FWX1/Desktop/lab8/part2/matrix-v2_runs"

for n in {001..100}; do
    echo "Running iteration $n..."
    perf stat -B \
        -e all_data_cache_accesses \
        -e l2_cache_accesses_from_dc_misses \
        -e l2_cache_hits_from_dc_misses \
        -e l2_cache_misses_from_dc_misses \
        -e cycles \
        -e instructions \
        ./matrix-v2 2> "${OUTPUT_DIR}/matrix-v2.${n}.txt"
done

echo "All 100 runs completed!"

perf stat -o output.txt -B -e cycles,instructions ./my_program arg1 arg2

#!/bin/bash

OUTPUT_DIR="/home/cs21FWX1/Desktop/lab8/part2/matrix-v1_runs"

for i in {001..100}; 
do 
    perf stat -o "${OUTPUT_DIR}/matrix-v1.${i}.txt" -B  \
    -e all_data_cache_accesses \
    -e l2_cache_accesses_from_dc_misses \
    -e l2_cache_hits_from_dc_misses \
    -e l2_cache_misses_from_dc_misses \
    -e cycles \
    -e instructions \
    ./matrix-v1
done