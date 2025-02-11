#include <stdlib.h>
#include "even.h"

struct node *even(struct node *head)
{
    struct node *curr = head;
    struct node *lead = NULL;
    if (curr == NULL) return NULL;
    if (curr->next == NULL)
    {
        struct node *even = (struct node*)malloc(sizeof(struct node));
        even->val = 2;
        curr->next = even;
        even->next = NULL;
        curr = even;
    }
    while (curr->next)
    {
        if (curr->val * curr->next->val % 2 != 0)
        {
            lead = curr->next;
            struct node *even = (struct node*)malloc(sizeof(struct node));
            even->val = 2;
            curr->next = even;
            even->next = lead;
            curr = even;
        }
        else 
        {
            curr = curr->next;
        }
    }
    return head;
}
