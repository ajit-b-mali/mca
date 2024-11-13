#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

#include "SparseMatrix.h"

int pairCmp(const std::pair<int, int>& first, const std::pair<int, int>& second)
{
    if (first.first < second.first) return -1;    
    if (first.first > second.first) return 1;    
    if (first.second < second.second) return -1;    
    if (first.second > second.second) return 1;    
    return 0;
}

void SparseMatrix::insert(const std::vector<int>& record)
{
    m_mat.push_back(record);
    ++m_mat[0][2];
}

std::ostream& operator<<(std::ostream& out, const SparseMatrix& sparse)
{
    for (const auto& row: sparse.m_mat)
    {
        for (int e: row) out <<  e << ' ';
        out << '\n';
    }
    return out;
}

SparseMatrix SparseMatrix::create(IntMat mat)
{
    int rowCnt{ static_cast<int>(mat.size()) };
    int colCnt{ static_cast<int>(mat[0].size()) };

    SparseMatrix newSparse{ rowCnt, colCnt };

    for (std::size_t i = 0; i < rowCnt; ++i)
        for (std::size_t j = 0; j < colCnt; ++j)
            if (mat[i][j]) newSparse.insert({static_cast<int>(i), static_cast<int>(j), mat[i][j]});

    return newSparse;
}

SparseMatrix operator+(const SparseMatrix& first, const SparseMatrix& second)
{
    if (first(0, 0) != second(0, 0) || first(0, 1) != second(0, 1))
        return {};
    
    SparseMatrix newSparse{first(0, 0), first(0, 1)};

    int fIndex = 1;
    int sIndex = 1;
    while (fIndex <= first(0, 2) && sIndex <= second(0, 2))
    {
        int ans{ pairCmp({first(fIndex, 0), first(fIndex, 1)}, {second(sIndex, 0), second(sIndex, 1)}) };
        
        switch (ans)
        {
        case 0:
            newSparse.insert({first(fIndex, 0), first(fIndex, 1), first(fIndex, 2) + second(sIndex, 2)});
            ++fIndex;
            ++sIndex;
            break;

        case -1:
            newSparse.insert(first(fIndex++));
            break;
        
        case 1:
            newSparse.insert(second(sIndex++));
            break;
        }
    }

    while (fIndex <= first(0, 2))
        newSparse.insert(first(fIndex++));

    while (sIndex <= second(0, 2))
        newSparse.insert(second(sIndex++));

    return newSparse;
}

void SparseMatrix::transpose()
{
    for (int i{ 0 }; i < m_mat.size(); ++i)
        std::swap(m_mat[i][0], m_mat[i][1]);

    std::sort(m_mat.begin() + 1, m_mat.end());
}
