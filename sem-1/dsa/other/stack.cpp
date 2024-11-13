#include <iostream>
#include <vector>

class Stack
{
public:
	Stack() = default;

	Stack(int size)
		: m_size(size)
	{
		m_stack.resize(size);
	}

	void push(int element);
	int pop();
	bool isFull() { return m_top == m_size - 1; }
	bool isEmpty() { return m_top == -1; }

private:
	std::vector<int> m_stack{};
	int m_top{ -1 };
	int m_size{ 0 };
};

void Stack::push(int element)
{
	if (isFull()) 
		std::cout << "Overflow\n";
	else
		m_stack[++m_top] = element;
}

int main()
{
	std::cout << "Hello, World!\n";
	return 0;
}

