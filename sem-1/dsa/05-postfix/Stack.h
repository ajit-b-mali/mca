#ifndef STACK_H
#define STACK_H

#include <iostream>

struct Node {
    char data{};
    Node* next{};
};

class Stack
{
public:
    void push(char data)
    {
        m_top = new Node{data, m_top};
        m_size++;
    }

    void pop()
    {
        if (empty()) return;
        Node* temp = m_top;
        m_top = m_top->next;
        m_size--;
        delete temp;
    }

    char top()   { return m_top->data; }
    bool empty() { return m_top;       }
    int  size()  { return m_size;      }

private:
    Node* m_top{ nullptr };
    int m_size{ 0 };
};
#endif