# EV-Charging-Simulation
# EV-Charging-Simulation

## Overview
This is a Python-based Electric Vehicle (EV) Charging Simulation project. The program simulates a **50 kWh** EV battery charging with a **7.68 kW** charger and displays the battery percentage, voltage, and current until the battery is fully charged.

## Features
- Simulates a 50 kWh EV battery.
- Uses a 7.68 kW charging rate.
- Displays battery percentage in real time.
- Shows simulated voltage (220–240 V) and current (15–32 A).
- Automatically stops charging when the battery reaches 100%.

## Technologies Used
- Python 3
- `time` module
- `random` module
- GitHub

## Project Configuration
- Battery Capacity: **50 kWh**
- Charging Rate: **7.68 kW**
- Initial Charge: **20%**
- Charging Interval: **10 minutes**

## File
- `ev_charging.py` – Main Python simulation program.

## Sample Output

```text
Charging started. Current level: 20%
[10 min] Charge: 22.6% | Voltage: 231.4V | Current: 24.8A
[20 min] Charge: 25.1% | Voltage: 226.8V | Current: 19.5A
Battery fully charged. Stopping charge.
Final Battery Level: 100.0% | Energy Stored: 50.00 kWh
```

## Future Improvements
- Charging cost calculation
- Battery health monitoring
- GUI dashboard
- IoT sensor integration

## Author
Kalika Revanna
