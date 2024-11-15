#include "Stack.h"

#include <iostream>
#include <string>

char returnOpen(char c)
{
	switch(c)
	{
	case ')': return '(';
	case ']': return '[';
	case '}': return '{';
	}
	return ' ';
}

bool validExp(const std::string& exp)
{
	Stack<int> st;
	for (const char c: exp)
	{
		if (c == '(' or c == '[' or c == '{')
			st.push(c);
		else if (c == ')' or c == ']' or c == '}')
		{
			if (st.empty() || st.top() != returnOpen(c)) return false;
			st.pop();
		}
	}
	return st.empty();
}

int main()
{
	std::string exp;
	std::cout << "Enter a mathematical expression: ";
	std::getline(std::cin, exp);

	std::cout << std::boolalpha;
	std::cout << "The expression is: " << validExp(exp) << '\n';
	return 0;
}
