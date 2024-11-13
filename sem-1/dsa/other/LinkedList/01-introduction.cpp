#include <iostream>
#include <vector>
#include <array>

struct Node
{
    int data;   // 4 byte
    Node* next; // 8 byte
};

// creation
Node* convertArr2LL(std::vector<int> arr);

// tranersal
void printLL(Node* head);
int lengthOfLL(Node* head);
bool linearSearch(Node* head, int value);

// deletion
Node* removeHead(Node* head);
Node* removeTail(Node* head);
Node* removeK(Node* head, int k);
Node* removeData(Node* head, int data);
void deleteLL(Node* head);

// insertion

int main()
{
    std::vector<int> arr{2, 1, 3, 8};
    Node* head = convertArr2LL(arr);
    printLL(head);
    head = removeData(head, 80);
    printLL(head);
}










Node* removeData(Node* head, int data)
{
    if (!head) return nullptr; // no head
    if (head->data == data) // data found at first element
    {
        Node* temp{ head };
        head = head->next;
        delete temp;
        return head;
    }
    Node* temp{ head->next };
    Node* prev{ head }; // rememer previous
    while (temp)
    {
        if (temp->data == data)// checking temp
        {
            prev->next = temp->next;
            delete temp;
            return head;
        }
        prev = temp;
        temp = temp->next;
    }
    return head;
}

Node* removeK(Node* head, int k)
{
    if (!head) return nullptr; // no head
    if (k == 0) // k is first element
    {
        Node* temp{ head };
        head = head->next;
        delete temp;
        return head;
    }
    int cnt{ 0 };
    Node* temp{ head->next };
    Node* prev{ head };
    while (temp)
    {
        cnt++;
        if (cnt == k)
        {
            prev->next = temp->next;
            delete temp;
            return head;
        }
        prev = temp;
        temp = temp->next;
    }
    return head;
}

Node* removeTail(Node* head)
{
    if (!head->next || !head) // if no or single element present
    {
        delete head;
        return nullptr;
    }

    Node* temp{ head };
    while(temp->next->next) // go to second last
        temp = temp->next;
    delete temp->next;
    temp->next = nullptr;
    return head;
}

Node* removeHead(Node* head)
{
    if(!head) return nullptr;
    Node* temp{ head };
    head = head->next;
    delete temp;
    return head;
}

Node* convertArr2LL(std::vector<int> arr)
{
    Node* head{ new Node{arr[0]} };
    Node* mover{ head };
    for (std::size_t i{ 1 }; i < std::size(arr); ++i)
    {
        Node* temp{ new Node{arr[i]} };
        mover->next = temp;
        mover = temp;
    }
    return head;
}

void printLL(Node* head)
{
    Node* temp = head;
    while (temp)
    {
        std::cout << temp->data << ' ';
        temp = temp->next;
    }
    std::cout << '\n';
}

int lengthOfLL(Node* head)
{
    int cnt{ 0 };
    Node* temp = head;
    if (!temp) return 0;
    do ++cnt;
    while (temp = temp->next);
    
    return cnt;
}

void deleteLL(Node* head)
{
    Node* temp = head;
    while(temp)
    {
        head = head->next;
        delete temp;
        temp = head;
    }
    delete temp;
}

bool linearSearch(Node* head, int value)
{
    Node* temp = head;
    while (temp)
    {
        if (temp->data == value)
            return true;
        temp = temp->next;
    }
    return false;
}
