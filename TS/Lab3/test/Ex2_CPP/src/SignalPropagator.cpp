#include "SignalPropagator.h"
#include "Wire.h"

SignalPropagator::SignalPropagator(char symbol, int position, int tick_lifetime, Wire *wire)
    : symbol(symbol), left_position(position), right_position(position), tick_lifetime(tick_lifetime),
      tick_counter(tick_lifetime), wire(wire) {}

bool SignalPropagator::isActive() const
{
    return tick_counter > 0;
}

void SignalPropagator::tick()
{
    tick_counter--;
    if (left_position == right_position)
    {
        propagateSignal(left_position);
    }
    else
    {
        propagateSignal(left_position);
        propagateSignal(right_position);
    }
    left_position--;
    right_position++;
}

void SignalPropagator::propagateSignal(int position)
{
    if (isPositionValid(position))
    {
        wire->signal_groups[position].emplace_back(symbol, tick_lifetime);
    }
}

bool SignalPropagator::isPositionValid(int position) const
{
    return 0 <= position && position < wire->getLength();
}
