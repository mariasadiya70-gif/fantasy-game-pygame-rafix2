class Game:
    def __init__(self):
        self.characters = []
        self.enemies = []
        self.npcs = []
        self.state = 'idle'

    def start(self):
        print("Game started!")
        self.load_game()

    def load_game(self):
        # Load game data from a file
        pass

    def save_game(self):
        # Save game data to a file
        pass

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

    def attack_enemy(self, enemy):
        enemy.health -= self.attack
        print(f'{self.name} attacks {enemy.name} for {self.attack} damage!')

class Enemy(Character):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)

class NPC:
    def __init__(self, name, dialogue):
        self.name = name
        self.dialogue = dialogue

    def interact(self):
        print(f'{self.name}: {self.dialogue}')

# Game loop
if __name__ == '__main__':
    game = Game()
    game.start()