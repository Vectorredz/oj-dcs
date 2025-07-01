#include <stdio.h>
#include <stdlib.h>
#include "distance.h"

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

void Display(struct node *head)
{
    while (head)
    {
        printf("%d -> ", head->val);
        head = head->next;
    }
    printf("\n");
}


  int distance(struct node *a, struct node *b)
{
    struct node *currA = a;
    struct node *currB = b;
    int jumps = 0;
    if (a == b)
    {
        return 0;
    }
    while (currA)
    {
        if (currA==b)
        {
            return jumps;
        }
        currA = currA->next;
        jumps++;
    }
    while (currB)
    {
        if (currB==a)
        {
            return jumps;
        }
        currB = currB->next;
        jumps++;
    }
}



int main()
{
    struct node *head = Build();
    
    Display(head);
}