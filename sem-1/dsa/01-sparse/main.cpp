#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

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

	int size() { return m_mat[0][2]; }
    void insert(const std::vector<int>& record);
    
    const int& operator()(int i, int j) const { return m_mat[i][j]; }
    
    friend std::ostream& operator<<(std::ostream& out, const SparseMatrix& sparse);

private:
	IntMat m_mat{};
};

IntMat getMatrix(std::string msg);

/*--------------MAIN------------------------------------*/
int main()
{
	auto friends = getMatrix("Enter Friends matrix:\n");
	auto friendSparse = SparseMatrix::create(friends);

	for (int i = 1; i <= friendSparse.size(); i++)
	{
		int isFriend = friendSparse(i, 2);
		if (isFriend)
		{
			std::cout << friendSparse(i, 0) + 1 << " is friend of "
				<< friendSparse(i, 1) + 1 << '\n';
		}
	}
	
	auto map = getMatrix("\nEnter Map matrix:\n");
	auto mapSparse = SparseMatrix::create(map);

	for (int i = 1; i <= mapSparse.size(); i++)
	{
		int isConnected = mapSparse(i, 2);
		if (isConnected)
		{
			std::cout << mapSparse(i, 0) + 1 << " has route of distance "
				<< mapSparse(i, 2) << " to " << mapSparse(i, 1) + 1 << '\n';
		}
	}
}
/*------------------------------------------------------*/

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

IntMat getMatrix(std::string msg)
{
	std::cout << msg << "how many entries: ";
	int cnt;
	std::cin >> cnt;

	std::cout << "Matrix:\n";
	IntMat mat{};
	mat.resize(cnt);
	for (int i = 0; i < cnt; ++i)
	{
		mat[i].resize(cnt);
		for (int j = 0; j < cnt; ++j) std::cin >> mat[i][j];
	}
	return mat;
}