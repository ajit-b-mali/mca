#include "Stack.h"

#include <iostream>
#include <string>

bool validExp(const std::string& exp)
{
	Stack<int> st;
	for (const char c: exp)
	{
		if (c == '(' || c == '[' || c == '{')
			st.push(c);
		else if (c == ')' && (st.empty() || st.top() != '('))
			return false;
		else if (c == ']' && (st.empty() || st.top() != '['))
			return false;
		else if (c == '}' && (st.empty() || st.top() != '{'))
			return false;
		else if (c == ')' || c == ']' || c == '}')
			st.pop();
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
