#include <stdlib.h>
#include <stdio.h>
#include "squares.h"

void Push(struct node**headRef,int newData){
    struct node* temp=malloc(sizeof(struct node));
    temp->val=newData;
    temp->next=*headRef;
    *headRef=temp;
}
void Display(struct node* head) {
    struct node* current = head;
    while (current != NULL) {
        printf("%d -> ", current->val);
        current = current->next;
    }
    printf("NULL\n"); // Indicate the end of the list
}

struct node* BuildList(){
    struct node* head=NULL;
    Push(&head, 3);
    Push(&head, 9);
    Push(&head, 25);
    Push(&head, 24);
    Push(&head, 0);
    Push(&head, 25);
    return head;
}


#include <stdlib.h>
#include "squares.h"

int squareroot(int n)
{
    if (n < 0) return 0;
    for (int i = 0; i < n; i++)
    {
        if ((i*i) == n)
        {
            return 1;
        }
    }
    return 0;
}

int squares(struct node *head, int **res)
{
    struct node *curr = head;

    int size = 0;
    int re_sized = 0;

    while (curr)
    {
        if (squareroot(curr->val) || curr->val == 0)
        {
            re_sized++;
        }
        curr = curr->next;
    }
    curr = head;

    int *array = (int*)malloc(re_sized * sizeof(int));
    int i = 0;
    while (curr)
    {
        if (squareroot(curr->val) || curr->val == 0)
        {
            array[i++] = curr->val;
        }
        curr = curr->next;
    }

    *res = array;
    return re_sized;
}

int main()
{
    struct node *head = BuildList();
    int *res = (int*)malloc(sizeof(int));
    Display(head);
    squares(head, &res);
    for (int i = 0; i < 4; i++)
    {
        printf("%d ", res[i]);
    }
}