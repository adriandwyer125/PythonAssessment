class Card:
    def __init__(self, name, attack, style):
        self.__name = name
        self.__attack = attack
        self.__style = style
        self.__health = 100
        self.__is_active = True

    # ------------------------------------------------------------------
    # Copy
    # ------------------------------------------------------------------
    def copy(self):
        return Card(self.__name, self.__attack, self.__style)

    # ------------------------------------------------------------------
    # Getters
    # ------------------------------------------------------------------
    def get_name(self):
        return self.__name

    def get_attack(self):
        return self.__attack

    def get_style(self):
        return self.__style

    def get_health(self):
        return self.__health

    def is_active(self):
        return self.__is_active

    # ------------------------------------------------------------------
    # Mutations
    # ------------------------------------------------------------------
    def take_damage(self, damage):
        """Reduce health by damage. Deactivates the card if health reaches 0 or below."""
        self.__health -= damage
        if self.__health <= 0:
            self.__health = 0
            self.__is_active = False

    # ------------------------------------------------------------------
    # Display
    # ------------------------------------------------------------------
    def __str__(self):
        return f"{self.__name} ({self.__style}) | ATK: {self.__attack} | HP: {self.__health}"