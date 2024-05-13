#include <iostream>
#include <queue>
#include <stack>

int main()
{
    std::queue<int> kolejka;

    for (int i = 1; i <= 50; ++i)
    {
        kolejka.push(i);
        std::cout << "Dodano do kolejki: " << i << std::endl;
    }

    std::cout << "\nPobieranie elementów z kolejki:\n";
    while (!kolejka.empty())
    {
        int element = kolejka.front();
        std::cout << "Pobrano z kolejki: " << element << std::endl;
        kolejka.pop();
    }

    std::stack<int> stos;

    for (int i = 1; i <= 50; ++i)
    {
        stos.push(i);
        std::cout << "Dodano do stosu: " << i << std::endl;
    }

    std::cout << "\nPobieranie elementów ze stosu:\n";
    while (!stos.empty())
    {
        int element = stos.top();
        std::cout << "Pobrano ze stosu: " << element << std::endl;
        stos.pop();
    }
    return 0;
}
