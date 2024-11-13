#include <iostream>
#include <vector>
#include <string>

class Polynomial
{
public:
	Polynomial(int degree = 0)
	: m_degree{degree} { m_arr.resize(degree); }
	
	int degree() { return m_degree; }
	int coeff(int exp) { return m_arr[exp]; }
	void setCoeff(int exp, int coeff) { m_arr[exp] = coeff; }
	
	void get(std::string msg);
	
private:
	std::vector<int> m_arr{};
	int m_degree{};
};

std::ostream& operator<<(std::ostream& out, Polynomial poly);
Polynomial operator+(Polynomial first, Polynomial second);

// ---------- main -----------
int main()
{
	Polynomial p1, p2;
	p1.get("Enter first polynomial:\n");
	p2.get("\nEnter second polynomial:\n");
	
	std::cout << '\n' << p1 << "\n+\n" << p2 << "\n----------\n" << p1 + p2 << '\n';
}
// -----------end -----------------

Polynomial operator+(Polynomial first, Polynomial second)
{
	Polynomial result( std::max(first.degree(), second.degree()) );
	int i;
	for (i = 0; i <= std::min(first.degree(), second.degree()); i++)
		result.setCoeff(i, first.coeff(i) + second.coeff(i));
		
	while (i <= first.degree())
	{
		result.setCoeff(i, first.coeff(i));
		i++;
	}
	
	while (i <= second.degree())
	{
		result.setCoeff(i, second.coeff(i));
		i++;
	}
	
	return result;
}

/**
 *		- else
 *			- else if coefficient == 1 --> output " + " + "x^i"
 *			- else if coefficient == -1 --> output " - " + "x^i"
 *			- else
 *				- if coeff < 0 --> output " - " + "abs(coeff) x^i"
 *				- else --> output " + " + "coeff x^i"
**/

std::ostream& operator<<(std::ostream& out, Polynomial poly)
{
	bool isFirst = true;
	for (int i = poly.degree(); i >= 0; i--)
	{
		int coeff = poly.coeff(i);
		if (coeff == 0) continue;

		if (isFirst)
		{
			if (i == 0) out << coeff;
			else if (coeff == 1) out << "x^" << i;
			else if (coeff == -1) out << "-x^" << i;
			else out << coeff << "x^" << i;

			isFirst = false;
		}
		else
		{
			if (i == 0)
			{
				if (coeff < 0) out << " - " << std::abs(coeff);
				else out << " + " << coeff;
			}
			else if (coeff == 1) out << " + x^" << i;
			else if (coeff == -1) out << " - x^" << i;
			else
			{
				if (coeff < 0) out << " - " << std::abs(coeff) << "x^" << i;
				else out << " + " << coeff << "x^" << i;
			}
		}
	}
	return out;
}

void Polynomial::get(std::string msg)
{
	std::cout << msg << "What is highest order: ";
	std::cin >> m_degree;
	m_arr.resize(m_degree + 1);
	
	int cnt = m_degree;
	while (cnt-- >= 0)
	{
		std::cout << ":";
		std::cout<< "\texponential >>> ";
		std::size_t exp;
		std::cin >> exp;
		if (exp > m_degree)
		{
			std::cerr << "Error: Invalid Degree\n";
			cnt++;
			continue;
		}
		std::cout << "\tcoefficient >>> ";
		std::cin >> m_arr[exp];
		if (exp == 0) break;
	}
}

