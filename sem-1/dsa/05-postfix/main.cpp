#include "Stack.h"
// #include <stack>
#include <iostream>
#include <string>
#include <cctype>

int order(char opr)
{
	if (opr == '+' || opr == '-') return 1;
	if (opr == '*' || opr == '/') return 2;
	return 0;
}

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

std::string infixToPostfix(const std::string& infix)
{
	Stack st;
	// std::stack<char> st;
	std::string postfix;

	for (char c: infix)
	{
		if (c == ' ') continue;
		if (std::isalnum(c))
			postfix += c;
		else if (st.empty() || order(c) > order(st.top()) || c == '(' || c == '[' || c =='{')
			st.push(c);
		else if (c == ')' || c == ']' || c == '}')
		{
			while (st.empty() || st.top() != returnOpen(c))
			{
				postfix += st.top();
				st.pop();
			}
			st.pop();
		}
		else if (order(c) <= order(st.top()))
		{
			while (!st.empty())
			{
				postfix += st.top();
				st.pop();
			}
			st.push(c);
		}
	}

	while (!st.empty())
	{
		postfix += st.top();
		st.pop();
	}
	return postfix;
}

int main()
{
	std::string infix;
	std::cout << "Enter infix: ";
	std::getline(std::cin, infix);

	std::string postfix = infixToPostfix(infix);
	std::cout << "POSTFIX: " << postfix << '\n';
	return 0;
}
