#ifndef PANOPTICON_H
#define PANOPTICON_H

#include <assert.h>
#include <inttypes.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

// it should be a char (kasi name)
// typedef struct two_names {
//     const char *nearest;
//     const char *snd_nearest;
// } two_names;

// for testing purposes
typedef struct two_names {
    int64_t *nearest;
    int64_t *snd_nearest;
} two_names;

// provided by the judge
// int64_t oj_rand(void);

typedef struct tower_spy {
    int64_t f;
    char* name;
    struct tower_spy *l, *r;
    int64_t p;
} tower_spy;

int64_t rand_prio() {
    int64_t res = 0;
    for (int i = 0; i < 4; i++) {
        res = (res << 16) ^ rand();
    }
    return res;
}

tower_spy *t_init(int64_t n) {
    tower_spy* t = (tower_spy* )malloc(n * sizeof(tower_spy));
    t->p = rand_prio();
    // switch when submitting
    // t->p = oj_rand()
    t->f = -1;
    t->l = NULL;
    t->r = NULL;
    return t;
};

tower_spy *t_make(int64_t f, tower_spy *l, tower_spy *r) {
    tower_spy *t = (tower_spy*)malloc(sizeof(tower_spy));
    t->f = f;
    t->l = l;
    t->r = r;
    t->p = rand_prio();
    return t;
}

tower_spy *t_merge(tower_spy *l, tower_spy *r){
    if (l == NULL) {
        return r;
    }
    if (r == NULL) {
        return l;
    }
    assert(l->f < r->f);
    if (l->p >= r->p) {
        l->r = t_merge(l->r, r);
        return l;
    } else {
        r->l = t_merge(l, r->l);
        return r;
    }
}

void t_split(tower_spy *t, int64_t f, tower_spy **l, tower_spy **x, tower_spy **r){
    if (t == NULL) {
        *l = *x = *r = NULL;
    } else if (f < t->f) {
        *r = t;
        t_split(t->l, f, l, x, &(t->l));
    } else if (f > t->f) {
        *l = t;
        t_split(t->r, f, &(t->r), x, r);
    } else {
        assert(f == t->f);
        *l = t->l;
        *x = t;
        *r = t->r;
        t->l = t->r = NULL;
    }
}

tower_spy* t_add(tower_spy *t, const char *g, int64_t f){
    tower_spy *l, *x, *r;
    t_split(t, f, &l, &x, &r);
    assert(x == NULL);
    x = t_make(f, NULL, NULL);
    return t_merge(t_merge(l, x), r);
}


void purchase(tower_spy *t, const char *g, int64_t f) {
    t_add(t, g, f);
};


tower_spy *t_remove(tower_spy *t, int64_t f) {
    assert(t != NULL);
    tower_spy *l, *x, *r;
    t_split(t, f, &l, &x, &r);
    assert(x != NULL && f == x->f);
    free(x);
    return t_merge(l, r);
}

int64_t t_next_higher(tower_spy *t, int64_t f) {
    if (t == NULL) {
        return f;
    }

    if (f < t->f) {
        int64_t r = t_next_higher(t->l, f);
        assert(r >= f);
        return r > f ? r : t->f;
    } else {
        return t_next_higher(t->r, f);
    }
};

int64_t t_next_lower(tower_spy *t, int64_t f) {
    if (t == NULL) {
        return f;
    }

    if (f > t->f) {
        int64_t l = t_next_lower(t->r, f);
        assert(l <= f);
        return l < f ? l : t->f;
    } else {
        return t_next_lower(t->l, f);
    }
};

int64_t closest(tower_spy *t, int64_t f){
    int64_t higher = t_next_higher(t, f);
    int64_t lower = t_next_lower(t, f);
    int64_t closestt;
    if (f - higher > f - lower){
        closestt = higher;
    } else {
        closestt = lower;
    }
    return closestt;
}

two_names two_nearest(tower_spy *t, int64_t f){
    two_names res;
    int64_t nearest_floor_1 = closest(t, f);
    // find a way to save the name
    if (nearest_floor_1 != NULL){
        t_remove(t, nearest_floor_1);
        int64_t nearest_floor_2 = closest(t, f);
        if (nearest_floor_2 != NULL){
            // to do
            res.nearest = nearest_floor_1;
            res.snd_nearest = nearest_floor_2;
            purchase(t, "test", nearest_floor_1);
        }
    }  
    return res;
};

int main() {
    tower_spy *spy_1 = t_init(90210);

    two_names res;
    // res = two_nearest(spy_1, 20);
    // assert(res.nearest == NULL);
    // assert(res.snd_nearest == NULL);

    purchase(spy_1, "Tom", 10);
    purchase(spy_1, "Ving", 20);

    // res = two_nearest(spy_1, 20);
    // assert(res.nearest == NULL);
    // assert(res.snd_nearest == NULL);

    purchase(spy_1, "Simon", 30);

    res = two_nearest(spy_1, 20);
    printf("sanity");
    printf("%ln", res.nearest);
    printf("%ln", res.snd_nearest);

    // res = two_nearest(spy_1, 30);
    // assert(strcmp(res.nearest, "Ving") == 0);
    // assert(strcmp(res.snd_nearest, "Tom") == 0);

    // purchase(spy_1, "Rebecca", 33);
    // purchase(spy_1, "Michelle", 10000); //its a very tall tower

    // res = two_nearest(spy_1, 30);
    // assert(strcmp(res.nearest, "Rebecca") == 0);
    // assert(strcmp(res.snd_nearest, "Ving") == 0);

    // res = two_nearest(spy_1, 10000);
    // assert(strcmp(res.nearest, "Rebecca") == 0);
    // assert(strcmp(res.snd_nearest, "Simon") == 0);
}

#endif


