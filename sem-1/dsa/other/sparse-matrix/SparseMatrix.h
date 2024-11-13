#ifndef SPARSEMATRIX_H
#define SPARSEMATRIX_H

#include <iostream>
#include <vector>

typedef std::vector<std::vector<int>> IntMat;

class SparseMatrix
{
public:
    static SparseMatrix create(IntMat mat);

    SparseMatrix(int rowCnt = 0, int colCnt = 0, int nonZeroCnt = 0)
    {
        m_mat.push_back({rowCnt, colCnt, nonZeroCnt});
        m_mat.reserve(nonZeroCnt);
    }

    void insert(const std::vector<int>& record);
    void transpose();
    
    const std::vector<int>& operator() (int i) const { return m_mat[i]; }
    const int& operator() (int i, int j) const { return m_mat[i][j]; }
    
    friend std::ostream& operator<< (std::ostream& out, const SparseMatrix& sparse);
    friend SparseMatrix operator+ (const SparseMatrix& first, const SparseMatrix& second);

private:
	IntMat m_mat{};
};

#endif

