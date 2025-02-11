#include <stdio.h>
#include "reverse_circ.h"
#include <stdlib.h>

struct node *Build()
{
    int arr[] = {1,2,3,4,5};
    int len = sizeof(arr) / sizeof(arr[0]);
    struct node *list = (struct node*)malloc(sizeof(struct node));
    struct node *curr = list;
    curr->next = NULL;
    for (int i = 0; i < len; i++)
    {
        if (i==0)
        {
            curr->val = arr[i];
        }
        else 
        {
            struct node *newNode = (struct node*)malloc(sizeof(struct node*));
            newNode->val = arr[i];
            curr->next = newNode;
            curr = newNode;
        }
    }
    curr->next = NULL;

    return list;
}

struct node *Build123()
{
    struct node *head = NULL;
    struct node *first = NULL;
    struct node *second = NULL;
    struct node *third = NULL;
    struct node *fourth = NULL;
    struct node *fifth = NULL;

    head = (struct node*)malloc(sizeof(struct node));
    first = (struct node*)malloc(sizeof(struct node));
    second = (struct node*)malloc(sizeof(struct node));
    third = (struct node*)malloc(sizeof(struct node));
    fourth = (struct node*)malloc(sizeof(struct node));
    fifth = (struct node*)malloc(sizeof(struct node));

    head->val = 1;
    head->next = first;
    
    first->val = 2;
    first->next = second;

    second->val = 3;
    second->next = third;

    third->val = 4;
    third->next = fourth;

    fourth->val = 5;
    fourth->next = head;
    
    return head;

}

void Display(struct node *head)
{
    struct node *curr = head;
    while (curr->next != head)
    {
        printf("%d -> ", curr->val);
        curr = curr->next;
    }
    printf("%d -> ", curr->val);
    printf("\n");
}

int is_circular(struct node *head)
{
    struct node *slow = head;
    struct node *fast = head;
    while (fast->next && fast)
    {
        if (slow->next == fast->next)
        {
            return slow->val;
        }
        else
        {
            slow = slow->next;
            fast = fast->next->next;
        }
    }
}

void reverse_circ(struct node *x)
{
    struct node *prev = NULL;
    struct node *curr = x;
    struct node *nextNode = NULL;
    if (curr == NULL)
    {
        return;
    }
    while (curr)
    {
        nextNode  = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nextNode;
    }
    x = curr;
    return;
}


int main()
{
    struct node *head = Build123();
    Display(head);
    reverse_circ(head);
    Display(head);
}

// void reverse_circ(struct node *x)
// {

// }