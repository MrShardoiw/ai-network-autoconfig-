import os
from openai import OpenAI
from netmiko import ConnectHandler

def run_network_task():
    # 1. Get credentials from GitHub Environment
    api_key = os.getenv("OPENAI_API_KEY")
    device_ip = os.getenv("DEVICE_IP")
    device_user = os.getenv("DEVICE_USER")
    device_pass = os.getenv("DEVICE_PASS")

    if not api_key:
        print("ERROR: OpenAI API Key is missing!")
        return

    client = OpenAI(api_key=api_key)

    # 2. Ask AI for the config
    intent = "Configure a description 'Managed_by_GitHub' on interface GigabitEthernet1"
    print(f"Asking AI to generate config for: {intent}")
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Generate Cisco IOS commands for: {intent}. No text, just commands."}]
    )
    config_commands = response.choices[0].message.content.strip()
    print(f"Generated Commands:\n{config_commands}")

    # 3. Connect to the Cisco Sandbox
    device = {
        "device_type": "cisco_ios",
        "host": device_ip,
        "username": device_user,
        "password": device_pass,
    }

    try:
        print(f"Connecting to {device_ip}...")
        with ConnectHandler(**device) as net_connect:
            output = net_connect.send_config_set(config_commands.split("\n"))
            print("SUCCESS! Output from Router:")
            print(output)
    except Exception as e:
        print(f"FAILED to connect: {e}")

if __name__ == "__main__":
    run_network_task()
