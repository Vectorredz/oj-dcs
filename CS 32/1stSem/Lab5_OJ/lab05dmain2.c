#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>

// DEQUE NODE
typedef struct deque_node {
    int64_t data;
    struct deque_node *left;
    struct deque_node *right;
} deque_node;

// DEQUE
typedef struct deque {
    deque_node *leftmost;
    deque_node *rightmost;
    uint32_t size;
} deque;

// Initialize a deque
deque *deque_init() {
    deque *d = (deque *)malloc(sizeof(deque));
    d->leftmost = NULL;
    d->rightmost = NULL;
    d->size = 0;
    return d;
}

// Check if deque is empty
int deque_empty(deque *d) {
    return (d->size == 0);
}

// Push an element to the right of the deque
void deque_push_right(deque *d, int64_t data) {
    deque_node *newNode = (deque_node *)malloc(sizeof(deque_node));
    newNode->data = data;
    newNode->left = d->rightmost;
    newNode->right = NULL;

    if (deque_empty(d)) {
        d->leftmost = newNode; // First element
    } else {
        d->rightmost->right = newNode; // Append to the rightmost
    }
    d->rightmost = newNode; // Update rightmost
    d->size++;
}

// Pop an element from the left of the deque
int64_t deque_pop_left(deque *d) {
    if (deque_empty(d)) {
        return 0;  
    }

    int64_t popped = d->leftmost->data;
    deque_node *temp = d->leftmost;

    d->leftmost = d->leftmost->right; // Move leftmost pointer
    if (d->leftmost) {
        d->leftmost->left = NULL; // Update left pointer
    } else {
        d->rightmost = NULL; // If empty, set rightmost to NULL
    }
    free(temp);
    d->size--;
    return popped;
}

// QUEUE
typedef struct queue {
    deque *enqueue_deque; // Deque for enqueueing
    deque *dequeue_deque; // Deque for dequeueing
    int64_t size;
} queue;

// Initialize the queue
queue *queue_init(void) {
    queue *q = (queue *)malloc(sizeof(queue));
    q->enqueue_deque = deque_init();
    q->dequeue_deque = deque_init();
    q->size = 0;
    return q;
}

// Check if queue is empty
int queue_empty(queue *q) {
    return (q->size == 0);
}

// Enqueue function
void enqueue(queue *q, int64_t val) {
    deque_push_right(q->enqueue_deque, val);
    q->size++;

    // Maintain the monotonic property in the dequeue deque
    while (!deque_empty(q->dequeue_deque) && q->dequeue_deque->rightmost->data > val) {
        deque_pop_left(q->dequeue_deque); // Remove larger elements
    }
    deque_push_right(q->dequeue_deque, val); // Push to min deque
}

// Dequeue function
int64_t dequeue(queue *q) {
    if (queue_empty(q)) {
        return 0;
    }

    // If dequeue_deque is empty, refill it from enqueue_deque
    if (deque_empty(q->dequeue_deque)) {
        while (!deque_empty(q->enqueue_deque)) {
            int64_t val = deque_pop_left(q->enqueue_deque);
            deque_push_right(q->dequeue_deque, val);
        }
    }

    int64_t dequeued = deque_pop_left(q->dequeue_deque);
    q->size--;
    return dequeued;
}

// Peek front of the queue
int64_t peek_front(queue *q) {
    if (queue_empty(q)) {
        return 0;
    }

    // Check the front of the dequeue_deque
    if (!deque_empty(q->dequeue_deque)) {
        return q->dequeue_deque->leftmost->data;
    }

    return 0; // If both are empty
}

// Get the minimum element in the queue
int64_t queue_min(queue *q) {
    if (queue_empty(q)) {
        return 0;
    }
    return q->dequeue_deque->leftmost->data; // Return min from dequeue_deque
}

// Display function for demonstration purposes
void display_deque(deque *d) {
    if (deque_empty(d)) {
        printf("Deque is empty\n");
        return;
    }
    deque_node *current = d->leftmost;
    while (current != NULL) {
        printf("%lld -> ", current->data);
        current = current->right;
    }
    printf("NULL\n");
}

// Display the queue contents
void display_queue(queue *q) {
    printf("Queue:\n");
    display_deque(q->enqueue_deque);
    printf("Min Deque:\n");
    display_deque(q->dequeue_deque);
}

int main() {
    queue *q1 = queue_init();
    enqueue(q1, 6);
    enqueue(q1, 3);
    enqueue(q1, 9);
    enqueue(q1, 5);
    
    display_queue(q1); // Display both deques
    printf("Queue min: %lld\n", queue_min(q1)); // Show minimum value in queue

    // Free allocated memory (not shown for brevity)
    return 0;
}
