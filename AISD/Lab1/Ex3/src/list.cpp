#include "list.h"
#include <cstdlib>

void insert(List &l, int i)
{
    Node *newNode = new Node{i, nullptr, nullptr};
    if (l.head == nullptr)
    {
        l.head = newNode;
        newNode->next = l.head;
        newNode->prev = l.head;
    }
    else
    {
        Node *last = l.head->prev;
        last->next = newNode;
        newNode->prev = last;
        newNode->next = l.head;
        l.head->prev = newNode;
    }
    l.size++;
}

List merge(const List &l1, const List &l2)
{
    List mergedList{nullptr, 0};
    Node *current = l1.head;
    do
    {
        insert(mergedList, current->data);
        current = current->next;
    } while (current != l1.head);

    current = l2.head;
    do
    {
        insert(mergedList, current->data);
        current = current->next;
    } while (current != l2.head);

    return mergedList;
}

int searchCost(const List &l, int target)
{
    int cost = 0;
    Node *current = l.head;

    bool forward = rand() % 2 == 0;

    do
    {
        cost++;
        if (current->data == target)
        {
            return cost;
        }
        current = forward ? current->next : current->prev;
    } while (current != l.head);

    return cost;
}
