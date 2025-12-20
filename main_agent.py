import os
import sys
from netmiko import ConnectHandler

def run_task():
    print("--- Starting Network Agent (Bypass Mode) ---")
    
    # We skip OpenAI and just type the command manually for testing
    print("Bypassing AI to save credits...")
    commands = ["interface GigabitEthernet1", "description Configured_by_GitHub_Action"]
    print(f"Generated Commands: {commands}")

    # Load Router Details
    host = os.getenv("DEVICE_IP")
    user = os.getenv("DEVICE_USER")
    pasw = os.getenv("DEVICE_PASS")

    # Connect to Device
    device = {
        "device_type": "cisco_ios",
        "host": host,
        "username": user,
        "password": pasw,
    }

    try:
        print(f"Connecting to {host}...")
        with ConnectHandler(**device) as net_connect:
            output = net_connect.send_config_set(commands)
            print("SUCCESS! Router Output:")
            print(output)
    except Exception as e:
        print(f"CONNECTION FAILED: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_task()


