#ifndef BINARY_H
#define BINARY_H

#include <initializer_list>
#include <iostream>

class Binary
{
public:
    struct Node { bool data{}; Node* next{}; Node* back{}; };

public:
    Binary() = default;
    Binary(std::initializer_list<int> digits) { for (int d: digits) push_back(d); }

    void push_front(bool d);
    void push_back(bool d);
    Binary ones() const;
    Binary twos() const;

    friend Binary operator+(const Binary& first, const Binary& second);
    friend std::ostream& operator<<(std::ostream& out, const Binary& binary);

private:
    Node* head{ nullptr };
    Node* tail{ nullptr };
};

std::istream& operator>>(std::istream& in, Binary& binary);
Binary operator+(const Binary& first, const Binary& second);

#endif