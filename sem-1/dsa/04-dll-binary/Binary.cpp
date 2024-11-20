#include "Binary.h"

#include <iostream>

void Binary::push_front(bool d)
{
    Node* newNode{ new Node{d} };
    if (!head) head = tail = newNode;
    else
    {
        newNode->next = head;
        head->back = newNode;
        head = newNode;
    }
}

void Binary::push_back(bool d)
{
    Node* newNode{ new Node{d} };
    if (!head) head = tail = newNode;
    else
    {
        newNode->back = tail;
        tail->next = newNode;
        tail = newNode;
    }
}

Binary Binary::ones() const
{
    Binary binary{};
    Node* temp{ head };
    while (temp)
    {
        binary.push_back(!temp->data);
        temp = temp->next;
    }
    return binary;
}

Binary Binary::twos() const
{
    Binary binary{};
    Node* temp{ tail };
    bool flag{ false };
    while (temp)
    {
        if (flag) binary.push_front(!temp->data);
        else binary.push_front(temp->data);
        if (temp->data) flag = true;
        temp = temp->back;
    }
    return binary;
}

std::istream& operator>>(std::istream& in, Binary& binary)
{
    std::string str{};
	in >> str;
	for (auto c: str) binary.push_back(c - '0');
    return in;
}

std::ostream& operator<<(std::ostream& out, const Binary& binary)
{
    Binary::Node* temp{ binary.head };
    while (temp)
    {
        out << temp->data;
        temp = temp->next;
    }
    return out;
}

Binary operator+(const Binary& first, const Binary& second)
{
    Binary::Node* t1{ first.tail };
    Binary::Node* t2{ second.tail };

    Binary result{};
    bool carryon{ 0 };
    while (t1 && t2)
    {
        result.push_front(t1->data ^ t2->data ^ carryon);
        carryon = (t1->data && t2->data) || (t1->data || t2->data) && carryon;
        t1 = t1->back;
        t2 = t2->back;
    }
    while (t1)
    {
        result.push_front(t1->data ^ carryon);
        carryon = t1->data && carryon;
        t1 = t1->back;
    }
    while (t2)
    {
        result.push_front(t2->data ^ carryon);
        carryon = t2->data && carryon;
        t2 = t2->back;
    }
    if (carryon) result.push_front(carryon);
    return result;
}
