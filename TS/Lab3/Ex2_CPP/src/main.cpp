#include <iostream>
#include <fstream>
#include <vector>
#include <memory>
#include "Device.h"
#include "Wire.h"

const int WIRE_LENGTH = 20;
const double TRANSMISSION_PROBABILITY = 0.04;
const int TICKS = 2000;
const std::string OUTPUT_FILENAME = "./output.txt";

int main()
{
    std::shared_ptr<Wire> wire = std::make_shared<Wire>(WIRE_LENGTH);
    std::vector<Device> devices = {
        Device('A', wire, 3),
        Device('B', wire, 7),
        Device('C', wire, 18),
    };

    std::ofstream output_file(OUTPUT_FILENAME);

    for (int i = 0; i < TICKS; ++i)
    {
        for (auto &device : devices)
        {
            if (static_cast<double>(rand()) / RAND_MAX < TRANSMISSION_PROBABILITY)
            {
                device.sendPacket();
            }
            device.tick();
        }
        wire->tick();
        output_file << wire->toString() << std::endl;
    }

    for (const auto &device : devices)
    {
        output_file << "Device " << device.getSuccessfulTransmissions()
                    << " successful transmissions, "
                    << device.getFailedTransmissions() << " failed transmissions.\n";
    }

    output_file.close();
    return 0;
}
