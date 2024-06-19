#ifndef SIGNALPROPAGATOR_H
#define SIGNALPROPAGATOR_H

#include <vector>
#include "Signal.h"

class Wire; // Forward declaration

class SignalPropagator
{
public:
    SignalPropagator(char symbol, int position, int tick_lifetime, Wire *wire);

    bool isActive() const;
    void tick();

private:
    char symbol;
    int left_position;
    int right_position;
    int tick_lifetime;
    int tick_counter;
    Wire *wire;

    void propagateSignal(int position);
    bool isPositionValid(int position) const;
};

#endif // SIGNALPROPAGATOR_H
