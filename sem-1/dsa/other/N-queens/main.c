#include <stdio.h>

#define N 8

typedef struct {
    int row;
    int col;
} Position;

typedef struct {
    Position positions[N];
    int front;
    int rear;
} Queue;

void initializeQueue(Queue *q) {
    q->front = -1;
    q->rear = -1;
}

int isEmpty(Queue *q) {
    return q->front == -1;
}

int isFull(Queue *q) {
    return q->rear == N - 1;
}

void enqueue(Queue *q, Position pos) {
    if (isFull(q)) {
        printf("Queue is full\n");
        return;
    }
    if (isEmpty(q)) {
        q->front = 0;
    }
    q->rear++;
    q->positions[q->rear] = pos;
}

Position dequeue(Queue *q) {
    Position pos = { -1, -1 };
    if (isEmpty(q)) {
        printf("Queue is empty\n");
        return pos;
    }
    pos = q->positions[q->front];
    if (q->front == q->rear) {
        q->front = q->rear = -1;
    } else {
        q->front++;
    }
    return pos;
}

int isSafe(int board[N][N], int row, int col) {
    int i, j;
    for (i = 0; i < col; i++)
        if (board[row][i])
            return 0;
    for (i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if (board[i][j])
            return 0;
    for (i = row, j = col; j >= 0 && i < N; i++, j--)
        if (board[i][j])
            return 0;
    return 1;
}

int solveNQUtil(int board[N][N], int col, Queue *q) {
    if (col >= N)
        return 1;
    for (int i = 0; i < N; i++) {
        if (isSafe(board, i, col)) {
            board[i][col] = 1;
            Position pos = { i, col };
            enqueue(q, pos);
            if (solveNQUtil(board, col + 1, q))
                return 1;
            board[i][col] = 0;
            dequeue(q);
        }
    }
    return 0;
}

void printSolution(int board[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++)
            printf(" %d ", board[i][j]);
        printf("\n");
    }
}

int solveNQ() {
    int board[N][N] = {0};
    Queue q;
    initializeQueue(&q);
    if (solveNQUtil(board, 0, &q) == 0) {
        printf("Solution does not exist");
        return 0;
    }
    printSolution(board);
    return 1;
}

int main() {
    solveNQ();
    return 0;
}


