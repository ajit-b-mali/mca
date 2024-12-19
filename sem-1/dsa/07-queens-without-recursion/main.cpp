#include <iostream>
#include <queue>
#include <array>
#include <cmath>

struct QState
{
    int board[4] = {-1};
    int row = 0;
};

bool isValid(int board[4], int row, int col)
{
    for (int i = 0; i < row; ++i)
    {
        int j = board[i];
        if (j == col || std::abs(i - row) == std::abs(j - col))
            return false;
    }
    return true;
}

void printBoard(int board[4])
{
    static int cnt = 0;
    std::cout << "\nPossibility >>> " << cnt << ":\n";
    cnt += 1;
    
    for (int i = 0; i < 4; ++i)
    {
        for (int j = 0; j < 4; ++j)
        {
            if (board[i] == j)
                std::cout << "Q ";
            else
                std::cout << "- ";
        }
        std::cout << '\n';
    }
    std::cout << '\n';
}

void solveQueens() {
    std::queue<QState> q;
    q.push({});

    while (!q.empty())
    {
        QState current = q.front(); q.pop();

        if (current.row == 4) 
        {
            printBoard(current.board);
            continue;
        }
        
        int row = current.row;
        for (int col = 0; col < 4; ++col)
        {
            if (isValid(current.board, row, col))
            {
                QState next = current;
                next.board[row] = col;
                next.row++;
                q.push(next);
            }
        }
    }
}

int main()
{
    solveQueens();
    return 0;
}

