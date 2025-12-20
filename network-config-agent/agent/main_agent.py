import os
import sys
from openai import OpenAI
from netmiko import ConnectHandler

def run_task():
    print("--- Starting AI Network Agent ---")
    
    # Load secrets from GitHub environment
    api_key = os.getenv("OPENAI_API_KEY")
    host = os.getenv("DEVICE_IP")
    user = os.getenv("DEVICE_USER")
    pasw = os.getenv("DEVICE_PASS")

    if not api_key:
        print("ERROR: Missing OPENAI_API_KEY secret!")
        sys.exit(1)

    # 1. Ask AI for config
    client = OpenAI(api_key=api_key)
    intent = "Set description to 'Configured_by_Gemini_AI' on interface GigabitEthernet1"
    
    print(f"Requesting AI config for: {intent}")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Provide only Cisco IOS commands for: {intent}"}]
    )
    commands = response.choices[0].message.content.strip().split('\n')
    print(f"AI Generated Commands: {commands}")

    # 2. Connect to Device
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
