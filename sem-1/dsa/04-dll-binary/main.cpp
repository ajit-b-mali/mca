#include "Binary.h"
#include <iostream>

int main()
{
    std::cout << "Enter binary: ";
    Binary binary1{};
    std::cin >> binary1;
    
    std::cout << "1's compliment: " << binary1.ones() << '\n';
    std::cout << "2's compliment: " << binary1.twos() << '\n';

    std::cout << "\nEnter another binary: ";
    Binary binary2{};
    std::cin >> binary2;

    std::cout << binary1 << "\n+\n" << binary2
        << "\n--------\n" << binary1 + binary2 << std::endl;
}
