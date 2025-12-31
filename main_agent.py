from network_runner import run_network_config

def main():
    print("--- 🤖 STARTING AI NETWORK AGENT ---")
    
    # Define the intent (what we want to do)
    intent = "Configure GigabitEthernet1 description 'Managed_by_GitHub'"
    
    # Generate Commands (Hardcoded for stability, or use OpenAI if credits allow)
    print(f"📝 Intent: {intent}")
    commands = [
        "interface GigabitEthernet1",
        "description Managed_by_GitHub_Action",
        "no shutdown"
    ]
    print(f"⚙️  Generated {len(commands)} commands.")

    # Run the configuration
    result = run_network_config(commands)
    
    print("\n---------------------------------------")
    print(f"🚀 FINAL STATUS: {result}")
    print("---------------------------------------")

if __name__ == "__main__":
    main()
