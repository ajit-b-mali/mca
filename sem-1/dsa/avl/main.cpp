#include <iostream>     // for std::cout, std::cin
#include <algorithm>    // for std::max

struct Node
{
    int data = 0;
    Node* left = nullptr;
    Node* right = nullptr;
};

int height(Node* node)
{
    if (!node)
        return 0;

    int lh = height(node->left);
    int rh = height(node->right);

    return std::max(lh, rh) + 1;
}

int balanceFactor(Node* node)
{
    if (!node) return 0;
    int lh = height(node->left);
    int rh = height(node->right);
    return lh - rh;
}

// LL imbalance
Node* llRotate(Node* a)
{
    Node* b = a->left;
    a->left = b->right;
    b->right = a;
    return b;
}

// RR imbalance
Node* rrRotate(Node* a)
{
    Node* b = a->right;
    a->right = b->left;
    b->left = a;
    return b;
}

// LR imbalance
Node* lrRotate(Node* a)
{
    a->left = rrRotate(a->left);
    a = llRotate(a);
    return a;
}

// RL imbalance
Node* rlRotate(Node* a)
{
    a->right = llRotate(a->right);
    a = rrRotate(a);
    return a;
}

Node* insertion(Node* root, int data)
{
    if (!root)
        return new Node{ data };
    
    if (data < root->data)
        root->left = insertion(root->left, data);
    else if (data > root->data)
        root->right = insertion(root->right, data);
    else
        return root;

    int bf = balanceFactor(root);
    if (bf > 1 && data < root->left->data)
        root = llRotate(root);
    else if (bf > 1 && data > root->left->data)
        root = lrRotate(root);
    else if (bf < -1 && data > root->right->data)
        root = rrRotate(root);
    else if (bf < -1 && data < root->right->data)
        root = rlRotate(root);

    return root;
}

/**
 * 1. perform normal BST deletion
 *      1. node has no childs
 *          just remove node
 *      2. node has only one child
 *          make child node root
 *      3. node has both childs
 *          make smaller node root and move right node at end of the right subtree of smaller node
 */
Node* inorderSuccesor(Node* node)
{
    Node* curr = node->right;
    while (curr->left)
        curr = curr->left;
    return curr;
}

Node* deletion(Node* root, int data)
{
    if (!root)
        return nullptr;

    if (data < root->data)
        root->left = deletion(root->left, data);
    else if (data > root->data)
        root->right = deletion(root->right, data);
    else
    {
        // no child or only right child
        if (!root->left)
        {
            Node* temp = root->right;
            delete root;
            root = temp;
        }
        // only left child
        else if (!root->right)
        {
            Node* temp = root->left;
            delete root;
            root = temp;
        }
        else
        {
            Node* succesor = inorderSuccesor(root);
            root->data = succesor->data;
            root->right = deletion(root->right, succesor->data);
        }
    }

    return root;
}

void preOrder(Node* root)
{
    if (root)
    {
        std::cout << root->data << ' ';
        preOrder(root->left);
        preOrder(root->right);
    }
}

int main()
{
    Node* root = nullptr;
    root = insertion(root, 1);
    root = insertion(root, 2);
    root = insertion(root, 3);
    root = insertion(root, 4);
    root = insertion(root, 5);
    root = insertion(root, 6);
    root = insertion(root, 7);

    preOrder(root);
    std::cout << '\n';

    deletion(root, 4);

    preOrder(root);
    std::cout << '\n';

    return 0;
}