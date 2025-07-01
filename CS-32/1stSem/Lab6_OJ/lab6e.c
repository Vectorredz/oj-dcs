#include <stdio.h>
#include <stdlib.h>
#include "podium_heap.h"
#include <assert.h>

//--------DYNAMIC ARRAYS-------------------------------------//

// dynamic_array *da_init(void);
// void da_set(dynamic_array *a, idx_t i, int64_t val);
// int64_t da_get(dynamic_array *a, idx_t i);
// void da_push(dynamic_array *a, int64_t val);
// int64_t da_pop(dynamic_array *a);
// int32_t da_size(dynamic_array *a);
// bool da_empty(dynamic_array *a);  



podium_heap *ph_init() {
    podium_heap *h = (podium_heap*)malloc(sizeof(podium_heap));
    h->vals = da_init();
    h->size = 0;
    assert(ph_empty(h));
    return h;
}

int64_t ph_peek_max(podium_heap *h) {
    assert(!ph_empty(h));
    return da_get(h->vals, 0);
}

bool ph_empty(podium_heap *h) {
    return ph_size(h) == 0;
}

void ph_push(podium_heap *h, int64_t value);
int64_t ph_peek_max(podium_heap *h);
int64_t ph_pop_max(podium_heap *h);
int64_t ph_peek_2nd_max(podium_heap *h);
int64_t ph_pop_2nd_max(podium_heap *h);
int64_t ph_peek_3rd_max(podium_heap *h);
int64_t ph_pop_3rd_max(podium_heap *h);
int32_t ph_size(podium_heap *h);

int main(){
    podium_heap *heap = ph_init();
    
}