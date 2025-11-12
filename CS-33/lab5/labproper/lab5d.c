#include "book_stack.h"
#include <stdlib.h>
#include <string.h> 
t_stack *t_deepcopy(const t_stack *orig);
typedef struct t_node t_node;
struct t_node *t_node_init(const char *t, int64_t q);
void update_node(t_node *node, const char *t, int64_t q);
char *strdup(const char *s);
t_node *better_prio_node(t_node *a, t_node *b);
typedef struct t_history_node { // idea here is to make a list of snapshots of stack states
    struct t_stack *snapshot;          // deep copy of stack state
    struct t_history_node *next;
} t_history_node;
typedef struct t_history {
    t_history_node *head;              // latest snapshot
    int versions;                      // index of versions
} t_history;
struct t_stack {
    struct t_node *top;
    t_history *hist;
    int size;   
};
struct t_node {
    char *title;
    int64_t quantity;
    struct t_node *next;
    int64_t priority;
};
t_stack *t_init(void) {
    t_stack *stack = malloc(sizeof(t_stack));
    stack->top = NULL;
    stack->size = 0;
    t_history *history = malloc(sizeof(t_history));
    history->head = NULL;
    history->versions = 0;
    stack->hist = history;
    // initial empty state snapshot for k=0
    t_stack *snapshot = t_deepcopy(stack);
    t_history_node *hnode = malloc(sizeof(t_history_node));
    hnode->snapshot = snapshot;
    hnode->next = history->head;
    history->head = hnode;
    history->versions++;
    return stack;
}
char *strdup(const char *s) {
    size_t len = strlen(s) + 1;
    char *dup = malloc(len);
    if (dup) { memcpy(dup, s, len); } 
    return dup;
}
t_node *t_node_init(const char *t, int64_t q) {
    t_node *node = (t_node *)malloc(sizeof(t_node));
    node->title = strdup(t);
    node->quantity = q;
    node->next = NULL;
    return node;
}
void t_push(t_stack *ts, const char *t, int64_t q) {
    t_node *newNode = t_node_init(t, q);
    if (ts->top == NULL) {
        newNode->priority = 1;
    } else {
        newNode->priority = ts->top->priority + 1;
        newNode->next = ts->top;
    }
    ts->top = newNode;
    ts->size++;
    // Save snapshot
    t_stack *snapshot = t_deepcopy(ts);
    t_history_node *hnode = malloc(sizeof(t_history_node));
    hnode->snapshot = snapshot;
    hnode->next = ts->hist->head;
    ts->hist->head = hnode;
    ts->hist->versions++;
}
char *t_pop(t_stack *ts) {
    if (ts->top == NULL) {
        return NULL;
    }
    t_node *temp = ts->top;
    char *poppedTitle = strdup(temp->title);
    ts->top = ts->top->next;
    ts->size--;
    t_stack *snapshot = t_deepcopy(ts);
    t_history_node *hnode = malloc(sizeof(t_history_node));
    hnode->snapshot = snapshot;
    hnode->next = ts->hist->head;
    ts->hist->head = hnode;
    ts->hist->versions++;
    return poppedTitle;
}
char *t_peek(t_stack *ts) {
    char *res = ts->top ? strdup(ts->top->title) : NULL;
    t_stack *snapshot = t_deepcopy(ts);
    t_history_node *hnode = malloc(sizeof(t_history_node));
    hnode->snapshot = snapshot;
    hnode->next = ts->hist->head;
    ts->hist->head = hnode;
    ts->hist->versions++;
    return res;
}
void update_node(t_node *node, const char *t, int64_t q) {
    free(node->title);
    node->title = strdup(t);
    node->quantity = q;
}
t_node *better_prio_node(t_node *a, t_node *b) {
    if (a->quantity > b->quantity) {
        return a;
    } else if (a->quantity < b->quantity) {
        return b;
    } else {
        return (a->priority > b->priority) ? a : b;
    }
}
void t_top_three(t_stack *ts, char *res1, char *res2, char *res3) {
    // idea here is two stacks sorting
    t_node *current = ts->top;
    t_node *max1 = t_node_init("", -1e9);
    t_node *max2 = t_node_init("", -1e9);
    t_node *max3 = t_node_init("", -1e9);
    while (current) {
        if (current->quantity >= max1->quantity) {
            if (better_prio_node(current, max1) == current) {
                update_node(max3, max2->title, max2->quantity);
                update_node(max2, max1->title, max1->quantity); 
                update_node(max1, current->title, current->quantity); 
            }
            else {
                update_node(max3, max2->title, max2->quantity);
                update_node(max2, current->title, current->quantity); 
            }
        }
        else if (current->quantity >= max2->quantity) {
            if (better_prio_node(current, max2) == current) {
                update_node(max3, max2->title, max2->quantity);
                update_node(max2, current->title, current->quantity); 
            }
            else {
                update_node(max3, current->title, current->quantity); 
            }
        }
        else if (current->quantity > max3->quantity) {
            update_node(max3, current->title, current->quantity); 
        }   
        
        current = current->next;
    }
    strcpy(res1, max1->title);  
    strcpy(res2, max2->title);
    strcpy(res3, max3->title);  
    // Save snapshot
    t_stack *snapshot = t_deepcopy(ts);
    t_history_node *hnode = malloc(sizeof(t_history_node));
    hnode->snapshot = snapshot;
    hnode->next = ts->hist->head;
    ts->hist->head = hnode;
    ts->hist->versions++;
}
t_stack *t_deepcopy(const t_stack *orig) {
    if (!orig) { return NULL; }
    t_stack *copy = malloc(sizeof(t_stack));
    copy->size = orig->size;
    copy->hist = NULL; 
    copy->top = NULL;
    if (!orig->top) { return copy; }
    // copy nodes in reverse order
    t_node *src = orig->top;
    t_node *rev = NULL;
    while (src) {
        t_node *tmp = malloc(sizeof(t_node));
        tmp->title = strdup(src->title);
        tmp->quantity = src->quantity;
        tmp->priority = src->priority;
        tmp->next = rev;
        rev = tmp;
        src = src->next;
    }
    // reverse again; so that it is in the original stack order topmost -> bottomost
    t_node *dst_prev = NULL, *dst_curr = rev;
    while (dst_curr) {
        t_node *next = dst_curr->next;
        dst_curr->next = dst_prev;
        dst_prev = dst_curr;
        dst_curr = next;
    }
    copy->top = dst_prev;
    return copy;
}
void time_travel(t_stack *ts, int k) {
    if (k < 0 || k > ts->hist->versions - 1) { return; }
    // since head is the latest, we need to walk (versions-1 - k) steps to reach snapshot k
    int target = ts->hist->versions - 1 - k;
    t_history_node *curr = ts->hist->head;
    for (int i = 0; i < target; i++) {curr = curr->next;}
    // replace current stack with DEEP COPY of snapshot
    t_stack *copy = t_deepcopy(curr->snapshot);
    ts->top = copy->top;
    ts->size = copy->size;
    // push this restored state into history
    t_history_node *hnode = malloc(sizeof(t_history_node));
    hnode->snapshot = copy;
    hnode->next = ts->hist->head;
    ts->hist->head = hnode;
    ts->hist->versions++;
}
