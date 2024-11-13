#include "SparseMatrix.h"

#include <iostream>

IntMat getMatrix(std::string msg)
{
	std::cout << msg << "row count: ";
	int rowCnt;
	std::cin >> rowCnt;

	std::cout << "column count: ";
	int colCnt;
	std::cin >> colCnt;

	std::cout << "Matrix:\n";
	IntMat mat{};
	mat.resize(rowCnt);
	for (int i = 0; i < rowCnt; ++i)
	{
		mat[i].resize(colCnt);
		for (int j = 0; j < colCnt; ++j) std::cin >> mat[i][j];
	}
	return mat;
}

int main()
{
	auto mat1 = getMatrix("Enter first matrix:\n");
	auto mat2 = getMatrix("\nEnter seccond matrix:\n");

	auto sparse1 = SparseMatrix::create(mat1);
	auto sparse2 = SparseMatrix::create(mat2);

	std::cout << "\nAddition is:\n" << sparse1 + sparse2;
	sparse1.transpose();
	std::cout << "\nTranspose of first is:\n" << sparse1;
}
