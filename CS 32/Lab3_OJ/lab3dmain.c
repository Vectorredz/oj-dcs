// [3, 7, 2, 5, 6]

#include <stdio.h>
#include <stdlib.h>
#include "even.h"

void Push(struct node **headref, int data)
{
    struct node *newNode = (struct node*)malloc(sizeof(struct node));
    newNode->val = data;
    newNode->next = *headref;
    *headref = newNode;
}

void Display(struct node* head) 
{
    struct node* current = head;
    while (current != NULL) 
    {
        printf("%d -> ", current->val);
        current = current->next;
    }
    printf("NULL\n"); 
}

struct node *Build()
{
    struct node *head = NULL;
    Push(&head, 5);
    Push(&head, 5);
    Push(&head, 2);
    Push(&head, 7);
    Push(&head, 3);
    return head;
}

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

int main()
{
    struct node *head = Build();
    Display(head);
    struct node *ret = even(head);
    Display(ret);
}
