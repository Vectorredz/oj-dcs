#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define STRMAX_LEN 10000

/*
note: 
the first line output is the corresponding letter/symbol i, 
where 0<= i <= 255 according to bytes

*/


//node to use for the current data cell
typedef struct datacell {
    char value;
    struct datacell *prev;
    struct datacell *next;
} Datacell;


Datacell* create_node();
int matching_bracket(int len, char* bf_program, int* match_bracket_arr);
void BF(int n, char* bf_program, int* input);


//helper function to create nodes allocation
Datacell* create_node() {
    Datacell *new_cell = (Datacell*)malloc(sizeof(Datacell));
    new_cell->value = 0;
    new_cell->prev = new_cell->next = NULL;
    return new_cell;
}


//for brackets
//for open, traverse string until current data cell is zero, store index value of bracket(?)
//for close, traverse string until current data cell is nonzero, store index value of bracket(?)

int matching_bracket(int len, char* bf_program, int* match_bracket_arr){
    int stack[STRMAX_LEN];
    int top = 0;

    for(int i = 0; i < len; i++){
        if(bf_program[i] == '['){
            stack[top++] = i;
        }else if(bf_program[i] == ']'){
            if (top == 0){ //if there is no current top and we detect closing bracket, it is a mismatch
                return 0;
            }
            int index = stack[--top]; //pop the bracket 
            match_bracket_arr[index] = i;
            match_bracket_arr[i] = index;
        }
    }
    return (top == 0);
}


void BF(int n, char* bf_program, int* input){
    Datacell* curr_data_ptr = create_node(); //starts at a single node
    int instruction_idx = 0; //indexing for the bf_program in exchange for for loop if-else to switch case
    int input_idx = 0; //to access the array of input according to bf_program

    int match_bracket_arr[STRMAX_LEN];
    if(!matching_bracket(strlen(bf_program), bf_program, match_bracket_arr)){
        printf("UNCLOSED\n");
        free(curr_data_ptr);
        return;
    }

    while(bf_program[instruction_idx]){
        switch (bf_program[instruction_idx]){
        case '>':
            if(!curr_data_ptr->next){
                curr_data_ptr->next = create_node();
                curr_data_ptr->next->prev = curr_data_ptr;
            }
            curr_data_ptr = curr_data_ptr->next;
            break;
        case '<':
            if(!curr_data_ptr->prev){
                curr_data_ptr->prev = create_node();
                curr_data_ptr->prev->next = curr_data_ptr;
            }
            curr_data_ptr = curr_data_ptr->prev;
            break;
        case '+':
            if(curr_data_ptr->value < 255){ //truncate if adding to value will be greater than 255
                curr_data_ptr->value++;
            }
            break;
        case '-':
            if(curr_data_ptr->value > 0){ //truncate if subtracting to value will be less than 0
                curr_data_ptr->value--;
            }
            break;
        case '.':
            printf("%c", curr_data_ptr->value);
            break;
        case ',':
            if(input_idx >= n){
                printf("NO INPUT\n");
                return;
            }
            curr_data_ptr->value = input[input_idx++];
            break;
        case '[':
            if(curr_data_ptr->value == 0){
                instruction_idx = match_bracket_arr[instruction_idx];
            }
            break;
        case ']':
            if(curr_data_ptr->value != 0){
                instruction_idx = match_bracket_arr[instruction_idx];
            }
            break;
        }

        instruction_idx++;
        
    }

    printf("\n");

    //since our position is not explicitly leftmost/rightmost
    //to print from left to right, go back to the leftmost position
    while(curr_data_ptr->prev){
        curr_data_ptr = curr_data_ptr->prev;
    }
    while(curr_data_ptr){
        printf("%d", curr_data_ptr->value);
        if(curr_data_ptr->next){
            printf(",");
        }
        //print next values
        Datacell *store_ptr = curr_data_ptr;
        curr_data_ptr = curr_data_ptr->next;
        free(store_ptr);
    }

    printf("\n");

}


int main() {
    int n;
    scanf("%d", &n);

    char bf_program[STRMAX_LEN];
    scanf("%s", bf_program);

    int *input_val = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        scanf("%d", &input_val[i]);
    }

    BF(n, bf_program, input_val);
    
    free(input_val);
    return 0;
}