#ifndef PODIUM_HEAP_H
#define PODIUM_HEAP_H

#include <stdbool.h>
#include <stdint.h>

typedef struct dynamic_array dynamic_array;

typedef int32_t idx_t;

dynamic_array *da_init(void);
void da_set(dynamic_array *a, idx_t i, int64_t val);
int64_t da_get(dynamic_array *a, idx_t i);
void da_push(dynamic_array *a, int64_t val);
int64_t da_pop(dynamic_array *a);
int32_t da_size(dynamic_array *a);
bool da_empty(dynamic_array *a);  // return whether the array is empty or not


typedef struct podium_heap {
    dynamic_array *vals;
    int32_t size;
} podium_heap;

podium_heap *ph_init(void);
void ph_push(podium_heap *h, int64_t value);
int64_t ph_peek_max(podium_heap *h);
int64_t ph_pop_max(podium_heap *h);
int64_t ph_peek_2nd_max(podium_heap *h);
int64_t ph_pop_2nd_max(podium_heap *h);
int64_t ph_peek_3rd_max(podium_heap *h);
int64_t ph_pop_3rd_max(podium_heap *h);
int32_t ph_size(podium_heap *h);
bool ph_empty(podium_heap *h);  // return whether the heap is empty or not

#endif
