#include <iostream>
#include <array>

using Board = std::array<std::array<int, 4>, 4>;
void print(Board& board);
void solve4queens(Board& board);
void solve4Q(Board& board, int row);
bool isValid(Board& board, int row, int col);


int main()
{
    Board board{};
    solve4queens(board);

    return 0;
}

void print(Board& board)
{
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            if (board[i][j])
                std::cout << board[i][j] << ' ';
            else
                std::cout << board[i][j] << ' ';
        }
        std::cout << '\n';
    }
    std::cout << '\n';
}

void solve4queens(Board& board)
{
    solve4Q(board, 0);
}

void solve4Q(Board& board, int row)
{
    if (row == 4)
    {
        print(board);
        return;
    }

    for (int j = 0; j < 4; j++)
    {
        if (isValid(board, row, j))
        {
            board[row][j] = 1;
            solve4Q(board, row + 1);
            board[row][j] = 0;
        }
    }
}

bool isValid(Board& board, int row, int col)
{
    for (int i = row; i >= 0; i--)
    {
        if (board[i][col])
            return false;
    }

    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--)
    {
        if (board[i][j])
            return false;
    }

    for (int i = row, j = col; i >= 0 && j < 4; i--, j++)
    {
        if (board[i][j])
            return false;
    }

    return true;
}
