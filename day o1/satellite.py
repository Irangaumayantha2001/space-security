import json
import random
import time

while True:
    telemetry_data = {
        "satellite": "CYBERNEOX-SAT01",
        "battery_voltage": round(random.uniform(7.0, 8.4), 2),
        "temperature": round(random.uniform(15, 35), 2),
        "signal_strength": random.randint(50, 100),
        "status": "ONLINE"
    }
    
    print(json.dumps(telemetry_data, indent=2))
    print("-" * 40)

    time.sleep(3)