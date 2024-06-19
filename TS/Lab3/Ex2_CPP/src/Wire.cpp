#include "Wire.h"
#include <algorithm>
#include "Wire.h"

const char Wire::DEFAULT_SIGNAL_SYMBOL = ' ';
const char Wire::OVERLAPPING_SIGNAL_SYMBOL = '#';
const char Wire::JAM_SIGNAL_SYMBOL = '!';

Wire::SignalPropagator::SignalPropagator(char symbol, int position, int tick_lifetime, Wire *wire)
    : symbol(symbol), left_position(position), right_position(position), tick_lifetime(tick_lifetime),
      tick_counter(tick_lifetime), wire(wire) {}

bool Wire::SignalPropagator::isActive() const
{
    return tick_counter > 0;
}

void Wire::SignalPropagator::tick()
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

void Wire::SignalPropagator::propagateSignal(int position)
{
    if (isPositionValid(position))
    {
        wire->signal_groups[position].emplace_back(symbol, tick_lifetime);
    }
}

bool Wire::SignalPropagator::isPositionValid(int position) const
{
    return 0 <= position && position < wire->getLength();
}

Wire::Wire(int length)
    : length(length), symbols(length, DEFAULT_SIGNAL_SYMBOL), signal_groups(length) {}

int Wire::getLength() const
{
    return length;
}

void Wire::tick()
{
    signal_propagators.erase(
        std::remove_if(signal_propagators.begin(), signal_propagators.end(),
                       [](SignalPropagator &sp)
                       { sp.tick(); return !sp.isActive(); }),
        signal_propagators.end());

    for (auto &signals : signal_groups)
    {
        signals.erase(
            std::remove_if(signals.begin(), signals.end(),
                           [](Signal &s)
                           { s.tick(); return !s.isActive(); }),
            signals.end());
    }

    updateSegmentSymbols();
}

void Wire::updateSegmentSymbols()
{
    for (int i = 0; i < length; ++i)
    {
        if (signal_groups[i].empty())
        {
            symbols[i] = DEFAULT_SIGNAL_SYMBOL;
        }
        else if (signal_groups[i].size() == 1)
        {
            symbols[i] = signal_groups[i][0].symbol;
        }
        else if (std::any_of(signal_groups[i].begin(), signal_groups[i].end(),
                             [](Signal &s)
                             { return s.symbol == JAM_SIGNAL_SYMBOL; }))
        {
            symbols[i] = JAM_SIGNAL_SYMBOL;
        }
        else
        {
            symbols[i] = OVERLAPPING_SIGNAL_SYMBOL;
        }
    }
}

void Wire::addSignal(int device_position, char signal_symbol, int tick_lifetime)
{
    signal_propagators.emplace_back(signal_symbol, device_position, tick_lifetime, this);
}

void Wire::addJamSignal(int device_position, int tick_lifetime)
{
    signal_propagators.emplace_back(JAM_SIGNAL_SYMBOL, device_position, tick_lifetime, this);
}

bool Wire::isFree(int position, char signal_symbol) const
{
    return symbols[position] == DEFAULT_SIGNAL_SYMBOL || symbols[position] == signal_symbol;
}

bool Wire::isCollision(int position, char signal_symbol) const
{
    return !isFree(position, signal_symbol);
}

bool Wire::isJammed(int position) const
{
    return symbols[position] == JAM_SIGNAL_SYMBOL;
}

std::string Wire::toString() const
{
    return std::string(symbols.begin(), symbols.end());
}
