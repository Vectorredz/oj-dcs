#ifndef FRIENDS_H
#define FRIENDS_H

typedef struct friend_pair {
    int person1;
    int person2;
} friend_pair;

typedef struct friends {
    int count;
    friend_pair *pairs;
} friends;

friends *guess_friends(int n, int *f);

#endif
