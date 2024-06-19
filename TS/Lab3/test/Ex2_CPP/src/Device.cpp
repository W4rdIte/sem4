#include "Device.h"
#include <iostream>

Device::Device(char symbol, std::shared_ptr<Wire> wire, int position_in_wire)
    : symbol(symbol), wire(wire), position_in_wire(position_in_wire),
      min_packet_time(2 * wire->getLength()), tick_counter(0), retransmissions_counter(0),
      backoff_waiting_ticks(0), state(State::RECEIVING), is_ready_to_transmit(true),
      successful_transmissions(0), failed_transmissions(0) {}

void Device::tick()
{
    switch (state)
    {
    case State::TRANSMITTING:
        transmit();
        break;
    case State::WAITING_FOR_WIRE:
        sendPacket();
        break;
    case State::JAMMING:
        jam();
        break;
    case State::BACKOFF:
        backoff();
        break;
    default:
        break;
    }
}

void Device::sendPacket()
{
    if (is_ready_to_transmit)
    {
        if (wire->isCollision(position_in_wire, symbol))
        {
            state = State::WAITING_FOR_WIRE;
        }
        else
        {
            state = State::TRANSMITTING;
            tick_counter = 0;
            wire->addSignal(position_in_wire, symbol, min_packet_time);
            is_ready_to_transmit = false;
        }
    }
}

void Device::transmit()
{
    if (wire->isCollision(position_in_wire, symbol))
    {
        if (wire->isJammed(position_in_wire))
        {
            state = State::BACKOFF;
            retransmissions_counter = 0;
        }
        else
        {
            state = State::JAMMING;
            wire->addJamSignal(position_in_wire, min_packet_time);
            tick_counter = 0;
        }
        failed_transmissions++;
    }
    else
    {
        tick_counter++;
        if (tick_counter == min_packet_time)
        {
            state = State::RECEIVING;
            is_ready_to_transmit = true;
            successful_transmissions++;
        }
    }
}

void Device::jam()
{
    tick_counter++;
    if (tick_counter == min_packet_time)
    {
        state = State::BACKOFF;
        retransmissions_counter = 0;
        calculate_exponential_backoff();
    }
}

void Device::backoff()
{
    backoff_waiting_ticks--;
    if (backoff_waiting_ticks <= 0)
    {
        if (wire->isFree(position_in_wire, symbol))
        {
            state = State::TRANSMITTING;
            tick_counter = 0;
            wire->addSignal(position_in_wire, symbol, min_packet_time);
        }
        else
        {
            calculate_exponential_backoff();
            failed_transmissions++;
        }
    }
}

void Device::calculate_exponential_backoff()
{
    retransmissions_counter++;
    if (retransmissions_counter == MAX_BACKOFF_TRANSMISSION_ATTEMPTS)
    {
        throw std::runtime_error("Max transmission attempts reached.");
    }
    int k = std::min(retransmissions_counter, 10);
    backoff_waiting_ticks = (rand() % (1 << k)) * min_packet_time;
}
