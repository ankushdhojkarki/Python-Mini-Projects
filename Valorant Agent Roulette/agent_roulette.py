import random


agent_roles = {
    "Controller": ["Brimstone", "Viper", "Omen", "Astra", "Harbor", "Clove"],
    "Duelist": ["Phoenix", "Reyna", "Jett", "Raze", "Yoru", "Neon", "Iso", "Walay"],
    "Initiator": ["Sova", "Breach", "Skye", "Kay/0", "Fade", "Gekko", "Tejo"],
    "Sentinel": ["Sage", "Cypher", "KillJoy", "Chamber", "DeadLock", "Vyse"]
}


def assign_agent(player_num):
    
    name = input(f"\nEnter name for Player {player_num}: ").strip()

    
    print("\nAvailable roles: Controller, Duelist, Initiator, Sentinel")
    role = input(f"\n{name}, which role would you like to play? ").strip().capitalize()

    while role not in agent_roles:
        print("Invalid role. Please choose from Controller, Duelist, Initiator, or Sentinel.")
        role = input(f"\n{name}, which role would you like to play? ").strip().capitalize()

    
    agent = random.choice(agent_roles[role])

    
    print(f"\n{name}, your assigned agent from the {role} role is: {agent}\n")


assign_agent(1)
assign_agent(2)
