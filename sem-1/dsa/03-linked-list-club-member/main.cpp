#include <iostream>
#include <string>

struct Data { std::string prn; std::string name; std::string ay; };
struct Node { Data data; Node* next; };

Node* append(const Data& data, Node* head = nullptr);
Node* remove(const std::string& prn, Node* head);
int len(Node* head);
void print(Node* head, const std::string& start);
Node* concat(Node* first, Node* second);

std::string get_string(const std::string& prompt)
{
    std::cout << prompt;
    std::string value;
    std::getline(std::cin, value);
    return value;
}

int main()
{
    Node* head = nullptr;
    int n = 0;
    std::cout << "How many entries? >>> ";
    std::cin >> n;
	std::cin.ignore();
    for (int i{ 0 }; i < n; ++i)
    {
        auto prn{ get_string("Enter prn: ") };
        auto name{ get_string("Enter name: ") };
        auto ay{ get_string("Enter academic year: ") };
        head = append({prn, name, ay}, head);
    }
    print(head, "\nLL:\n");
}

Node* append(const Data& data, Node* head)
{
    if (!head) return new Node{data};
    Node* temp{ head };
    while (temp->next) temp = temp->next;
    temp->next = new Node{data};
    return head;
}

Node* remove(const std::string& prn, Node* head)
{
    if (!head) return nullptr;
    Node* temp{ head };
    if (head->data.prn == prn)
    {
        head = head->next;
        delete temp;
    }
    else while (temp->next)
    {
        if (temp->next->data.prn == prn)
        {
            Node* trash{ temp->next };
            temp->next = temp->next->next;
			trash->next = nullptr;
            delete trash;
            break;
        }
        temp = temp->next;
    }
    return head;
}

int len(Node* head)
{
    Node* temp{ head };
    int cnt{ 0 };
    while (temp && ++cnt) temp = temp->next;
    return cnt;
}

void print(Node* head, const std::string& start)
{
    std::cout << start;
    Node* temp{ head };
    while (temp)
    {
        std::cout << temp->data.prn << ' ' << temp->data.name << ' ' << temp->data.ay << '\n';
        temp = temp->next;
    }
    std::cout << '\n';
}

Node* concat(Node* first, Node* second)
{
    if (!first) return second;
    if (!second) return first;
    Node* temp{ first };
    while (temp->next) temp = temp->next;
    temp->next = second;
    return first;
}

