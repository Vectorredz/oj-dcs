#include <stdio.h>
#include <stdlib.h>


typedef struct vertex{
    int VRTX;
    struct vertex *NEXT;
} Vertex;

typedef struct queue{
    int *ARR;
    int FRONT;
    int REAR;
} Queue;

typedef struct list{
    Vertex **adj_list;
    int adj_size;
} LIST;

typedef struct matrix{
    int **adj_mat;
    int adj_size;
} MATRIX;

Vertex *create_vertex(int x){
    Vertex *newVertex = malloc(sizeof(Vertex));
    newVertex->VRTX = x;
    newVertex->NEXT = NULL;
    return newVertex;
}

Vertex **init_adj_list(LIST *l){
    Vertex **ADJ = malloc(sizeof(Vertex*) * l->adj_size);
    for (int i = 1; i < l->adj_size; i++){
        ADJ[i] = NULL;
    }

    return ADJ;
}

LIST *init_list(int size){
    LIST *l = malloc(sizeof(LIST));
    l->adj_size = size;
    l->adj_list = init_adj_list(l);

    return l;
}

MATRIX *init_matrix(int size){
    MATRIX *m = malloc(sizeof(MATRIX));
    m->adj_size = size;
    m->adj_mat = malloc(sizeof(int*) * m->adj_size);
    for (int i = 1; i <= m->adj_size; i++){
        m->adj_mat[i] = malloc(sizeof(int) * m->adj_size);
        for (int j = 1; j <= m->adj_size; j++){
            m->adj_mat[i][j] = 0; // init to zeroes
        }
    }
    return m;
}

Queue *init_queue(int size){
    Queue *q = malloc(sizeof(Queue));
    q->FRONT = 0;
    q->REAR = 0;
    q->ARR = malloc(sizeof(int) * size);

    return q;
}

void enqueue(Queue *q, int vx){
    q->ARR[q->REAR++] = vx;
}

int dequeue(Queue *q){
    return q->ARR[q->FRONT++];
}

void m_add_edge(MATRIX *m, int u, int v){
    m->adj_mat[u][v] = 1;
    m->adj_mat[v][u] = 1;
}

void add_edge(LIST *l,  int u, int v){
    // l->adj_list[v]->NEXT = l->adj_list[u];
    Vertex *currVRTX = l->adj_list[u]; // root
    if (!l->adj_list[u]){
        l->adj_list[u] = create_vertex(v);
        l->adj_list[u]->NEXT = NULL;
    }
    else {
        while (currVRTX->NEXT){
            currVRTX = currVRTX->NEXT;
        } 
        Vertex *newVRTX = create_vertex(v);
        currVRTX->NEXT = newVRTX;
        currVRTX = newVRTX;
    }

    // Vertex *v_currVRTX = l->adj_list[v];
    // if (!l->adj_list[v]){
    //     l->adj_list[v] = create_vertex(u);
    //     l->adj_list[v]->NEXT = NULL;
    // }
    // else {
    //     while (v_currVRTX->NEXT){
    //         v_currVRTX = v_currVRTX->NEXT;
    //     } 
    //     Vertex *v_newVRTX = create_vertex(u);
    //     v_currVRTX->NEXT = v_newVRTX;
    //     v_currVRTX = v_newVRTX;
    // }
}

void dfs_rec(LIST *graph, int *visited, int *res, int u, int *j){
    printf("%d ", u);
    visited[u] = 1;
    res[(*j)++] = u;

    Vertex *currVRTX = graph->adj_list[u];
    while (currVRTX){
        if (!visited[currVRTX->VRTX]){
           dfs_rec(graph,visited,res,currVRTX->VRTX,j);
        }
        currVRTX = currVRTX->NEXT;
    }
    
    return;
}

void dfs(LIST *graph){
    // create an array of visits
    int *visited = malloc(sizeof(int) * graph->adj_size);
    int *res = malloc(sizeof(int) * graph->adj_size);

    for (int i = 1; i < graph->adj_size; i++) visited[i] = 0;
    int j;
    dfs_rec(graph, visited, res, 1, &j);

    for (int x = 0; x < j; x++){
        printf("%d ", res[x]);
    }
}

void bfs(LIST *graph, int n){
    int *visited = malloc(sizeof(int) * graph->adj_size);
    int *res = malloc(sizeof(int) * graph->adj_size);
    Queue *Q = init_queue(n);

    for (int i = 1; i < graph->adj_size; i++) visited[i] = 0;
    
    visited[1] = 1;
    enqueue(Q, 1);
    int j = 1;

    while (Q->FRONT < Q->REAR){
        int popped = dequeue(Q);
        printf("%d ", popped);
        res[j++] = popped;

        Vertex *curr = graph->adj_list[popped];
        while (curr){
            if (!(visited[curr->VRTX])){
                visited[curr->VRTX] = 1;
                enqueue(Q, curr->VRTX);
            }
            curr = curr->NEXT;
        }
    }


}

int main(){
    int n;
    scanf("%d", &n);

    // MATRIX *m = init_matrix(n+1);

    // int i = 1;
    // while (1){
    //     int u, v;
    //     scanf("%d %d", &u, &v);
    //     if (!u && !v) break;
    //     m_add_edge(m, u, v);
    //     i++;
    // }

    // for (int i = 1; i <= n; i++){
    //     printf("%d: ", i);
    //     for (int j = 1; j <= n; j++){
    //         printf("%d ", m->adj_mat[i][j]);
    //     }
    //     printf("\n");
    // }

    LIST *l = init_list(n+1);
    // i = 1;
    while (1){
        int u, v;
        scanf("%d %d", &u, &v);
        if (!u && !v) break;
        add_edge(l, u, v);
    }
    // printf("%d", curr->VRTX);
    for (int i = 1; i <= n; i++){
        Vertex *curr = l->adj_list[i];
        printf("%d: ", i);
        while (curr){
            printf("%d -> ", curr->VRTX);
            curr = curr->NEXT;
        }
        printf("NULL \n");
    }
    
    // dfs(l);
    bfs(l, n+1);

}