#ifndef STACK_H
#define STACK_H

template <typename T>
class Stack
{
public:
    Stack() = default;
    ~Stack() { while (!empty()) pop(); }

    void push(T data)
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

    T top() { return m_top->data; }
    bool empty() { return m_top == nullptr; }
    int  size()  { return m_size; }

private:
    struct Node {
        T data{};
        Node* next{};
    };
    Node* m_top{ nullptr };
    int m_size{ 0 };
};
#endif