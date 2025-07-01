#include <stdio.h>
#include <stdlib.h>
#include "sorted_streaks.h"
#define MAX_LEN 10

struct node *Build()
{
    // int arr[] = {1,1,1,1,1,2};
    // int arr[] = {1,3,8,100};
    int arr[] = {1,2,3,4,5};
    // int arr[] = {3,1,2,2,5,6,1,4,5,5,3};
    // int arr[] = {1};
    int len = sizeof(arr) / sizeof(arr[0]);
    if (len == 0)
    {
        return NULL;
    }
    else 
    {
        struct node *list = (struct node*)malloc(sizeof(struct node));
        struct node *curr = list;
        list->next = NULL;
        for (int i = 0; i < len; i++)
        {
            if (i==0)
            {
                curr->val = arr[i];
            }
            else 
            {
                struct node *newNode = (struct node*)malloc(sizeof(struct node ));
                newNode->val = arr[i];
                curr->next = newNode;
                curr = newNode;
            }
        }
        curr->next = NULL;
        return list;
    }
}


void Display(struct node *head)
{
    struct node *curr = head;
    while (curr!= NULL)
    {
        printf("%d -> ", curr->val);
        curr = curr->next;
    }
    printf("NULL\n");
}

// 3 | 1,2,2,5,6 | 1,4,5,5 | 3 
// 1 2 | 1

int sorted_streaks(struct node *head, struct node **result)
{
    struct node *curr = head;
    struct node *store = NULL;
    int subs = 0;
    if (head == NULL)
    {
        curr = NULL;
        return 0;
    }
    if (head->next == NULL)
    {
        result[0] = head;
        return 1;
    }
    {
        while (curr)
        {
            store = curr->next;
            if (curr->next != NULL&& curr->val > curr->next->val)
            {
                curr->next = NULL;
                result[subs] = head;
                head = store;
                subs++;
            }
            curr = store;
        }
        result[subs] = head;
        subs += 1;
        return subs;
    }
}

int main()
{
    int length = 0;
    struct node *head = Build();
    struct node *result[MAX_LEN];
    int ret = sorted_streaks(head, result);
    for (int i = 0; i < ret; i++)
    {
        Display(result[i]);
    }
    printf("%d ", ret);
}