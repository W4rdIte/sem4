#ifndef LIST_H
#define LIST_H

struct Node
{
    int data;
    Node *next;
    Node *prev;
};

struct List
{
    Node *head;
    int size;
};

void insert(List &l, int i);
List merge(const List &l1, const List &l2);
int searchCost(const List &l, int target);

#endif // LIST_H
