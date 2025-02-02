#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "bubbles.h"

// Define the structure to maintain the state
struct bubbles {
    struct node* head; // doubly linked list to store bubbles
    int count;         // total number of bubbles
    int moved;         // number of bubbles that moved
};

// Node structure for the doubly linked list
typedef struct node {
    int x;         // position of the bubble
    int distance;  // total distance moved by the bubble
    struct node* prev;
    struct node* next;
} node;

// Initialize the bubbles structure
struct bubbles* init() {
    struct bubbles* b = (struct bubbles*) malloc(sizeof(struct bubbles));
    b->head = NULL;
    b->count = 0;
    b->moved = 0;
    return b;
}

// Helper function to insert a new node at the correct position in the linked list
node* insert_node(struct bubbles* b, int x) {
    node* new_node = (node*) malloc(sizeof(node));
    new_node->x = x;
    new_node->distance = 0;

    if (b->head == NULL || b->head->x > x) {
        new_node->next = b->head;
        if (b->head) b->head->prev = new_node;
        b->head = new_node;
    } else {
        node* current = b->head;
        while (current->next && current->next->x < x) {
            current = current->next;
        }
        new_node->next = current->next;
        new_node->prev = current;
        if (current->next) current->next->prev = new_node;
        current->next = new_node;
    }
    return new_node;
}

// Helper function to remove a node from the linked list
void remove_node(struct bubbles* b, node* n) {
    if (n->prev) n->prev->next = n->next;
    else b->head = n->next;
    if (n->next) n->next->prev = n->prev;
    free(n);
    b->count--;
}

// Helper function to move bubbles apart
void move_bubbles_apart(struct bubbles* b, node* n) {
    int moved = 0;
    node* current = n->next;
    while (current && current->x - n->x < 2) {
        int delta = 2 - (current->x - n->x);
        current->x += delta;
        current->distance += delta;
        if (current->distance >= 8) {
            remove_node(b, current);
            moved++;
        } else {
            current = current->next;
        }
    }
    current = n->prev;
    while (current && n->x - current->x < 2) {
        int delta = 2 - (n->x - current->x);
        current->x -= delta;
        current->distance += delta;
        if (current->distance >= 8) {
            remove_node(b, current);
            moved++;
        } else {
            current = current->prev;
        }
    }
    b->moved += moved;
}

int bubble(struct bubbles* b, int x_i) {
    node* existing = b->head;
    while (existing && existing->x == x_i) {
        remove_node(b, existing);
        existing = b->head;
    }
    if (!existing || existing->x != x_i) {
        node* new_node = insert_node(b, x_i);
        b->count++;
        move_bubbles_apart(b, new_node);
    }
    int ret = b->count;
    b->moved = 0; // reset moved count for next call
    return ret;
}

#define VERIFY(b) do {\
    fprintf(stderr, "verifying: " #b "\n");\
    bool _b = (b);\
    if (!_b) {\
        fprintf(stderr, "verification failed!\n");\
        exit(1);\
    }\
} while (0)

int main() {
    struct bubbles *b1 = init();
    struct bubbles *b2 = init();

    VERIFY(bubble(b1, 1) == 1);
    VERIFY(bubble(b1, 13) == 2);
    VERIFY(bubble(b1, 7) == 3);
    VERIFY(bubble(b1, 9) == 4);
    VERIFY(bubble(b1, 13) == 4);
    VERIFY(bubble(b2, -1) == 1);
    VERIFY(bubble(b2, 1) == 2);
    VERIFY(bubble(b2, 0) == 2);
    VERIFY(bubble(b2, -1) == 2);
    VERIFY(bubble(b2, 0) == 3);
    VERIFY(bubble(b2, -1) == 3);
    VERIFY(bubble(b2, 0) == 3);
    VERIFY(bubble(b2, -1) == 3);
    VERIFY(bubble(b1, 4) == 4);
    VERIFY(bubble(b1, 8) == 5);
    VERIFY(bubble(b1, 1) == 5);
    VERIFY(bubble(b1, 5) == 5);

    // TODO add more tests
    printf("All tests passed!\n");
    return 0;
}