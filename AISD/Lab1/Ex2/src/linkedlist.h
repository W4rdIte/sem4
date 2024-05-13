// linkedlist.h
#ifndef LINKEDLIST_H
#define LINKEDLIST_H

struct Node
{
    int data;
    Node *next;
};

struct List
{
    Node *head;
    int size;
};

void insert(List &l, int i);
List merge(const List &l1, const List &l2);
int searchCost(const List &l, int target);

#endif // LINKEDLIST_H
