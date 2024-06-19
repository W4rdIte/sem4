#ifndef WIRE_H
#define WIRE_H

#include <vector>
#include <string>
#include "Signal.h"
#include "SignalPropagator.h"

class Wire
{
public:
    static const char DEFAULT_SIGNAL_SYMBOL;
    static const char OVERLAPPING_SIGNAL_SYMBOL;
    static const char JAM_SIGNAL_SYMBOL;

    Wire(int length);

    int getLength() const;
    void tick();
    void addSignal(int device_position, char signal_symbol, int tick_lifetime);
    void addJamSignal(int device_position, int tick_lifetime);
    bool isFree(int position, char signal_symbol) const;
    bool isCollision(int position, char signal_symbol) const;
    bool isJammed(int position) const;
    std::string toString() const;

    std::vector<std::vector<Signal>> signal_groups;

private:
    int length;
    std::vector<char> symbols;
    std::vector<SignalPropagator> signal_propagators;

    void updateSegmentSymbols();
};

#endif // WIRE_H
