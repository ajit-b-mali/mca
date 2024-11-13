#include <iostream>
#include <vector>

#include "SparseMatrix.h"

int main()
{
    std::vector<std::vector<int>> arr{
        {1, 2, 0},
        {0, 0, 0},
        {1, 0, 0}
    };

    SparseMatrix sparse{ SparseMatrix::create(arr) };

    std::cout << "Sparse:\n" << sparse << '\n';
    sparse.transpose();
    std::cout << "transpose:\n" << sparse << '\n';
}
