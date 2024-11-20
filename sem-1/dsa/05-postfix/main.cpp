#include "Stack.h"

#include <iostream>
#include <string>
#include <cctype>

int order(char opr);
char returnOpen(char c);
std::string infixToPostfix(const std::string& infix);

double evalPostfix(const std::string& postfix);

int main()
{
	std::string infix;
	std::cout << "Enter infix: ";
	std::getline(std::cin, infix);

	std::string postfix = infixToPostfix(infix);
	std::cout << "POSTFIX: " << postfix << '\n';
	std::cout << "RESULT: " << evalPostfix(postfix) << '\n';

	return 0;
}

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
	Stack<char> st;
	std::string postfix;

	for (char c: infix)
	{
		bool isOpen = c == '(' || c == '[' || c == '{'; 
		bool isClose = c == ')' || c == ']' || c == '}';

		if (c == ' ') continue;
		if (std::isalnum(c))
			postfix += c;
		else if (st.empty() || order(c) > order(st.top()) || isOpen)
			st.push(c);
		else if (isClose)
		{
			while (st.empty() || st.top() != returnOpen(c))
			{
				postfix += st.top(); st.pop();
			}
			st.pop();
		}
		else if (order(c) <= order(st.top()))
		{
			while (!st.empty())
			{
				postfix += st.top(); st.pop();
			}
			st.push(c);
		}
	}

	while (!st.empty())
	{
		postfix += st.top(); st.pop();
	}
	return postfix;
}

double evalPostfix(const std::string& postfix)
{
	Stack<double> st;

	for (auto c: postfix)
	{
		if (std::isdigit(c))
			st.push(c - '0');
		else if (std::isalpha(c))
			st.push(0);
		else
		{
			double b = st.top(); st.pop();
			double a = st.top(); st.pop();

			if      (c == '+') st.push(a + b);
			else if (c == '-') st.push(a - b);
			else if (c == '*') st.push(a * b);
			else if (c == '/') st.push(a / b);
			else               st.push(0);
		}
	}

	return st.top();
}

