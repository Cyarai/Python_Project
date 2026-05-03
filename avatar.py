import random

class Avatar:
    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.attack_power = random.randint(5, 20)  
        self.defense = random.randint(3, 10)
        self.max_health = 100
        self.current_health = 100
        self.enemy_damage = random.randint(5, 20)  
        self.enemy_health = 100
        self.enemy_max_health = 100
        self.enemy_defense = random.randint(3, 10)  

    def health_bar(self, current, max_health, name=""):
        bar_length = 20
        ratio = current / max_health
        filled = int(bar_length * ratio)
        bar = '█' * filled + '░' * (bar_length - filled)
        print(f"{name}[{bar}] {current}/{max_health}")

    def display_info(self):
        print(f"  Avatar: {self.name} | Power: {self.power} | ATK: {self.attack_power} | DEF: {self.defense}")
        print(f"  Enemy: ATK: {self.enemy_damage} | DEF: {self.enemy_defense}")
        self.health_bar(self.current_health, self.max_health, "You: ")
        self.health_bar(self.enemy_health, self.enemy_max_health, "Enemy: ")
    
    def attack(self): 
        
        raw_damage = random.randint(self.attack_power - 2, self.attack_power + 5)
        enemy_block = min(raw_damage, self.enemy_defense + random.randint(-1, 2))
        final_damage = max(0, raw_damage - enemy_block)
        
        self.enemy_health = max(0, self.enemy_health - final_damage)
        print(f"  {self.name} hits for {raw_damage}! Enemy blocks {enemy_block}, takes {final_damage}!")
        self.health_bar(self.enemy_health, self.enemy_max_health, "Enemy: ")
        return final_damage
    
    def enemy_attack(self):
       
        raw_damage = random.randint(self.enemy_damage - 3, self.enemy_damage + 5)
        your_block = min(raw_damage, self.defense + random.randint(-2, 3))
        damage_taken = max(0, raw_damage - your_block)
        
        self.current_health = max(0, self.current_health - damage_taken)
        print(f" Enemy strikes for {raw_damage}! You block {your_block}, take {damage_taken}!")
        self.health_bar(self.current_health, self.max_health, "You: ")
        return damage_taken

    def defend(self):
        print(f" {self.name} braces for impact! (+Defense bonus)")
        self.enemy_attack()  # Your defense already helps in enemy_attack()
    
    def rest(self):
        heal = random.randint(10, 20)
        self.current_health = min(self.max_health, self.current_health + heal)
        print(f" {self.name} rests and heals {heal} HP!")
        self.health_bar(self.current_health, self.max_health, "You: ")

    def battle_loop(self):
        print(f"\n  {self.name} enters battle!\n")
        self.display_info()
        
        while self.current_health > 0 and self.enemy_health > 0:
            print("\n" + "="*50)
            print("1️ Attack | 2️ Defend | 3️ Rest | 4️ Quit")
            choice = input("Your move: ").strip()
            
            if choice == '1':
                self.attack()
                if self.enemy_health > 0:
                    print("\n Enemy counterattacks!")
                    self.enemy_attack()
                    
            elif choice == '2':
                self.defend()
            elif choice == '3':
                self.rest()
                if self.enemy_health > 0:
                    print("\n Enemy attacks while you rest!")
                    self.enemy_attack()
            elif choice == '4':
                print(" Battle ended.")
                return
            else:
                print(" Invalid! Choose 1-4")
                continue
        
        if self.current_health <= 0:
            print("\n YOU LOSE!")
        else:
            print("\n VICTORY! Enemy defeated!")
            print(f" Final Health - You: {self.current_health}/{self.max_health}")


avatar1 = Avatar("Aang", "Air")
avatar1.battle_loop()