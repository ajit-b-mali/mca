#include <iostream>
#include <queue>
#include <array>
#include <utility>

using Board = std::array<std::array<int, 4>, 4>;
using Position = std::pair<int, int>;

void print(Board& board);
void solve4Q(Board& board, int row, std::queue<Position>& q);
bool isValid(Board& board, int row, int col);


int main()
{
	Board board{};
	std::queue<Position> q{};
    solve4Q(board, 0, q);
    return 0;
}

void print(Board& board)
{
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            if (board[i][j])
                std::cout << "Q ";
            else
                std::cout << ". ";
        }
        std::cout << '\n';
    }
    std::cout << '\n';
}

void solve4Q(Board& board, int row, std::queue<Position>& q)
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
			q.push({row, j});
            solve4Q(board, row + 1, q);
            board[row][j] = 0;
			q.pop();
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
