#include <iostream>
#include <string>

constexpr int SIZE = 10;

class FriendSparse
{
public:
	int mat[SIZE][3];

	FriendSparse(int cnt = 0)
	{
		mat[0][0] = mat[0][1] = cnt;
		mat[0][2] = 0;
	}

	void insert(int i, int j)
	{
		if (i > mat[0][0] || j > mat[0][1]) return;
		if (mat[0][2] + 1 > SIZE) return;

		int index = mat[0][2] += 1;
		mat[index][0] = i;
		mat[index][1] = j;
		mat[index][2] = 1;
	}

	void display()
	{
		for (int i = 1; i <= mat[0][2]; i++)
			std::cout << mat[i][0] << " has connection with " << mat[i][1] << '\n';
	}

	void displaySparse()
	{
		for (int i = 0; i < SIZE; i++)
			std::cout << mat[i][0] << '-' << mat[i][1] << '-' << mat[i][2] << '\n';
	}
};

int main() {
	FriendSparse a(4);
	a.insert(1, 2);
	a.insert(3, 1);
	a.insert(1, 3);

	a.display();
	return 0;
}
