#ifndef DEVICE_H
#define DEVICE_H

#include <random>
#include <memory>
#include "Wire.h"

class Device
{
public:
    enum class State
    {
        RECEIVING,
        TRANSMITTING,
        WAITING_FOR_WIRE,
        JAMMING,
        BACKOFF
    };

    Device(char symbol, std::shared_ptr<Wire> wire, int position_in_wire);

    void tick();
    void sendPacket();

private:
    static const int MAX_BACKOFF_TRANSMISSION_ATTEMPTS = 16;

    char symbol;
    std::shared_ptr<Wire> wire;
    int position_in_wire;

    int min_packet_time;
    int tick_counter;
    int retransmissions_counter;
    int backoff_waiting_ticks;
    State state;
    bool is_ready_to_transmit;

    int successful_transmissions;
    int failed_transmissions;

    void transmit();
    void jam();
    void backoff();
    void calculate_exponential_backoff();
};

#endif // DEVICE_H
