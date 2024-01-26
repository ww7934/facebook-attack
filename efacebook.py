import requests

def facebook_attack(victim_id):
    print("Successful attack on Facebook page using ID: " + str(victim_id))
    print("Adding a Syrian touch... 🇸🇾")

if _name_ == "_main_":
    print("To run the tool, type cd and folder name, then ls")
    victim_id = input("Enter the victim's ID: ")
    facebook_attack(victim_id)

    attack_status = True
    if not attack_status:
        print("\033[91mAttack bar in red - Attack failed! 🚨\033[0m")
    else:
        print("\033[92mAttack bar in green - Successful attack! ✅\033[0m")
