#include "Binary.h"
#include <iostream>

int main()
{
    Binary binary1{};
    std::cout << "Enter binary: ";
    std::cin >> binary1;
    
    Binary binary2{};
    std::cout << "Enter another binary: ";
    std::cin >> binary2;

    std::cout << "1's compliment: " << binary1.ones() << '\n';
    std::cout << "2's compliment: " << binary1.twos() << '\n';

    std::cout << '\n' << binary1 << "\n+\n" << binary2
        << "\n--------\n" << binary1 + binary2 << std::endl;
}
