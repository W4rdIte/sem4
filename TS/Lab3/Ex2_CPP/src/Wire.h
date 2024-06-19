#ifndef WIRE_H
#define WIRE_H

#include <vector>
#include <string>

class Wire
{
public:
    static const char DEFAULT_SIGNAL_SYMBOL;
    static const char OVERLAPPING_SIGNAL_SYMBOL;
    static const char JAM_SIGNAL_SYMBOL;

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

    Wire(int length);

    int getLength() const;
    void tick();
    void addSignal(int device_position, char signal_symbol, int tick_lifetime);
    void addJamSignal(int device_position, int tick_lifetime);
    bool isFree(int position, char signal_symbol) const;
    bool isCollision(int position, char signal_symbol) const;
    bool isJammed(int position) const;
    std::string toString() const;

private:
    int length;
    std::vector<char> symbols;
    std::vector<std::vector<Signal>> signal_groups;
    std::vector<SignalPropagator> signal_propagators;

    void updateSegmentSymbols();
};

#endif // WIRE_H
