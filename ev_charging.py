import time
import random

class EVCharger:
    def __init__(self, battery_capacity_kwh=40, charging_rate_kw=7.4):
        self.capacity = battery_capacity_kwh
        self.rate = charging_rate_kw
        self.current_charge = 0.0
        self.is_charging = False

    def start_charging(self, current_percent):
        self.current_charge = (current_percent / 100) * self.capacity
        self.is_charging = True
        print(f"Charging started. Current level: {current_percent}%")

    def charge_step(self, minutes=1):
        if not self.is_charging or self.current_charge >= self.capacity:
            self.is_charging = False
            return

        energy_added = self.rate * (minutes / 60)  # kWh added in this step
        self.current_charge = min(self.current_charge + energy_added, self.capacity)

        # Simulate sensor noise (like a real IoT reading)
        voltage = round(random.uniform(220, 240), 1)
        current = round(random.uniform(15, 32), 1)

        percent = (self.current_charge / self.capacity) * 100
        print(f"[{minutes} min] Charge: {percent:.1f}% | "
              f"Voltage: {voltage}V | Current: {current}A")

        if self.current_charge >= self.capacity:
            self.is_charging = False
            print("Battery fully charged. Stopping charge.")

    def status(self):
        percent = (self.current_charge / self.capacity) * 100
        return f"Battery at {percent:.1f}% ({self.current_charge:.2f}/{self.capacity} kWh)"


# --- Simulation ---
if __name__ == "__main__":
    ev = EVCharger(battery_capacity_kwh=40, charging_rate_kw=7.4)
    ev.start_charging(current_percent=20)

    while ev.is_charging:
        ev.charge_step(minutes=10)
        time.sleep(0.5)  # simulate real-time delay

    print(ev.status())
