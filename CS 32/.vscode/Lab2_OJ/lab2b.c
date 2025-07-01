#include <stdio.h>
#include <stdlib.h>
#include "splice.h"

struct node *Build()
{
    int arr[] = {1,2,3,4,5,6};
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

void Display(struct node *head)
{
    while (head)
    {
        printf("%d -> ", head->val);
        head = head->next;
    }
    printf("\n");
}

// must return a pointer [i, j)
// head->spliced 
struct node *splice(struct node **head, int i, int j)
{
    struct node *curr = *head;
    struct node *prev = NULL;
    struct node *spliceHead = NULL;
    struct node *splicePtr = NULL;
    struct node *spliceTail = NULL;
    struct node *splicePrev = NULL;
    if (i < 0 || j < i) 
    {
        return NULL;
    }
    else if (i == 0) 
    {
        spliceHead = curr;
        splicePtr = spliceHead;
        for (int x = 0; x < j-1; x++)
        {
            splicePtr = splicePtr->next;
        }
        spliceTail = splicePtr->next;
        *head = spliceTail;
        splicePtr->next = NULL;
        return spliceHead;
    }
    else
    {
        for (int x = 0; x < i; x++)
        {
            prev = curr;
            curr = curr->next;
        }
        spliceHead = curr;
        splicePtr = spliceHead;
        splicePrev = prev;
        for (int x = i; x < j-1; x++)
        {
            splicePtr = splicePtr->next;
        }
        spliceTail = splicePtr->next;
        splicePtr->next = NULL;
        prev->next = spliceTail;
        return spliceHead;
    }
}

int main()
{
    struct node *head = Build();
    Display(head);
    struct node *ret = splice(&head, 0, 4);
    Display(ret);

}