// linkedlist.cpp
#include "linkedlist.h"

void insert(List &l, int i)
{
    Node *newNode = new Node{i, nullptr};
    if (l.head == nullptr)
    {
        l.head = newNode;
        newNode->next = l.head;
    }
    else
    {
        Node *last = l.head;
        while (last->next != l.head)
        {
            last = last->next;
        }
        last->next = newNode;
        newNode->next = l.head;
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
    do
    {
        cost++;
        if (current->data == target)
        {
            return cost;
        }
        current = current->next;
    } while (current != l.head);

    return cost;
}