#ifndef SIGNAL_H
#define SIGNAL_H

struct Signal
{
    char symbol;
    int ticks_left;

    Signal(char symbol, int ticks_left)
        : symbol(symbol), ticks_left(ticks_left) {}

    void tick()
    {
        ticks_left--;
    }

    bool isActive() const
    {
        return ticks_left > 0;
    }
};

#endif // SIGNAL_H
