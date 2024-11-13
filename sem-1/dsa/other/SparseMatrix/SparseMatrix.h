#ifndef SPARSEMATRIX_H
#define SPARSEMATRIX_H

#include <iostream>
#include <vector>

class SparseMatrix
{
public:
    static SparseMatrix create(std::vector<std::vector<int>> arr);

    SparseMatrix(int rowCnt = 0, int colCnt = 0, int nonZeroCnt = 0)
    {
        m_mat.push_back({rowCnt, colCnt, nonZeroCnt});
        m_mat.reserve(nonZeroCnt);
    }

    void insert(const std::vector<int>& record);
    void transpose();
    
    const std::vector<int>& operator() (int i) const;
    std::vector<int>& operator() (int i);
    const int& operator() (int i, int j) const;
    int& operator() (int i, int j);
    
    friend std::ostream& operator<< (std::ostream& out, const SparseMatrix& sparse);
    friend SparseMatrix operator+ (const SparseMatrix& first, const SparseMatrix& second);

private:
    std::vector<std::vector<int>> m_mat{};
};

#endif