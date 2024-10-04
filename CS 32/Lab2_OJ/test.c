#include "sorted_streaks.h"
#include <stdlib.h>
#include <stdio.h>
#define MAX_LEN 100000
void Push(struct node**headRef,int newData){
    struct node* temp=malloc(sizeof(struct node));
    temp->val=newData;
    temp->next=*headRef;
    *headRef=temp;
}
void PrintList(struct node* head) {
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
    Push(&head, 7);
    Push(&head, 2);
    Push(&head, 5);
    Push(&head, 6);
    return head;
}


int sorted_streaks(struct node *head, struct node **result)
{
    struct node *curr = head;
    struct node *store = NULL;
    int subs = 0;
    int i = 0;
    if (curr == NULL)
    {
        result = NULL;
        return 0;
    }
    if (curr->next == NULL)
    {
        result[0] = head;
        return 1;
    }
    else {
        while (curr->next)
            if (curr->val > curr->next->val)
            {
                store = curr->next;
                curr->next = NULL;
                result[i++] = head;
                head = store;
                curr = store;
                subs++;
            }
            else 
            {
                curr = curr->next;
            }
        result[i++] = head;
        subs += 1;
        return subs;
    }
}
int main(){
    struct node* list=BuildList();
    // Push(&list,1);
    // Push(&list,2);
    // Push(&list,3);
    // Push(&list,4);
    // Push(&list,5);
    PrintList(list);
}
