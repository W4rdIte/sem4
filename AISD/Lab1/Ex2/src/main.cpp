// main.cpp
#include <iostream>
#include <cstdlib>
#include <ctime>
#include "linkedlist.h"

int main()
{
    srand(static_cast<unsigned>(time(nullptr)));

    int T[10000];
    for (int i = 0; i < 10000; ++i)
    {
        T[i] = rand() % 100001;
    }

    List L{nullptr, 0};
    for (int i = 0; i < 10000; ++i)
    {
        insert(L, T[i]);
    }

    int totalCost1 = 0;
    int totalCost2 = 0;

    for (int i = 0; i < 1000; ++i)
    {
        int randomIndex = rand() % 10000;
        int target1 = T[randomIndex];
        int target2 = rand() % 100001;

        totalCost1 += searchCost(L, target1);
        totalCost2 += searchCost(L, target2);
    }

    double averageCost1 = static_cast<double>(totalCost1) / 1000;
    double averageCost2 = static_cast<double>(totalCost2) / 1000;

    std::cout << "Average search cost for numbers in T: " << averageCost1 << std::endl;
    std::cout << "Average search cost for random numbers: " << averageCost2 << std::endl;

    return 0;
}
